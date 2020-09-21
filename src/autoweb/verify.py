import requests

index_urls = []
article_urls = []
counter = 0
headers = ""
root_path = 'C:\\temp\\image_downloader\\'
image_directory = "C:\\temp\\image_downloader\\downloaded_images\\"
config_directory = "C:\\temp\\image_downloader\\config\\"


def main():
    get_index_urls()
    get_article_urls()


def get_index_urls():
    index_file = open(config_directory + 'index_url.txt', 'r')
    for line in index_file:
        line = line.replace('\r\n', '').replace('\n', '')
        if len(line) > 0:
            index_urls.append(line)


def get_article_urls():
    for index_url in index_urls:
        print(index_url)


def get_request_header():
    header_file = open(config_directory + 'request_header.txt')
    for line in header_file:
        line = line.replace('\r\n', '').replace('\n', '')
        print(line)
        if len(line) > 0:
            global headers
            headers = headers + line


