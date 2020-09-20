import os

import requests

article_urls = []
img_urls = []
counter = 0
root_path = 'C:\\Users\\Eli\\Desktop\\test\\'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gbk, utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'host': 't66y.com',
    'Referer': 'https://t66y.com/',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
}
response = requests.get('https://t66y.com/thread0806.php?fid=16', headers=headers)
print(response.status_code)

response.encoding = 'gbk'
response_text = response.text
# print(response_text)

response_text_in_lines = response_text.split('h3>')
for line in response_text_in_lines:
    if 'target="_blank"' in line and 'stylesheet' not in line and '永久域名' not in line and 'color=blue' not in line\
            and 'color=red' not in line and 'color=orange' not in line:
        article_url = line.split('"')[1]
        print('https://t66y.com/' + article_url)

