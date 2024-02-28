
import random
liste = [i for i in range(10)]
random.shuffle(liste)
if liste[0]%2==0:
    print("ecrit")
if liste[0]%2!=0:
    print("pratique")