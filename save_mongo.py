# -*- coding:utf-8 -*-

import pymongo
import os
from pymongo.collection import Collection

# client = pymongo.MongoClient(host='192.168.209.128', port=27017)
client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['douyin']
collection = Collection(db, 'taskid')
collection_user_info = Collection(db, 'userinfo')

def init_task():
    shareid = os.path.dirname(os.path.realpath(__file__)) + "\\utils\\shareid.txt"
    with open(shareid) as f:
        for shareid in f.readlines():
            task_id = {}
            task_id['share_id'] = shareid.replace('\n','')
            collection.insert_one(task_id)
            # print(task_id)

def save_task(task):
    try:
        collection.update({'share_id': task['share_id']}, task, True)
    except:
        pass
    # collection.update_one({'share_id': task['share_id']}, {'$set': {'share_id': task['share_id']}})

def get_task():
    """获取分享ID"""
    try:
        share_id = collection.find_one_and_delete({})['share_id']
        return share_id
    except:
        pass

def save_user_info(data):
    """存储用户信息"""
    try:
        collection_user_info.insert(data)
    except:
        pass

if __name__ == '__main__':
    init_task()
    # print(get_task())