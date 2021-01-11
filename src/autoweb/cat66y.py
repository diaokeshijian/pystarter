# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2021/1/11 14:37
# @Author  : eli
# @File    : cat66y.py
#
# 监控文本， 持续下载


import os
import time
import requests
downloaded_urls = []
monitored_url = []
root_path = "D:\\caty\\"
img_urls = []
counter = 0
daily_counter = 0;

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


def get_monitored_page_urls():
    monitored_page_urls_file = open('D:\\caty\\monitored_page_urls', 'r')
    monitored_page_urls = monitored_page_urls_file.readlines()
    for url in monitored_page_urls:
        if len(url) != 0:
            monitored_url.append(url.strip())
    monitored_page_urls_file.close()


def get_downloaded_urls():
    downloaded_urls_file = open('D:\\caty\\downloaded_page_urls', 'r')
    downloaded_urls_file_lines = downloaded_urls_file.readlines()
    for line in downloaded_urls_file_lines:
        line = line.strip()
        if len(line) != 0:
            downloaded_urls.append(line)
    downloaded_urls_file.close()


def download_page(link):
    response = requests.get(link, headers=headers)
    print(response.status_code)
    response.encoding = 'gbk'
    response_text = response.text
    title = response_text.split('<title>')[1].split('</title>')[0].replace('&nbsp;', '')
    if ' - 達蓋爾的旗幟 | 草榴社區 - t66y.com' or ' - 技術討論區 | 草榴社區 - t66y.com' in title:
        title = title.replace(' - 達蓋爾的旗幟 | 草榴社區 - t66y.com', '').replace(' - 技術討論區 | 草榴社區 - t66y.com', '')
    print('title : ' + title)

    response_text_in_lines = response_text.split(' ')

    for line in response_text_in_lines:
        # print(line)
        if 'ess-data' in line and 'function' not in line and 'this' not in line:
            # print(line)
            line_element = line.split("'")
            # print(line_element)
            img_urls.append(line_element[1])

    downloaded_image_file_path = root_path + title
    if not os.path.exists(downloaded_image_file_path):
        os.makedirs(downloaded_image_file_path)

    for img_url in img_urls:
        print(img_url)
        image_name = img_url.split('/')[-1]
        print('downloading ' + image_name)
        response_img = requests.get(img_url)
        response_img_content = response_img.content
        with open(downloaded_image_file_path + '\\' + image_name, 'wb') as imgfile:
            imgfile.write(response_img_content)
            imgfile.close()
            print(image_name + ' has been downloaded.')
            global counter
            counter = counter + 1
            print(str(counter) + ' of ' + str(len(img_urls)) + ' has been downloaded.')


def mark_url_as_downloaded(link):
    with open('D:\\caty\\downloaded_page_urls', 'a') as f:
        f.write(link)
        f.write('\n')


while True:
    get_monitored_page_urls()
    get_downloaded_urls()
    for url in monitored_url:
        if url not in downloaded_urls:
            download_page(url)
            mark_url_as_downloaded(url)
            daily_counter = daily_counter + counter
            counter = 0
            img_urls = []
            time.sleep(5)
        else:
            time.sleep(5)

