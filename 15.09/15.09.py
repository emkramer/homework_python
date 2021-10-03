import random

x = [1,1,1,2,2,3,4,5]
s = input("введите число:" )
b = 4
m = 10
print(set(x))
print(set(s))
print(len(set(x)))
print(b in x)
print(m in x)
#2/
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}

#3/
set_1.update(set_2)
print(set_1, set_2)
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}
set_2.intersection_update(set_1)
print(set_1, set_2)
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}
set_1.difference_update(set_2)
print(set_1, set_2)
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}
set_1.symmetric_difference_update(set_2)
print(set_1, set_2)
set_1 = {1,2,3,4,5,6}
set_2 = {4,5,6,7,8,9}
set_1.add(1098)
print(set_1)
set_1.remove(6)
print(set_1)
set_1.pop()
print(set_1)
set_1.clear


def unique(x):
    return list(set(x))


def intersection(x,y):
    pk = set(x)
    pl = set(y)
    return list(pk.intersection(pl))

n = random.randint(0,50)
x = list()
for i in range(n):
    x.append(random.randint(1, 50))
print(x)
print(unique(x))
x = input('введите еще одно чиcло:')
x_list = [ ]
x2_list = [ ]
n = random.randint(1,20)
for i in range(n):
    x_list.append(random.randint(1,10))
for i in range(n):
    x2_list.append(random.randint(1,10))
print(x_list, x2_list)
print(intersection(x_list, x2_list))
