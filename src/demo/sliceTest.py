L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
slicedL = L[0: 3]
print(slicedL)


def trimString(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


str1 = '   1   123  '
print("trim之前长度: ", len(str1))
str = trimString(str1)
print(str)
print("trim之后长度: ", len(str))
