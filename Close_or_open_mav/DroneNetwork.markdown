---
layout:     post
title:      "无人机网络"
subtitle:   "无人机网络"
date:       2019-03-28
author:     "elmagnifico"
header-img: "img/git-head-bg.jpg"
catalog:    true
tags:
    - AP
    - H3C
---
# 网络规划

飞机使用dhcp配置，自动上线，上线以后飞机本身有一个id，这个id可以重复，但是每次飞行时必须是无重复id，然后可以通过点灯区分同id

ssid不再需要改，全部进入同一个ssid，每个AP有上限，会自动踢出信号强度弱的。

其他的会自动连接进入到其他AP中

飞机状态使用轮询的方式来处理，每0.1s查询一架或者多架？

标准是1000架次时，每10s可以更新一次所有飞机状态 = 0.1s更新10架飞机状态

在触发失联等异常状态时，恢复心跳自动发送，用于确认位置

不漫游的原因是？

普通漫游是由终端发起的，unifi可以用最小信号强度来踢出弱信号的人。

无缝漫游是靠AP完成的，而且必须是相同信道，放置位置非常合适，不适合高密度部署

![SMMS](https://i.loli.net/2019/04/01/5ca1c116363b2.png)

NBIOT，LoRaWAN 都不可行，通信频率达不到

#### 2.4g 不干扰的频段

![SMMS](https://i.loli.net/2019/04/01/5ca1c2365f697.png)

最好使用1 6 11，蜂窝状排布，这个是使用20MHZ带宽的情况下，其他情况干扰更严重

![SMMS](https://i.loli.net/2019/04/01/5ca1c2e95773f.png)

#### 5.8g 不干扰频段

![SMMS](https://i.loli.net/2019/04/01/5ca1c46d38904.png)

使用 149，157，165，153，161，使用20MHZ的带宽的情况下

![SMMS](https://i.loli.net/2019/04/01/5ca1c9e41ad0d.png)

带宽小的情况下，会导致总带宽下降，总速率下降。

## 测试

开了隔离以后一架一架往上加，看能加到多少。

## 无人机网卡

目前使用的是：RTL8812au

802.11AC/ABGN USB WLAN NETWORK CONTROLLER

> General Description
> The Realtek RTL8812AU-CG is a highly integrated single-chip that supports 2-stream 802.11ac solutions with a Wireless LAN (WLAN) USB interface controller. It combines a WLAN MAC, a 2T2R capable WLAN baseband, and RF in a single chip. The RTL8812AU-CG provides a complete solution for a high-performance integrated wireless device.
> Features
> General
> QFN-76 package
> 802.11ac/abgn
> 802.11ac 2x2
> Host interface
> USB3.0 for WLAN controller
> Applications
> The product is applicable for Drone application


## 网络包的情况

广播包
- 起飞解锁？


单播包
- 航点


组播包
- ？？？

## 设备

#### 当前设备

UniFi Outdoor5
理论带机量200+
目前实际带机量80
理论范围183m
走的协议是802.11n 最大只有300Mbps，而且由于是802.11n根本利用不起来802.11ac协议


UAP‑AP‑SHD
理论带机量500+
目前实际带机量200+

#### 带机量

并发带机量具体计算公式如下：
转发性能（换算成与终端设备预留带宽相同单位）* 84 * 8 / 预留给终端设备的带宽=并发带机量；

我们一般预留给终端的带宽是2M-4M

转发性能是指一秒能转发多少个数据帧。与该数据帧大小无关。但是，该数据帧越大。里面的信息量也越多，因此，在这个计算公式中，我们按照每个数据帧都只有84位来计算，是以最坏的情况来考虑的。

故而，当你在为客户进行方案的设计时，你可以对路由器进行更加优质的选择。

带业务转发性能则是指：计划分给每个客户的宽带*实际并发带机量。

#### 错峰

错开所有飞机的心跳时间，保持整个无线连接时信道上的碰撞 CSMA/CS 是最好的状态

#### 新设备

![SMMS](https://i.loli.net/2019/03/28/5c9c9283d23d8.png)

UniFi AP XG 5400税后 号称1500 实际750左右
UniFi WiFi BaseStation XG 无货 无报价  1500刀，只能从国外买

锐捷网络
http://www.ruijie.com.cn/fa/jzhdch/20180525/

aruba无线
http://www.quatec.com.cn/product/product.php?class2=5

鲲鹏无限
https://www.nradiowifi.com/

华为 AP8082DN&AP8182DN
https://e.huawei.com/cn/related-page/products/enterprise-network/wlan/outdoor-access-points/ap8082dn-ap8182dn/brochure/wlan-ap8082dn-ap8182dn


## 参考
