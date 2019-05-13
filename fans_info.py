# -*- coding:utf-8 -*-

from mitmproxy import ctx
from save_mongo import save_task
import json

def response(flow):
    """获取粉丝数据"""
    url = "aweme/v1/user/follower/list/"
    if  url in flow.request.url:
        data = json.loads(flow.response.text)
        # info = ctx.log.info
        followers = data['followers']
        for follower in followers:
            user = {}
            user['short_id'] = follower.get('short_id')
            user['share_id'] = follower.get('uid')
            user['nickanem'] = follower.get('nickname')
            save_task(user)
            print(user)
