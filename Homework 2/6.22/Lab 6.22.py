'''
Esteban Camarillo
ID #:1636095
Lab:6.22

'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())


def funca(x1, y1):
    return a * x1 + b * y1 - c


def funcb(x1, y1):
    return d * x1 + e * y1 - f


finalx = 100
finaly = 100
for x1 in range(-10, 11):
    for y1 in range(-10, 11):
        if funca(x1, y1) == funcb(x1, y1) and funca(x1, y1) == 0:
            finalx = x1
            finaly = y1
if finalx != 100:
    print(finalx, finaly)

else:
    print('No solution')