# _*_ coding:utf-8 _*_
#
# @Version : 1.0
# @Time    : 2021/1/11 14:37
# @Author  : eli
# @File    : cat66y.py
#
# 监控文本， 持续下载


import os
import threading
import time
from http.client import RemoteDisconnected
from requests.exceptions import ConnectionError
from requests.exceptions import ChunkedEncodingError

import requests
from urllib3.exceptions import ProtocolError

downloaded_urls = []
monitored_url = []
root_path = "D:\\caty\\"
img_urls = []
counter = 0
daily_counter = 0
thread_counter = 0

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gbk, utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection': 'keep-alive',
    'host': 't66y.com',
    'Referer': 'https://t66y.com/',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW 64) AppleWebKit/537.36 '
                  '(HTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360SE'
}


def get_monitored_page_urls():
    monitored_page_urls_file = open('D:\\caty\\monitored_page_urls', 'r')
    monitored_page_urls = monitored_page_urls_file.readlines()
    for page_url in monitored_page_urls:
        if len(page_url) != 0:
            monitored_url.append(page_url.strip())
    monitored_page_urls_file.close()


def get_downloaded_urls():
    downloaded_urls_file = open('D:\\caty\\downloaded_page_urls', 'r')
    downloaded_urls_file_lines = downloaded_urls_file.readlines()
    for line in downloaded_urls_file_lines:
        line = line.strip()
        if len(line) != 0:
            downloaded_urls.append(line)
    downloaded_urls_file.close()


def download_img(img_url, file_path):
    print(img_url)
    image_name = img_url.split('/')[-1]
    print('downloading ' + image_name)
    response_img_content = b''
    try:
        response_img = requests.get(img_url)
        response_img_content = response_img.content
    except RemoteDisconnected:
        print('failed to download url: ' + img_url)
        print('http.client.RemoteDisconnected: Remote end closed connection without response')
    except ConnectionError:
        print('failed to download url: ' + img_url)
        print('Connection aborted. Remote end closed connection without response')
    except ProtocolError:
        print('Remote end closed connection without response')
    except ChunkedEncodingError:
        print('An existing connection was forcibly closed by the remote host, , None, 10054, None')
    if len(response_img_content) != 0:
        with open(file_path + '\\' + image_name, 'wb') as imgfile:
            imgfile.write(response_img_content)
            imgfile.close()
            print(image_name + ' has been downloaded.')
            global counter
            counter = counter + 1
            global daily_counter
            daily_counter = daily_counter + 1
            print(str(counter) + ' of ' + str(len(img_urls)) + ' has been downloaded.')
            print(str(daily_counter) + ' have been downloaded in this session today.')


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
    threads = []
    for img_url in img_urls:
        t = threading.Thread(target=download_img, args=(img_url, downloaded_image_file_path))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join(120)

#        global thread_counter
#        while thread_counter < 5:
#            threading.Thread(target=download_img, args=(img_url, downloaded_image_file_path)).start()
#            thread_counter = thread_counter + 1


def mark_url_as_downloaded(link):
    with open('D:\\caty\\downloaded_page_urls', 'a') as f:
        f.write(link)
        f.write('\n')


def download_img_in_url(page_url):
    print('扫描到下载任务， 即将开始下载...')
    print('开始下载链接：  ' + page_url)
    download_page(url)
    mark_url_as_downloaded(url)
    global daily_counter
    global counter
    global img_urls
    daily_counter = daily_counter + counter
    counter = 0
    img_urls = []
    time.sleep(5)
    print('当前页面下载完成，即将扫描监控文本，检测下载任务...')


while True:
    monitored_url = []
    downloaded_urls = []
    get_monitored_page_urls()
    get_downloaded_urls()
    for url in monitored_url:
        if url not in downloaded_urls:
            download_img_in_url(url)
    print('当前无下载任务，30秒后重新扫描监控文本...')
    time.sleep(30)
