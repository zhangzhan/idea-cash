# -*- coding: utf-8 -*-

import sys
import binascii

sys.path.append("./APNSWrapper")

from utils.APNSWrapper.notifications import APNSNotification, APNSNotificationWrapper
__author__ = 'zhangzhan'


deviceToken = binascii.unhexlify("c0eb6a1c0312690c66b16e304c75a9c2e6ff27dfa7c2930503e4836af9cb0188")

if __name__ == "__main__":
    #创建通知对象
    notification = APNSNotification()
    notification.token(deviceToken)
    notification.alert("alert")
    notification.badge(5)
    notification.sound()

    #创建发送通知的这个wrapper
    pem_cert_name = "MyCert.pem"
    wrapper = APNSNotificationWrapper(pem_cert_name, True, False, True)
    wrapper.append(notification)
    wrapper.notify()