# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 14:56
# @Author  : #
# @File    : Transform.py
# @Software: PyCharm
from ruia import Request
import base64
import time
import json


def str2base64(_str: str):
    return base64.b64encode(_str.encode('utf-8')).decode('utf-8')


async def transform(url: str):
    """
    把原视频链接进行解析获取免费播放的视频
    :param url:
    :return:
    """
    base_url = 'http://5.nmgbq.com/jx.php'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.190 Safari/537.36 "
        , "Content-Type": "application/x-www-form-urlencoded"}
    referer = str2base64(base_url + "?url=" + url)
    other = str2base64(url)
    ref = 0
    __time = int(time.time() * 1000)
    data = {"url": url, "referer": referer, "other": other, "ref": ref, "time": __time}
    res = await Request(url='http://5.nmgbq.com/2/api.php', method="POST", data=data, headers=headers).fetch()
    ret = await res.text()
    return json.loads(ret)
