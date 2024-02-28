from random import*

a=randint(1,5)
b=randint(1,5)
c=randint(1,5)
d=randint(1,5)

def manhattan(XA,XB,YA,YB):
    return abs(XB-XA)+abs(YB-YA)


def euclidienne_carre(XA,XB,YA,YB):
    distance= (XB-XA)**2+(YB-YA)**2
    return distance


def tchebychev(XA,XB,YA,YB):
    distance= max(abs(XB-XA),abs(YB-YA))
    return distance

print(a,b,c,d)
print(manhattan(a,b,c,d))