#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path
import time

import qqbot
from qqbot.core.util.yaml_util import YamlUtil

test_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))


async def _at_message_handler(event, message: qqbot.Message):
    """
    定义事件回调的处理

    :param event: 事件类型
    :param message: 事件对象（如监听消息是Message对象）
    """
    msg_api = qqbot.AsyncDmsAPI(t_token, False)
    mAPI = qqbot.AsyncMessageAPI(t_token, False)
    # 打印返回信息
    qqbot.logger.info("event %s" % event + ",receive message %s" % message.content)

    # 输入/xxx后的处理
    if "/启动" in message.content:
        message_to_send = qqbot.MessageSendRequest("已启动群与频道消息同步", message.id)
        await mAPI.post_message(message.channel_id, message_to_send)

    elif "/停止" in message.content:
        message_to_send = qqbot.MessageSendRequest("已停止群与频道消息同步", message.id)
        await mAPI.post_message(message.channel_id, message_to_send)


if __name__ == "__main__":
    t_token = qqbot.Token(test_config["token"]["appid"], test_config["token"]["token"])

    # 注册机器人被@后的事件
    qqbot_handler = qqbot.Handler(
        qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, _at_message_handler
    )
    qqbot.async_listen_events(t_token, False, qqbot_handler)

    # init UserAPI
    uAPI = qqbot.UserAPI(t_token, False)

    # get bot info
    print(uAPI.me().__dict__)

    app_group_ids = []
    # get group info
    print(len(uAPI.me_guilds()))
    guilds = uAPI.me_guilds()
    for i in range(len(guilds)):
        group_info = guilds[i]
        print(group_info.__dict__)
        app_group_ids.append(group_info.id)

    # get group details
    for id in app_group_ids:
        gAPI = qqbot.GuildAPI(t_token, False)
        print(gAPI.get_guild(id).__dict__)

        # get child channel info
        cAPI = qqbot.ChannelAPI(t_token, False)
        channels = cAPI.get_channels(id)
        for i in range(len(channels)):
            print(channels[i].__dict__)

    # mAPI = qqbot.MessageAPI(t_token, False)
    # for i in range(100):
    #     # content max len is 10KB,but limit post times per day or per second
    #     content = "消息测试：" + str(i)
    #     message_id = "088de19cbeb883e7e97110a2e39c0138d401"
    #     send = qqbot.MessageSendRequest(content, message_id)
    #     mAPI.post_message("3315041", send)
    #     time.sleep(1)
