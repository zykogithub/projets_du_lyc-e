# Créé par n.mohamed, le 12/09/2022 en Python 3.7
from random import*

listeee=[5,3,4,8]
e=4
range=listeee.sort

'''
def dichotomie_1(liste,int) :
    milieu=len(liste)//2
    for i in range(milieu):
        if milieu==int:
            print("il y est")
        elif milieu>int:
            return n
'''
##corection


def dichotomie_1(liste,int) :
    debut=0
    fin=len(liste)-1
    milieu=debut+fin//2
    while milieu<=fin:
        if int==milieu:
            return true
        elif int>milieu:
            milieu=+1
        elif int<milieu:
            milieu=-1
    return false
print(dichotomie_1(listeee,e))

##A retenir : L’algorithme de dichotomie a une complexité logarithmique notée O(log(n)).




    for i in range(len(lst) - 1) :
       imin = i
       for j in range(i + 1, len(lst)) :
            if lst[j] < lst[imin] :
                  imin = j
       if imin != i:
           lst[i], lst[imin] = lst[imin], lst[i]

           def tri_selection(lst) :
    """
    :param lst: une liste de longueur n
    :returns: pas de valeur renvoyée

    >>> liste = [0, 3, 2, 1, 6, 8]
    >>> procedure_triSel(liste)
    >>> liste
    [0, 1, 2, 3, 6, 8]

    """

    for i in range(len(lst) - 1) :
       imin = i
       for j in range(i + 1, len(lst)) :
            if lst[j] < lst[imin] :
                  imin = j
       if imin != i:
           lst[i], lst[imin] = lst[imin], lst[i]

lst = [62, 25, 71, 10, 3, 13, 50, 40, 27, 27]
tri_selection(lst)
print(lst)