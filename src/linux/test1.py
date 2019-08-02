import platform
str1 = " /home/ecap/ "
str1 = str1.strip()
print str1

if str1.endswith("/"):
    print str1
else:

    str1 = str1 + '/'

platformInfo = platform.platform()
print(platformInfo)
print(type(platformInfo))
