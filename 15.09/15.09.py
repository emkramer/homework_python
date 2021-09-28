list_ = [1, 1, 2, 2]
g = set(list_)
d = set('aabbcc')
#print(g, d)
'''
set_1 = {1, 2, 3, 4, 5, 6}
set_2 = {4, 5, 6, 7, 8, 9}
print(set_1.isdisjoint(set_2))
print(set_1.union(set_2))
print(set_1.difference(set_2))
print(set_1.symmetric_difference(set_2))
cop = set_1.copy()
print(cop)
print('////////////////')
set_1.update(set_2)
print(set_1)
set_1.symmetric_difference_update(set_2)
print(set_1)
set_1.difference_update(set_2)
print(set_1)
set_2.add(3)
print(set_2)
set_1.remove(1)
print(set_1)
set_1.clear()
print(set_1)
'''

l = [1, 1, 2, 2, 4, 5]
h = [9, 8, 7, 6, 5, 4]
def unique(l):
    return list(set(l))
#print(unique(l))

def intersection_lists(l, h):
    l, h = set(l), set(h)
    return list(l & h)

print(intersection_lists(l, h))
