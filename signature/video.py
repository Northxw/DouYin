# -*- coding:utf-8 -*-


import json
import time
import requests
import re


share_id = '98524936524'
share_url = 'https://www.iesdouyin.com/share/user/%s' % share_id

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
}

response  = requests.get(url=share_url, headers=headers)

dytk = re.search("dytk:\s'(.*?)'", response.text, re.S).group(1)
tac = "var tac='" + re.search("tac='(.*?)'", response.text, re.S).group(1) + "';"

with open("html_head.txt") as f_head:
    head = f_head.read()

with open("html_foot.txt") as f_foot:
    foot = f_foot.read().replace("shareid", share_id)

with open("signature.html", "w") as f:
    f.write(head + '\n' + tac + '\n' + foot)

signature = input("秘钥：")
movie_url = "https://www.iesdouyin.com/web/api/v2/aweme/post/?user_id={}&count=21&max_cursor=0&aid=1128&_signature={}&dytk={}".format(
                share_id, signature, dytk)
print(movie_url)

# while True:
#     movie_response = requests.get(url=movie_url, headers=headers)
#     if not json.loads(movie_response.text)['aweme_list']:
#         time.sleep(1)
#         continue
#     else:
#         print(movie_response.text)
#         break
