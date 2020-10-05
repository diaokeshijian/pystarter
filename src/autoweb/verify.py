import requests

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
index_urls = []
article_urls = []
counter = 0
root_path = 'C:\\temp\\image_downloader\\'
image_directory = "C:\\temp\\image_downloader\\downloaded_images\\"
config_directory = "C:\\temp\\image_downloader\\config\\"


def main():
    get_index_urls()
    get_article_urls()
    print(article_urls)


def get_index_urls():
    index_file = open(config_directory + 'index_url.txt', 'r')
    for line in index_file:
        line = line.replace('\r\n', '').replace('\n', '')
        if len(line) > 0:
            index_urls.append(line)


def get_article_urls():
    for index_url in index_urls:
        response = requests.get(index_url, headers=headers)
        response.encoding = 'gbk'
        response_text = response.text
        response_text_in_lines = response_text.split('h3>')
        for line in response_text_in_lines:
            if 'target="_blank"' in line and 'stylesheet' not in line and '永久域名' not in line and 'color=blue' not in line \
                    and 'color=red' not in line and 'color=orange' not in line:
                article_url_short = line.split('"')[1]
                article_url_long = 'https://t66y.com/' + article_url_short
                if article_url_long not in article_urls:
                    article_urls.append(article_url_long)


def get_request_header():
    header_file = open(config_directory + 'request_header.txt')
    for line in header_file:
        line = line.replace('\r\n', '').replace('\n', '')
        print(line)
        if len(line) > 0:
            global headers
            headers = headers + line


main()
