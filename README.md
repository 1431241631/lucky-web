# lucky-web
一个爬虫+web项目  
爬取TX视频，qiy,uk的搜索功能和视频列表并向外提供接口和解析视频
# 项目演示
[lucky_app](https://github.com/1431241631/lucky_app)
# 项目依赖
[aiohttp](https://docs.aiohttp.org/)  
[fastapi](https://fastapi.tiangolo.com/)  
[ruia](https://github.com/howie6879/ruia/)  
# 项目结构
## Web
简单的接口设计  
1、搜索接口  
2、获取搜索内容视频列表接口  
3、解析视频接口  
## Spider
Spider_xxx为爬虫代码  
使用 `ruia` 框架的几个模块进行爬虫  
## Transform
视频解析功能  
从百度随便爬一个就行  
# 关于项目
## 怎么跑起来
`pip install -r requirements.txt`   
python环境：`python3.8`  
安装完依赖后运行`Web.py`即可  
## 项目完善
项目中很多地方都很粗糙，可以跟据自己的需求进行完善  
比如response我是直接使用字典进行返回的，可以根据自己需求封装成实体类  
或者爬虫使用ruia的Spider类来完成 
# lucky_app前端界面
[lucky_app](https://github.com/1431241631/lucky_app)
# 最后
项目仅是为了学习和练习使用，请勿商业  
