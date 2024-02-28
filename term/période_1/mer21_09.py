'''

def ef f_4(n):
    print(n)
    if n > 0:
        f_4(n - 1)
f_4(4)


def sommme_i(n):
    compteur=0
    for i in range(n+1):
        compteur+=i
    return compteur
print(sommme_i(4))

def sommme_r(n):
    if n==0:
        return 0
    else:
        return sommme_r(n-1)+n
print(sommme_r(5))

'''

def longueur(ch):
    if ch=="":
        return 0
    else:
    return 1+longueur(ch[1:])
