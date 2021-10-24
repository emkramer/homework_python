first=[1,2,3,3,3,4,5,5,6,6,7]
second=[5,6,7,8,9,9,9,10,11,11,12]


def func1(first, second):
    return set(first).intersection(set(second))

print(list(set(first).intersection(set(second))))
