f = open('240921[f4].txt', 'r')
lines = f.readlines()
lines = [line[:-1] for line in lines]

d = {lines[1]:lines[2],
lines[3]:int(lines[4])}

print(d)
f.close
