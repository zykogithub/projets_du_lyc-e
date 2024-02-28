# Créé par n.mohamed, le 26/09/2022 en Python 3.7

'''

def repeat(n,txt) -> str :
    if n==1:
        return txt
    else:
        return txt+repeat(n-1,txt)


print(repeat(3,"bla"))

'''

def toto(n):
    if n==0:
        return "'0'"
    else:
        return toto(n-1),"+",toto(n-1)
print(toto(5))
