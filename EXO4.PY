#exercice 4
import random
from math import sqrt
#fonction qui retourne une liste de 100 element aleatoire 
def getliste():
    liste = []

    for i in range(0,100):
        a=random.random()*100
        b=round(a,1)
        liste.append(b) 
    return liste

#calcule de la moyenne   
ma_liste = getliste()
moyenne = sum(ma_liste)/100

mediane= (ma_liste[49]+ ma_liste[50])/2
print(mediane)
print(moyenne)


temp_somme=0
for element in ma_liste:

    temp_some=temp_some + (element-moyenne)**2

variance= temp_some /100

print(variance)
ecarttype=sqrt(variance)
print(ecarttype)
print(ma_liste)
print(f"moyenne={moyenne}")
print(f"mediane={mediane}")
print(f"variance={variance}")
print(f"ecarttype={ecarttype}")
