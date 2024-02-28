# Créé par n.mohamed, le 30/11/2021 en Python 3.7

'''persos = [{"prenom": "Bilbo", "nom": "Baggins", "age" : 111},{"prenom" : "Frobbo", "nom" : "Baggins", "age" : 33}, {"prenom" : "Sam", "nom" : "Gamgee", "age" : 21}]


for p in persos :
    print("---------")
    for k,v in p.items():
        print(k, ":", v)
'''

'''exercice dictionnaire'''


exemple_pokemons = {"Bulbizarre" : (70,7),"Herbizarre" : (100,13),"Jungkok" : (170,52)}
exemple_pokemons ["Goupix"]=(60,10)
'''
print(exemple_pokemons)
'''
def leplusgrand(pokemons) :
    grand = None
    taille_max  = None
    for (nom,(taille, poinds)) in pokemons.items():
        if taille_max is None or taille>taille_max:
            taille_max = taille
            grand = nom
    return(grand, taille_max)

print(leplusgrand(exemple_pokemons))


def leplusleger(pokemons) :
    leger = None
    masse_min  = None
    for (nom,(taille, poids)) in pokemons.items():
        if masse_min is None or taille<masse_min:
            masse_min = taille
            leger = nom
    return(leger, masse_min)

print(leplusleger(exemple_pokemons))

'''correction
def taille(pokemon,nom) :
    if nom in pokemon :
        return pokemon[nom][0]
    else:
        return None

print(taille(exemple_pokemons,'Goupix'))

'''
zoo_Beauval = {"éléphant" : ("Asie", 5), "écureil" : ("Asie", 17),"panda" : ("")}
