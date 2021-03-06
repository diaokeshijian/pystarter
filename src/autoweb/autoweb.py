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
response = requests.get('https://t66y.com/htm_data/2009/16/4061369.html', headers=headers)
print(response.status_code)

response.encoding = 'gbk'
response_content = response.content.decode('utf-8', errors='ignore')

response_content_str = str(response_content)

response_content_in_lines = response_content_str.split(' ')

for line in response_content_in_lines:
    # print(line)
    if 'ess-data' in line and 'function' not in line and 'this' not in line:
        # print(line)
        line_element = line.split("'")
        # print(line_element)
        img_urls.append(line_element[1])

for img_url in img_urls:
    print(img_url)
    image_name = img_url.split('/')[-1]
    print('downloading ' + image_name)
    response_img = requests.get(img_url)
    response_img_content = response_img.content
    with open('C:\\Users\\Eli\\Desktop\\test\\' + image_name, 'wb') as imgfile:
        imgfile.write(response_img_content)
        print(image_name + ' has been downloaded.')
        counter = counter + 1
        print(str(counter) + ' of ' + str(len(img_urls)) + ' has been downloaded.')

