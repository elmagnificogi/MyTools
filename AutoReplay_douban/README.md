# 豆瓣自动回复/刷帖器



## 更新 2021.4.14

- 增加超级鹰验证码接口，可以自动回帖了
- 后续不再更新，合并到我的小工具里去了

> https://github.com/elmagnificogi/MyTools



#### 现状

无论是咸鱼也好，58也好（赶集也是58的），租房信息基本都沦陷了。

58上自己发的二房东的租房信息或者是合租的信息明显不如中介验证过的或者有房产证直接验证过的信息推广的更广，甚至很久都无人问津。

由于自己当了二房东所以不得不想办法招租啊，然后发现豆瓣上比58什么的要靠谱一点，但是依然逃不过那些公寓啊、中介的毒手，很多帖子说的很好，然后仔细一看都是各种公寓的招租贴，很坑，描述的房子贼好，价格贼便宜基本都是实际价格1/3到1/2的样子，等你去问有没有他说有，让你看房，带你看完以后告诉你便宜的都租了，现在就剩这个贵的，你要不要吧，巨坑无比。

然后这些个人呢还成天刷贴，只要一刷帖就会导致我们这种普通人发的帖子沉下去了，想找的人也看不到了，为了不让我帖子下沉只好自己刷贴，然后我加了好几个团体，都分别有发一样的帖子，为了方便自然要有一个刷帖的东西，刚巧又看到了下面这个回帖器的帖子，就稍微改改写了回复器

参考来源
> https://juejin.im/post/5b85630c6fb9a01a0231210c#heading-13



#### 使用

首先是在这里放入需要刷的帖子

```python
db_url = "https://www.douban.com/group/topic/141002674/"
```
然后是填写你的Cookie和回帖内容

    db_url = "https://www.douban.com/group/topic/141002674/"
    Cookie = 'bid=b16kx11APXM; ll="118282"; douban-fav-remind=1; douban-profile-remind=1; ct=y; _ga=GA1.2.2116562073.1558235896; _gid=GA1.2.1026987747.1558254879; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1558265006%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D57aywD0Q6WTnl7XKbIHuE8zWE5epzov3Jk7LtVUL7clOAGuZmUBS-a-MNTzYiTmfD2AoTT8mx1my6hYutqi9ia%26wd%3D%26eqid%3Dbfe569310000a652000000065ce0caec%22%5D; ps=y; ap_v=0,6.0; dbcl2="164776595:eNdVT94l/C8"; ck=OLvw; _pk_id.100001.8cb4=cc09238f4c125f7c.1558235895.5.1558275428.1558256275.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.2116562073.1558235896.1558251801.1558265006.5; __utmb=30149280.500.9.1558267190533; __utmc=30149280; __utmz=30149280.1558235896.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.16477'
    replay_comment = "up"
###### 如何获得你的cookie

首先登陆豆瓣，然后

https://jingyan.baidu.com/article/5d368d1ea6c6e33f60c057ef.html



#### 问题

验证码本质上还是个解决不了的问题，所以呢我是直接获取到验证码以后自己手动输入就行了。



#### 验证码规则

豆瓣的验证码基本上是半个小时一次，连续发贴只要超过三个基本就会弹验证码，所以这个其实不好用，手动自己刷贴也要来回写验证码贼麻烦

之前以为手机端不会被验证，后来发现手机端也会，无奈~



#### TODO

额，房子租出去了，不知道啥时候还会更新一下这个



原作者换了实现方式，总算给了代码，我基本就不再会更新了

https://github.com/gangfang/robo-commenter-for-douban

