
def main():
    print('this message i from main function.')
    test_02()


def test_01():
    print('test_01')


def test_02():
    print('test_02')


with open('D:\\1.txt','a') as f:
    f.write('test01')
    f.write('\n')
    f.write('test02')

