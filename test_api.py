# -*- coding:utf-8 -*-
# Author : chen
# Data : 2020/2/7 11:50 下午
# coding:utf-8

from locust import HttpLocust, TaskSet
import random
import time
import threading
test_time = time.strftime ("%Y%m%d%H%M%S", time.localtime ())
ran = str(random.randint(1,6))
orderNo="customer132xxxxxxxx"+test_time+str(random.randint(1,999999))

import requests
def test_func():
    #  ip：端口/接口路径
    url = "http://10.xx.xx.xxx:8086/gateway/customer2terminal/update-order"
    #  请求参数
    data = {
    "requestBody": {
        "data": {
            "deviceId": "XJZD666",
            "orderDetailList": [
                {
                    "count": ran,
                    "type": ran
                },
                {
                    "count": ran,
                    "type": ran
                }
            ],
            "orderNo": orderNo,
            "orderTime": test_time,
            "phone": "132xxxxxxxx"
        }
    },
    "requestHead": {
        "appId": "snuyw7x9yg8",
        "appVersion": "hhi6rabzjb",
        "channel": 1,
        "configVersion": "oa167gp4j5i",
        "deviceId": "8nxhucds21d",
        "ostype": "ANDROID",
        "sign": "8ay817nqmco6",
        "systemVersion": "7zgjf5uqve8",
        "token": "a1k6s55xia0m",
        "validateTime": test_time
    }
}

    response1 = requests.post (url, json=data)
    # print data
    # print random1
    print (response1.text)

# class UserBehavior (TaskSet):
#     # tasks = {test_func: 2}
#     tasks = test_func ()
#
#     #
#     def on_start(self):
#         test_func (self)

if __name__ == "__main__":
   # 创建数组存放线程
    threads = []
    # 创建10个线程
    for i in range (10):
        # 针对函数创建线程

        t = threading.Thread (target=test_func, args=())
        # 把创建的线程加入线程组
        threads.append (t)

    # 启动线程（记法一）
    # for t in threads:
    #     t.setDaemon (True)
    #     t.start ()
    #     t.join ()
    # 启动线程（记法二）
    for i in threads:
        i.start ()
        # keep thread
    for i in threads:
        i.join ()