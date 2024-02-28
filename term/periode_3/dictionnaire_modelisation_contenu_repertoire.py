docs = {
    "Administratif":{
        "certificat_JDC.pdf": 1500,
        "attestation_recensement.pdf": 850
    },
    "Cours": {
        "NSI": {
            "TP.html": 60,
            "dm.odt": 345
        },
        "Philo": {
            "Tractatus_logico-philosophicus.epub": 2600
        }
    },
    "liste_de_courses.txt": 24
}

def parcourt(racine, adr):
    repertoire = racine
    for nom_repertoire in adr:
        repertoire = repertoire[nom_repertoire]
    return repertoire

def ajoute_fichier(racine, adr, nom_fichier, taille):
    repertoire = parcourt(racine, adr)
    repertoire[nom_fichier] = taille
    
    
def ajoute_repertoire(racine, adr, nom_repertoire):
    repertoire = parcourt(racine, adr)
    repertoire[nom_repertoire] = dict()

def est_fichier(repertoire, cle):
    return isinstance(repertoire[cle], int)

def taille(racine):
    if est_fichier(racine):
        for cle in racine:
            return racine[cle]
    else:
        cumul = 0
        for cle in racine:
            cumul += taille(racine[cle])
        return cumul
#code principal

liste_parcours=["Cours","NSI"]
print(parcourt(docs,liste_parcours))
ajoute_fichier(docs,liste_parcours,"exo.py",4)
ajoute_repertoire(docs,liste_parcours,"code_par_cœur")
print(est_fichier(docs,"Cours"),est_fichier(docs,"liste_de_courses.txt"))
print(taille(docs))