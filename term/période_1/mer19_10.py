def nb_sommes(n):
    compteur=0
    for i in range(1,n):
        if (n-i)+(n-i+1)==n:
            compteur+=1
    return compteur



def maximum(nombres):
    for i in range (len(nombres)-1):
        cle=i
        for j in range(i+1,len(nombres)):
            if nombres[j]>cle:
                cle=j
        if cle!=i:
            nombres[i],nombres[cle]=nombres[cle],nombres[i]



def maxixi(nombres):
    nombres.sort
    a=nombres[0]
    return a

# Tests
# tests



a=[98, 12, 104, 23, 131, 9]
b=[-27, 24, -3, 15]

a.sort()
print(a,a[-1])