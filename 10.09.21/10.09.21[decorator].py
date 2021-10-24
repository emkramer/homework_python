import random
from random import randint

l = []

for i in range(44):
    l.append(randint(-99, 99))
q = [c for c in l]

def func(s):
    i = 0
    while i < len(s):
        print(s[i])
        i=i+1

def decorator(leng):
    def innerfunc(*args, **keywords):
        print('Running function:', leng.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', keywords)
        result = leng(*args, **keywords)
        print('Result: ', result)
        return result
    return innerfunc
decor = decorator(func)
decor(l)
