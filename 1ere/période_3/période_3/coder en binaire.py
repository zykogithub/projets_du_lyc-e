# Créé par n.mohamed, le 23/11/2021 en Python 3.7
b=5
a=0
liste=[0,1,2]

for i in range (len(liste)):
    b=b-2**(max(liste)-i)
    while b:
        a=a+1
        b=b-2**(max(liste)-a)
        print(b)




