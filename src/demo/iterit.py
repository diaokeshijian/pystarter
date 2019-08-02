letters = ['a', 'b', 'c', 'd', 'e']
iter(letters)


def iter(element_list):
    for element in element_list:
        print(element)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, b + a
        n = n + 1
    return 'done'


fib(0)


def open_file():
    file = open('1.txt')
    text = file.read()
    print(text)


#open_file()
str = 'C:\new\files\1.txt'
print(str)
raw_str = r'C:\new\files\1.txt'
print(raw_str)

