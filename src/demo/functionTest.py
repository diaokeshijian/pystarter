def power(x, n=2):
    s = 1
    while n > 0:
        s = x * s
        n = n - 1
    return s


y = power(4)
print(y)


def calc(*numbers):
    summ = 0
    for n in numbers:
        summ = summ + n*n
    return summ


numbers1 = [1, 2]
result = calc(*numbers1)
print(result)

result1 = calc(1, 2)
print(result1)


def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)


print('***************************')
person('eli', 30)
person('Serena', 18, who = 'eli\'s girl friend', times = 3)

