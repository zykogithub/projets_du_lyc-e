import numpy as np
from random import*
import matplotlib.pyplot as plt
plt.axis([-4,5,-2,10])
plt.grid()


























































































'''x= np.linspace(-5,5,30)
y=x**2
plt.plot(x,y)
plt.savefig("graphique1.png")
plt.show()
plt.close()
#plt.axis('equal')#repère orthonormé"
#on peut utiliser latex
plt.title(r'$\alpha_i > \beta_i \frac{1}{2}u_n q^3$')

plt.xlabel("C'est Noel")
plt.ylabel("Vive le vent")
x=[0,100,150,0]
y=[0,10,10,0]
plt.plot(x, y,"r*") #points rouges représentés par *
x2=[120,160,180]
y2=[20,10,20]
plt.plot(x2,y2)#sans autres arguments, les points sont reliés entre eux

plt.plot([50,100,150,200], [1,2,3,4], "r--", linewidth=5)
plt.plot([50,100,150,200], [1,4,6,8], "bs", linewidth=5)
plt.plot([50,100,150,200], [1,6,9,12], "g^", linewidth=5)

plt.show()
plt.close()

#une listre de 5 nombres de [0,10]régulièremetn répartis
tableau = np.linspace(0,10,5)
print(tableau)
liste=[randint(1,1000) for i in range(10000)]
moyenne=mean(liste)
minimum=min(liste)
maximun=max(liste)
mediane=median(liste)
ecarType=stdev(liste)
variance=variance(liste)
q1=percentile(liste,25)
q3=percentile(liste,75)
print("nombre de 500 : ", liste.count(500),)
print("moyenne : ",moyenne)
print("mediane : ", mediane)
print("minimum : ", minimum)
print("maximum : ", maximun)
print("ecart-type", ecarType)
print("variance : ", variance)
print("Q1 : ", q1)
print("Q3 : ", q3)
nombre=float(input("Saisir un nombre"))
resultat=sqrt(nombre)
print(resultat)
sqrt= rzcine carré'''
