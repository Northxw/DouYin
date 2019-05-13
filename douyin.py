# -*- coding:utf-8 -*-

import requests
import re
from lxml import etree
from save_mongo import get_task, save_user_info
import time
import random

def get_share_info(shareid):
    """个人主页信息"""
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    url = "https://www.iesdouyin.com/share/user/%s" % shareid
    res = requests.get(url, headers=headers).text
    # 加密-正常数字对照字典
    code_decode_nums =[
        {'codes': [' &#xe603; ', ' &#xe60d; ', ' &#xe616; '], 'decode': 0},
        {'codes': [' &#xe602; ', ' &#xe60e; ', ' &#xe618; '], 'decode': 1},
        {'codes': [' &#xe605; ', ' &#xe610; ', ' &#xe617; '], 'decode': 2},
        {'codes': [' &#xe604; ', ' &#xe611; ', ' &#xe61a; '], 'decode': 3},
        {'codes': [' &#xe606; ', ' &#xe60c; ', ' &#xe619; '], 'decode': 4},
        {'codes': [' &#xe607; ', ' &#xe60f; ', ' &#xe61b; '], 'decode': 5},
        {'codes': [' &#xe608; ', ' &#xe612; ', ' &#xe61f; '], 'decode': 6},
        {'codes': [' &#xe60a; ', ' &#xe613; ', ' &#xe61c; '], 'decode': 7},
        {'codes': [' &#xe60b; ', ' &#xe614; ', ' &#xe61d; '], 'decode': 8},
        {'codes': [' &#xe609; ', ' &#xe615; ', ' &#xe61e; '], 'decode': 9}
    ]
    # 替换加密数字
    for codes in code_decode_nums:
        for code in codes['codes']:
            res = re.sub(code, str(codes['decode']), res)
    html = etree.HTML(res)
    user_info = {}
    # 昵称
    user_info['nickname'] = re.search('class="nickname">(.*?)<', res, re.S).group(1)
    # 抖音ID
    id_str = ''.join(html.xpath("//p[@class='shortid']/text()")).replace("抖音ID：",'').strip()
    user_info['short_id'] = id_str + ''.join(html.xpath("//p[@class='shortid']/i/text()"))
    # 头像
    user_info['avatar'] = html.xpath('//*[@class="avatar"]/@src')[0]
    # 类型
    user_info['type'] = ''.join(html.xpath('//span[@class="info"]/text()'))
    # 签名
    user_info['signature'] = ''.join(html.xpath('//p[@class="signature"]/text()')).replace('\n', ' ').strip()
    # 关注
    user_info['focus'] = ''.join(html.xpath('//span[contains(@class, "focus")]/span/i/text()'))
    num_unit = ''.join(html.xpath('//span[contains(@class, "focus")]/span/text()'))
    if 'w' in num_unit:
        user_info['focus'] = str(int(user_info['focus']) / 10) + 'w'
    # 粉丝
    user_info['fans'] = ''.join(html.xpath('//span[contains(@class,"follower")]/span/i/text()'))
    num_unit = ''.join(html.xpath('//span[contains(@class,"follower")]/span/text()'))
    if 'w' in num_unit:
        user_info['fans'] = str(int(user_info['fans']) / 10) + 'w'
    # 获赞数
    user_info['likes_num'] = ''.join(html.xpath('//span[contains(@class, "liked-num")]/span/i/text()'))
    num_unit = ''.join(html.xpath('//span[contains(@class,"liked-num")]/span/text()'))
    if 'w' in num_unit:
        user_info['likes_num'] = str(int(user_info['likes_num']) / 10) + 'w'
    # 作品
    user_info['works'] = ''.join(html.xpath('//div[contains(@class, "user-tab")]/span/i/text()'))
    num_unit = ''.join(html.xpath('//div[contains(@class,"user-tab")]/span/text()'))
    if 'w' in num_unit:
        user_info['works'] = str(int(user_info['works']) / 10) + 'w'
    # 喜欢
    user_info['likes'] = ''.join(html.xpath('//div[contains(@class,"like-tab")]/span/i/text()'))
    num_unit = ''.join(html.xpath('//div[contains(@class,"like-tab")]/span/text()'))
    if 'w' in num_unit:
        user_info['likes'] = str(int(user_info['likes']) / 10) + 'w'

    print(user_info)
    return user_info


if __name__ == '__main__':
    # print(get_share_info('98564181541'))
    while True:
        task_id = get_task()
        if not task_id:
            break
        save_user_info(get_share_info(task_id))
        time.sleep(random.randint(0,1))
