import re
from lxml import html
import requests
from PIL import Image
import os
from hashlib import md5


# 来自官方demo
class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


def main():
    # 需要回帖的url 去掉后面那些有的没的后缀，但是最后这个斜杠需要
    db_url = "https://www.douban.com/group/topic/218863065/"
    # 你的cookie
    Cookie = 'bid=LnTf54vt3i0; douban-fav-remind=1; ll="118282"; dbcl2="164776595:8akuwQXyElQ"; push_doumail_num=0; __utmv=30149280.16477; push_noty_num=0; ck=qSzc; ap_v=0,6.0; __utma=30149280.882459586.1616824928.1617868431.1618382459.9; __utmc=30149280; __utmz=30149280.1618382459.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.85.5.1618382967262'
    # 回复内容
    replay_comment = "up 来自elmagnifico的自动回复"

    # 首先超级鹰官方注册，同时微信关注一下官方然后绑定你的账号，获取1000题分
    # 豆瓣验证码部分存在超过6位的英文，1元的资源包无法识别，需要更高级，就需要消耗题分。
    # 1元试用资源包（8001官方不保证全能识别），豆瓣的验证码基本都不能识别，很坑，建议别买，就试用一下，1000题分够了
    # 如果有必要再买3008类型的题分吧，我下面的代码是兼容了8001和3008类型，实际上可以去掉8001的

    # 超级鹰用户名
    Chaojiying_user_name = "elmagnificocj"
    # 超级鹰密码
    Chaojiying_password = "elmagnifico93"
    # 用户中心>>软件ID 生成一个
    Chaojiying_software_id = "914754"

    headers = {
        "Host": "www.douban.com",
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
        "Cookie": ''
    }
    params = {
        "ck": " ",
        "rv_comment": " ",
    }

    headers['Referer'] = db_url + '?start=0'
    headers['Cookie'] = Cookie
    # print(headers['Referer'])

    ck_index = Cookie.find('ck=')
    # print(ck)
    ck_str = Cookie[ck_index + 3:ck_index + 7]
    # print(ck_str)

    params['ck'] = ck_str
    params['rv_comment'] = replay_comment

    db_url_rpl = db_url + 'add_comment'
    # print(db_url_rpl)

    # get captcha
    response = requests.post(db_url, headers=headers, data=params, verify=False).content.decode()
    selector = html.fromstring(response)
    captcha_image = selector.xpath("//img[@id=\"captcha_image\"]/@src")
    if (captcha_image):
        # print(captcha_image)
        captcha_id = selector.xpath("//input[@name=\"captcha-id\"]/@value")
        # print(captcha_id)

        captcha_name = re.findall("id=(.*?):", captcha_image[0])  # findall返回的是一个列表
        filename = "douban_%s.jpg" % (str(captcha_name[0]))
        print("验证码文件名为：" + filename)
        captcha_image[0] = 'https:' + captcha_image[0]

        # 创建文件名
        with open(filename, 'wb') as f:
            # 以二进制写入的模式在本地构建新文件
            header = {
                'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",'
                , 'Referer': captcha_image[0]}
            f.write(requests.get(captcha_image[0], headers=header).content)
            print("%s下载完成" % filename)
        print(os.path.dirname(os.path.realpath(__file__)) + r'\\' + filename)
        img = Image.open(os.path.dirname(os.path.realpath(__file__)) + r'\\' + filename)
        # img.show()

        captcha_veryfy = ""
        # captcha_veryfy = input("输入验证码:").replace('\n', '').replace('\n', '')

        chaojiying = Chaojiying_Client(Chaojiying_user_name, Chaojiying_password, Chaojiying_software_id)
        im = open(filename, 'rb').read()

        ret = (chaojiying.PostPic(im, 8001))
        if ret != None:
            if ret['pic_str'] == '':
                print("8001无法识别，切换到3008尝试识别")
                ret = chaojiying.PostPic(im, 3008)
            if ret['pic_str'] != '':
                captcha_veryfy = ret['pic_str']
            else:
                print("验证码识别错误")
                return
        else:
            print("验证码接口错误")
            return

        print("识别验证码：" + captcha_veryfy)
        params['captcha-solution'] = captcha_veryfy
        params['captcha-id'] = captcha_id[0]
        params['start'] = 0

        # replay
        requests.post(db_url_rpl, headers=headers, data=params, verify=False)

    else:
        # 无需验证码，直接回复即可
        requests.post(db_url_rpl, headers=headers, data=params, verify=False)

    # input


if __name__ == '__main__':
    main()
