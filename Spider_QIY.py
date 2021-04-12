# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 9:47
# @Author  : #
# @File    : Spider_TX.py
# @Software: PyCharm
import asyncio
from ruia import Item, TextField, AttrField, Request
import aiohttp


class QIYPlayItem(Item):
    target_item = TextField(css_select='ul.site-piclist > li[data-albumlist-elem]')
    playItem = AttrField(xpath_select='.', attr='data-order')
    url = AttrField(css_select='a', attr='href', default="")
    title = AttrField(css_select='a', attr='title', default="")


async def get_search_list(name: str):
    # 关于为什么这里这么多参数,就自己动手抓包分析一下
    async with aiohttp.ClientSession() as session:
        request = Request(url='https://pcw-api.iqiyi.com/graphql', request_session=session, method="POST", data={
            "query": 'query { MMSoResult ( from: "pcw-ssr" if: "video" need_condense: 0 key: "' + name + '" pageNum: 1 '
                                                                                                         'pageSize: '
                                                                                                         '20 duration_level: 0 need_qc: 0 channel_name: "" site_publish_date_level: "" site: "iqiyi" mode: 1 '
                                                                                                         'bitrate: "" data_type: "6;mustnot" intent_category_type: 1 no_play_control: 0 ip: "" u: "" pu: "" '
                                                                                                         'p1: "101" ) { searchO { code result_num qc need_qc isreplaced event_id bkt terms search_time '
                                                                                                         'real_query intent_pos intent_type intent_result_num intent_action_type scoring_mode index_layer '
                                                                                                         'term_query { term field_name } graph_type { type intent_sub_type intent_action_type graph_sub_type '
                                                                                                         '} super_serial { serial_info { serial_doc_id super_album_name } } graph_categories { desc field '
                                                                                                         'field_name value hit } intent_graph_docinfos { __typename ...on SearchCardGraphT1 { name docid '
                                                                                                         'docinfo { description albumImg(size: "_128_128") starinfos { qipu_id starName } } entity_properties '
                                                                                                         '{ property_value } } ...on SearchCardGraphT2 { name docid docinfo { g_img(size: "_260_360") '
                                                                                                         'g_img2x(size: "_260_360") g_main_link videoDocType series siteId video_lib_meta { entity_id '
                                                                                                         'description } } entity_properties { property_value } } ...on SearchCardGraphT8 { name docid docinfo '
                                                                                                         '{ g_img(size: "_260_360") g_img2x(size: "_260_360") g_main_link videoDocType series siteId '
                                                                                                         'video_lib_meta { entity_id description } } child_nodes { docid docinfo { albumTitle starinfos { '
                                                                                                         'qipu_id } } } } ...on SearchCardGraphT3 { docid docinfo { videoDocType siteId g_year } child_nodes '
                                                                                                         '{ docid docinfo { g_img(size: "_128_128") g_img2x(size: "_128_128") g_main_link g_title } '
                                                                                                         'properties { name } } } ...on SearchCardGraphT5 { docid docinfo { g_img(size: "_128_128") g_img2x('
                                                                                                         'size: "_128_128") g_main_link g_title } description child_nodes { docid relation docinfo { g_img('
                                                                                                         'size: "_128_128") g_img2x(size: "_128_128") g_main_link g_title } child_nodes { docid relation '
                                                                                                         'docinfo { g_img(size: "_128_128") g_img2x(size: "_128_128") g_main_link g_title } } } } ...on '
                                                                                                         'SearchCardGraphT7 { docid child_nodes { docid docinfo { g_img(size: "_128_128") g_img2x(size: '
                                                                                                         '"_128_128") g_main_link g_title } properties { docinfo { g_title g_main_link } } } } } docinfos { '
                                                                                                         '__typename doc_id score pos sort is_from_intent albumDocInfo { videoDocType album_type channel '
                                                                                                         'siteId siteName qipu_id tag g_id g_rec_word_id g_title g_main_link g_black_region } ...on '
                                                                                                         'SearchIntentStar { albumDocInfo { g_img(size: "_128_128") g_img2x(size: "_128_128") videoinfos('
                                                                                                         'size: 1) { itemTitle, itemLink } } } ...on SearchIntentTagVideo { albumDocInfo { g_img(size: '
                                                                                                         '"_180_101") g_img2x(size: "_180_101") g_meta albumId } } ...on SearchIntentTagLive { albumDocInfo { '
                                                                                                         'g_img(size: "_180_101") g_img2x(size: "_180_101") g_corner_mark albumId live_room { '
                                                                                                         'presenter_nickname } } } ...on SearchIntentTagRole { albumDocInfo { g_img_link g_img(size: '
                                                                                                         '"_180_236") g_img2x(size: "_180_236") g_focus g_meta g_corner_mark albumId score star '
                                                                                                         'video_lib_meta { actor { id name } } live_room { presenter_nickname } } } ...on SearchCardVariety { '
                                                                                                         'albumDocInfo { g_img(size: "_260_360") g_img2x(size: "_260_360") g_corner_mark g_desc g_year '
                                                                                                         'g_update_strategy g_rec_word_id qipu_id super_album_order director star video_lib_meta { entity_id '
                                                                                                         'director { id name } host { id name } } super_show_cluster(size: 7) { super_show_cluster_info { '
                                                                                                         'site_id site_name cluster_tag album_url video_info { itemTitle itemLink year is_vip } '
                                                                                                         'site_data_doc_info { siteId siteName docid } } } clusterinfos { siteId siteName docid } videoinfos '
                                                                                                         '{ year itemTitle subTitle itemshortTitle itemLink is_vip g_corner_mark_s qipu_id timeLength } } } '
                                                                                                         '...on SearchCardEpisodeMuti { albumDocInfo { g_img(size: "_260_360") g_img2x(size: "_260_360") '
                                                                                                         'g_meta g_corner_mark g_year g_update_strategy g_desc qipu_id super_album_order albumAlias score '
                                                                                                         'director star video_lib_meta { entity_id director { id name } actor { id name } } clusterinfos { '
                                                                                                         'siteId siteName docid } videoinfos { g_corner_mark_s itemNumber itemTitle itemLink is_vip qipu_id '
                                                                                                         'timeLength } customize_related_content { g_corner_mark_s customize_related_content_type_name '
                                                                                                         'itemNumber itemTitle itemLink qipu_id } prevues { g_corner_mark_s itemNumber itemLink qipu_id '
                                                                                                         'timeLength } vip_unlock_video { g_corner_mark_s itemNumber itemLink qipu_id timeLength } } } ...on '
                                                                                                         'SearchCardSingleVideo { albumDocInfo { g_img(size: "_180_101") g_img2x(size: "_180_101") g_meta '
                                                                                                         'g_corner_mark g_update_strategy g_release_time(splitor: "-") g_desc qipu_id super_album_order '
                                                                                                         'source_type uploader_auth_mark threeCategory videoinfos { uploader_id uploader_name is_vip qipu_id '
                                                                                                         'timeLength } } } ...on SearchCardSerialEmpty { albumDocInfo { g_img(size: "_180_236") g_img2x(size: '
                                                                                                         '"_180_236") g_update_strategy g_release_time g_year g_last_days g_desc g_region super_album_order '
                                                                                                         'threeCategory director star video_lib_meta { entity_id category duration director { id name } actor '
                                                                                                         '{ id name } } prevues { itemLink qipu_id timeLength } related_videos { itemLink qipu_id timeLength '
                                                                                                         '} } } ...on SearchCardTopic { albumDocInfo { g_img g_img2x g_corner_mark g_update_strategy g_desc '
                                                                                                         'albumLink director star video_lib_meta { entity_id } } } ...on SearchCardMovie { albumDocInfo { '
                                                                                                         'g_img(size: "_260_360") g_img2x(size: "_260_360") g_img_link g_meta g_corner_mark g_release_time '
                                                                                                         'g_update_strategy g_year g_desc g_region super_album_order albumAlias is_third_party_vip score '
                                                                                                         'director star video_lib_meta { entity_id director { id name } actor { id name } } clusterinfos { '
                                                                                                         'siteId siteName docid } } } ...on SearchCardStar { albumDocInfo { g_img(size: "_128_128") g_img2x('
                                                                                                         'size: "_128_128") g_desc starinfos { qipu_id alias_name star_english_name occupation height '
                                                                                                         'starBirth star_region } recommendation { g_meta_s itemTitle itemLink itemVImage subChannel '
                                                                                                         'role_info { role character } qipu_id timeLength } videoinfos { g_meta_s itemTitle itemLink '
                                                                                                         'itemVImage subChannel role_info { role character } qipu_id timeLength } } } ...on SearchCardBodan { '
                                                                                                         'albumDocInfo { g_img(size: "_260_360") g_img2x(size: "_260_360") g_img_link g_meta g_corner_mark '
                                                                                                         'g_release_time g_desc source_type collection_type effective_start_time effective_end_time '
                                                                                                         'uploader_auth_mark videoinfos { g_meta_s itemTitle subTitle itemshortTitle itemLink itemHImage '
                                                                                                         'initialIssueTime threeCategory is_vip qipu_id timeLength } clusterinfos { siteId siteName docid } } '
                                                                                                         '} ...on SearchCardUgcVerified { albumDocInfo { g_img g_img2x g_desc verified_user_infos { user_id '
                                                                                                         'qipu_id followed_count video_count auth_mark is_verified self_media_content_rating } videoinfos { '
                                                                                                         'g_meta_s itemTitle itemHImage itemLink initialIssueTime qipu_id timeLength } } } ...on '
                                                                                                         'SearchCardBlank { albumDocInfo { g_img(size: "_180_236") g_img2x(size: "_180_236") g_img_link '
                                                                                                         'g_desc g_corner_mark g_update_strategy g_release_time g_last_days g_year g_region albumAlias '
                                                                                                         'albumEnglishTitle star video_lib_meta { entity_id director { id name } actor { id name } category } '
                                                                                                         'prevues { itemTitle timeLength itemHImage itemLink qipu_id } related_videos { itemTitle timeLength '
                                                                                                         'itemHImage itemLink qipu_id } music_videos { itemTitle timeLength itemHImage itemLink qipu_id } } } '
                                                                                                         '...on SearchCardBook { albumDocInfo { g_img(size: "_260_360") g_img2x(size: "_260_360") g_desc book '
                                                                                                         '{ author three_category } biz { button_text } } } ...on SearchCardGame { albumDocInfo { g_img '
                                                                                                         'g_img2x g_desc g_corner_mark app { running_platform } } } ...on SearchCardTvStation { albumDocInfo '
                                                                                                         '{ g_img g_img2x g_desc g_corner_mark g_display_mark live_group { live_channel { qipu_id live_type '
                                                                                                         'father_live_channel_id live_status live_video { qipu_id title start_play_time stop_play_time } } } '
                                                                                                         '} } ...on SearchCardGameRoom { albumDocInfo { g_img g_img2x g_desc live_room { presenter_nickname } '
                                                                                                         '} } ... on SearchCardAdvertise { albumDocInfo { g_desc g_img g_img2x videoinfos(size: 1) { '
                                                                                                         'itemTitle itemLink initialIssueTime } } } } } hotQuery: searchMHotQueryNew(hot_query_type: 1, '
                                                                                                         'pagesize: 5) { hot_query_info { query } } relateQuery: searchMRelatedQuery(key: "' + name + '") '
                                                                                                                                                                                                      'starGraph: '
                                                                                                                                                                                                      'qipuGetRelatedCelebrities{ self_info{ name entity_id imageformat_iqiyi_people } related_celebrity { '
                                                                                                                                                                                                      'name entity_id imageformat_iqiyi_people relationship } } starList: '
                                                                                                                                                                                                      'qipuGetRelatedCelebritiesOfVideo{ name entity_id imageformat_iqiyi_people } relateVideo: '
                                                                                                                                                                                                      'qiyuPortalResys30 { id name display_fields{ picture_url } } hotRank: searchMHotQueryNew { name '
                                                                                                                                                                                                      'hot_query_info { query search_trend } } } }'})
        res = await request.fetch()
        data = await res.json()
    ret = []
    data_list = data['data']['MMSoResult']['searchO']['docinfos']
    for i in data_list:
        if i['__typename'] == 'SearchCardEpisodeMuti' or i['__typename'] == 'SearchCardMovie':
            video = i['albumDocInfo']
            ret.append({'title': video['g_title'], 'url': "https:" + video['g_main_link'],
                        'img': "https:" + video['g_img']})
    return ret


async def get_play_list(url: str):
    items = QIYPlayItem.get_items(url=url)
    data = []
    async for item in items:
        data.append({'mark': '', 'url': 'https:' + item.url,
                     'play_item': item.playItem.replace(' ', '').replace('\n', ''), 'title': item.title})
    return data
