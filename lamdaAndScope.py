from math import sqrt as sq
def addition(num):
    return sq(num)
l1=[5,6,7,8,9]
l2=list(map(addition,l1))
print(l2)
l3=list(map(lambda k:sq(k),l2))
print(l3)

