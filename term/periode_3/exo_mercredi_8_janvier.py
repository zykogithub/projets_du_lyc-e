def indice(caractere):
    "Renvoie l'indice de caractere qui doit être une majuscule"
    return ord(caractere) - ord('A')
    
def majuscule(i):
    """Renvoie la majuscule d'indice donnée
    majuscule(0) renvoie 'A'
    majuscule(25) renvoie 'Z'
    """
    return chr(ord('A') + i)

def cesar(message, decalage):
    resultat = ''
    for caractere in message:
        if 'A' <= caractere <= "Z":
            i = indice(caractere)
            i = (i + decalage)
            resultat += majuscule(i)
        else:
            resultat += caractere
    return resultat 


# tests

# assert cesar('HELLO WORLD!', 5) == 'MJQQT BTWQI!'
# assert cesar('MJQQT BTWQI!', -5) == 'HELLO WORLD!'

# assert cesar('BONJOUR LE MONDE !', 23) == 'YLKGLRO IB JLKAB !'
# assert cesar('YLKGLRO IB JLKAB !', -23) == 'BONJOUR LE MONDE !'
print(cesar('BONJOUR LE MONDE !', 23))
print(cesar('YLKGLRO IB JLKAB !', -23))

