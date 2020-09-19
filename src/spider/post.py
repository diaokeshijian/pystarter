import json
import requests
from bs4 import BeautifulSoup

def get_translate_data(word):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    form_data = {'i':word,'from': 'AUTO','to': 'AUTO','smartresult': 'dict','client': 'fanyideskweb',
                 'salt': '15860559797390','sign': '3484b41eb2f872a169c900018a6d4705','ts': '1586055979739',
                 'bv': 'e3024dc52ff5c694b77471a08006ba92','doctype': 'json','version': '2.1',
                 'keyfrom': 'fanyi.web','action': 'FY_BY_REALTlME','typoResult':'false'}
    response = requests.post(url,data=form_data)
    content = json.loads(response.text)
    print(content)

get_translate_data('我爱你')