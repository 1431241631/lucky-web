# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 14:50
# @Author  : #
# @File    : Web.py
# @Software: PyCharm
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import Spider_TX
import Spider_QIY
import Spider_UK
from Transform import transform

app = FastAPI()
# 配置跨域访问
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 搜索接口
@app.get("/api/search")
async def search(cls: str, data: str):
    if cls == 'tx':
        ret = await Spider_TX.get_search_list(data)
    elif cls == 'qiy':
        ret = await Spider_QIY.get_search_list(data)
    elif cls == 'uk':
        ret = await Spider_UK.get_search_list(data)
    return ret


# 获取视频
@app.get("/api/transformvideo")
async def transform_video(url: str, cls: str):
    ret = await transform(url)
    return ret


# 获取视频列表
@app.post("/api/playvideolist")
async def get_video_list(url: str = Form(...), cls: str = Form(...)):
    if cls == 'tx':
        ret = await Spider_TX.get_play_list(url)
    elif cls == 'qiy':
        ret = await Spider_QIY.get_play_list(url)
    elif cls == 'uk':
        ret = await Spider_UK.get_play_list(url)
    return ret


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
