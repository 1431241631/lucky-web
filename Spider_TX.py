# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 9:47
# @Author  : #
# @File    : Spider_TX.py
# @Software: PyCharm
import asyncio
from ruia import Item, TextField, AttrField


# 搜索页面的爬虫
class TXSearchItem(Item):
    target_item = TextField(css_select='div._infos')
    title = TextField(css_select='a[_stat]')
    url = AttrField(css_select='a[_stat]', attr='href')
    img = AttrField(css_select='img.figure_pic', attr='src')


# 播放页面的爬虫
class TXPlayItem(Item):
    target_item = TextField(css_select='span.item')
    mark = AttrField(css_select='i.mark_v > img', attr='src')
    url = AttrField(css_select='a', attr='href')
    playItem = TextField(css_select='a')


async def get_search_list(url: str):
    items = TXSearchItem.get_items(url='https://v.qq.com/x/search/?q=' + url)
    data = []
    async for item in items:
        data.append(
            {'title': item.title.replace('\n', '').replace('\t', ''), 'url': item.url, 'img': item.img})
    return data


async def get_play_list(url: str):
    items = TXPlayItem.get_items(url=url)
    data = []
    async for item in items:
        data.append({'mark': item.mark, 'url': 'https://v.qq.com' + item.url,
                     'play_item': item.playItem.replace(' ', '').replace('\n', ''), 'title': ''})
    return data
