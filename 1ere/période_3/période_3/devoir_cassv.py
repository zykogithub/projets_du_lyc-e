# Créé par n.mohamed, le 13/01/2022 en Python 3.7
import csv
'''csv_file = open('personnes.csv', "r")
reader = csv.reader(csv_file) # row signifie rangée ce qui correspond à une ligne
for row in reader:
    print(row)
csv_file.close()
csv_file = open('personnes.csv', 'r')
reader = csv.reader(csv_file)
personnes = [row for row in reader]
print(personnes)
csv_file.close()
csv_file = open('personnes.csv', "r")
reader = csv.DictReader(csv_file) # row signifie rangée ce qui correspond à une ligne
for row in reader:
    print(dict(row)) # Chaque ligne est transformée en dictionnaire
csv_file.close()
csv_file = open('personnes.csv', "r")
reader = csv.DictReader(csv_file)
personnes = [row for row in reader]
personnes.append(reader(row)) # Ne pas oublier de transformer chaque ligne en dictionnaire
print(personnes)
csv_file.close()

csv_file = open('transports.csv', "r")
reader = csv.DictReader(csv_file)
transports= [dict(ligne) for ligne in reader]
print(transports)
csv_file.close()

for i in range(len(transports)):
    for v in [ vh for vh in transports if vh['age']==transports[i]['age'] ]:
        transports[i]['vehicule'] = v['vehicule']
print(transports)'''
csv_file = open('villes.csv', 'r')
reader=csv.DictReader(csv_file)
villes=[dict(ligne) for ligne in reader]
for i in range (10):
    print(villes)

