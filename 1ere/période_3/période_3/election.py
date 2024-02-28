# Créé par n.mohamed, le 20/01/2022 en Python 3.7

import csv
csv_file=open('election.csv','r')
reader=csv.DictReader(csv_file)
dict_election=[dict(ligne) for ligne in reader]
##print(dict_election)
csv_file.close()


def selection_c_300(liste_dictionnaire):
    condition=[]
    if 'prenom'[0]=='c' and int('nb_voix')>300:
        condition.append(liste_dictionnaire)
    return condition
print(selection_c_300(dict_election))




