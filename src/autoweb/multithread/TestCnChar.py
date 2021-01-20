# _*_ coding:utf-8 _*_

text_1 = '我是汉字'
print('before::')
print(text_1)
print('after::')
print(text_1.encode('utf-8').decode('GBK'))
