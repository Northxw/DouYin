## DouYin

&emsp; 根据抖音用户名片分享链接构造抓取队列，多设备 (多进程) 抓取用户信息。



## 抓取流程

1.  appium 脚本打开抖音后进入某个用户的粉丝列表界面，不断向下滑动触发粉丝列表的请求接口
2.  mitmdump 脚本拦截请求，获取 shareid、shortid、nickname 字段并存储 (或更新) 至 MongoDB 数据库
3.  获取数据库中保存的 shareid 字段并构造抓取链接，请求用户主页获取信息并保存至 MongoDB



## 环境依赖

```shell
pip3 install -r requirements
```

&emsp; 注意：appium, mitmproxy 证书等配置请自行谷歌。



## 运行

1. 初始化数据库：读取 shareid.txt 数据到 mongodb，完成初始抓取链接（可选）

   ```shell
   python save_mongo.py
   ```

2.  抓取准备：开启多个 Appium 服务器，开启相应数量的安卓模拟器（开发者模式，USB调试），mitmdump监听端口，准备拦截

   ```shell
   mitmdump -s fans_info.py -p 8080
   ```

3.  拦截响应：运行 appium 自动化脚本触发粉丝列表页面的请求接口，mitmdump 拦截返回的 response 处理后保存至 MongoDB

   ```shell
   python actions.py
   ```

4.  获取数据：读取 MongoDB 对应集合的 shareid 字段，构造抓取链接，请求用户主页信息并保存至MongoDB

   ```shell
   python douyin.py
   ```

   

## 结果

![shareid](https://github.com/Northxw/DouYin/blob/master/utils/shareid.png)

![userinfo](https://github.com/Northxw/DouYin/blob/master/utils/userinfo.png)