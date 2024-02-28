# Créé par n.mohamed, le 07/10/2021 en Python 3.7

#Module Alice

def fonction1(x):
    """ retourne le carre de x"""
    return x**2

def fonction2(n,k):
    """ retourne la liste des k premiers multiples de n
    Par exemple fonction2(5,4) retourne [5,10,15,20]"""
    liste_multiples=k*[0]
    for i in range(k):
        liste_multiples[i]=(i+1)*n
    return liste_multiples