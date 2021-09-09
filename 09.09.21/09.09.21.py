names = ['mush bag rom','ugun os as','mushba roman romanov']

def initials(name):
    l = name.split()
    return l[0] + ' ' + l[1][0:1] + '.' + l[2][0:1] + '.'

def initials_more(names):
    return [initials(name) for name in names]
from random import shuffle
shuffle (names)
print(initials_more(names*3))