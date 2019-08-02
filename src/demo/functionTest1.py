X = 'Spam'


def func():
    global X
    X = 'NI!'


func()
print(X)
