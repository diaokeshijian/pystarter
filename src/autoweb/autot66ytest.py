import requests

img_urls = []
counter = 0
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gbk, utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'host': 't66y.com',
    'Referer': 'https://t66y.com/',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
}


def get_title(response_content):
    content = response_content.split('title')
    print(content)


response = requests.get('https://t66y.com/htm_data/2009/16/4089558.html', headers=headers)
print(response.status_code)
response.encoding = 'gbk'
response_text = response.text
title = response_text.split('<title>')[1].split('</title>')[0].replace('&nbsp;', '')
if ' - 達蓋爾的旗幟 | 草榴社區 - t66y.com' in title:
    title = title.replace(' - 達蓋爾的旗幟 | 草榴社區 - t66y.com', '')
print(title)



