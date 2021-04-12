# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 9:47
# @Author  : #
# @File    : Spider_TX.py
# @Software: PyCharm
import asyncio
from ruia import Item, TextField, AttrField, Request
import json
import hashlib
import aiohttp
from urllib import parse


def MD5(m_str: str):
    m = hashlib.md5()
    b = m_str.encode('utf-8')
    m.update(b)
    return m.hexdigest()


class UKSearchItem(Item):
    target_item = TextField(css_select="div[data-spm=PhoneSokuThreeProgram_4] > div.pack-cover_1K0Xq")
    title = AttrField(css_select='a.pack-top_2nSnm', attr='data-trackinfo')
    url = AttrField(css_select='a.pack-top_2nSnm', attr='href')
    img = AttrField(css_select='a.pack-top_2nSnm', attr='style')


async def get_search_list(url: str):
    items = UKSearchItem.get_items(url='https://so.youku.com/search_video/q_' + url,
                                   cookies={"cna": "gNgBGK3cfCsCAXsFjUTM0GAy"})
    data = []
    async for item in items:
        title = json.loads(item.title)['object_title']
        img = item.img[item.img.find('background-image:url(') + len('background-image:url('):item.img.rfind(')"')]
        data.append(
            {'title': title, 'url': "https:" + item.url, 'img': img})
    return data


async def get_play_list(url: str):
    async with aiohttp.ClientSession() as session:
        res = await Request(
            'https://acs.youku.com/h5/mtop.youku.columbus.gateway.new.execute/1.0/?jsv=2.6.1&appKey=24679788',
            request_session=session).fetch()
    cookies = res.cookies
    token = cookies.get('_m_h5_tk')
    token = token.split('_')[0]
    show_id = url[url.find('id_') + len('id_'):url.find('.html')]
    data = r'{"ms_codes":"2019030100","params":"{\"biz\":true,\"scene\":\"component\",\"componentVersion\":\"3\",' \
           r'\"ip\":\"223.88.179.25\",\"debug\":0,\"utdid\":\"IwAoGKx9jmACAd9Ys8JZhiqg\",\"userId\":\"\",' \
           r'\"platform\":\"pc\",\"nextSession\":\"{\\\"componentIndex\\\":\\\"3\\\",' \
           r'\\\"componentId\\\":\\\"61518\\\",\\\"level\\\":\\\"2\\\",\\\"itemPageNo\\\":\\\"0\\\",' \
           r'\\\"lastItemIndex\\\":\\\"0\\\",\\\"pageKey\\\":\\\"LOGICSHOW_LOGICTV_DEFAULT\\\",' \
           r'\\\"group\\\":\\\"0\\\",\\\"itemStartStage\\\":1,\\\"itemEndStage\\\":120}\",' \
           r'\"videoId\":\"\",\"showId\":\"' + show_id + r'\"}","system_info":"{\"os\":\"pc\",' \
                                                         r'\"device\":\"pc\",\"ver\":\"1.0.0\",\"appPackageKey\":\"pcweb\",\"appPackageId\":\"pcweb\"}"}'
    sign = MD5(token + '&1618112499454' + "&24679788&" + data)
    print(sign)
    async with aiohttp.ClientSession() as session:
        request = Request(
            f'https://acs.youku.com/h5/mtop.youku.columbus.gateway.new.execute/1.0/?jsv=2.6.1&appKey=24679788&t'
            f'=1618112499454&sign={sign}&api=mtop.youku.columbus.gateway.new.execute&type=originaljson&v=1.0&ecode=1'
            f'&dataType=json&data={data}', cookies=cookies, request_session=session)
        res = await request.fetch()
        ret = await res.json()
    ret_data = []
    for item in ret['data']['2019030100']['data']['nodes']:
        item_data = item['data']
        title = item_data['title']
        url = item_data['action']['value']
        ret_data.append(
            {'mark': '', 'play_item': title, 'url': f'https://v.youku.com/v_show/id_{url}.html', 'title': ''})
    return ret_data


if __name__ == '__main__':
    asyncio.run(get_play_list('https://v.youku.com/v_nextstage/id_fbda851de7c841ce8d16.html'))
