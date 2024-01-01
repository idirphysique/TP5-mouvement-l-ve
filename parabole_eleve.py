import matplotlib.pyplot as plt
import numpy as np
""" lecture des données t,x et y contenues dans le fichier .................."""
from pylab import *
""" ---------------------------------
        CHOIX du PROFESSEUR
------------------------------------- """
# 'avimeca'         (crééer un fichier TXT en export; attention écrire 0.001 par exemple et pas 0,001; enlever pointage avimeca et les intitulés t x y donc que les nombre en colonnes
t,x,y=loadtxt('parabole.txt', skiprows=1,unpack=True)

"""  GRAPHE  y(x)     ..................................................."""
plot(x,y,'*k:')
xlabel('x(m)');  ylabel('y(m)')

""" rajout vecteur V sur GRAPHE  ..........................................."""
# les vecteurs V depuis le second point jusqu'à l'avant-dernier ................
""" TRAVAIL 1:
Taper, DANS LA BOUCLE ci-dessous, le code python permettant:
    - d'ajouter au tableau Vx l'abscisse du vecteur vitesse au point numéro "i"
    - d'ajouter au tableau Vx l'abscisse du vecteur vitesse au point numéro "i" 
    - utiliser la méthode centrée
    - attention à l'indentation de la formule rajoutée= retrait de ligne avec la touche tab """

for i in range(1,len(t)-1):
   
    
    arrow(x[i], y[i], vx/10, vy/10,  head_width=0.02, head_length=0.02,color='r',length_includes_head= True,lw=0.5)

""" rajout vecteur a sur GRAPHE  ..........................................."""
# les vecteurs a depuis le troisième point jusqu'à l'antépénultième ............
""" TRAVAIL 2:
Taper ci-dessous le code python permettant:
    - de mettre dans une variable DeltaVx l'abscisse du vecteur variation de vitesse au point i
    - de mettre dans une variable DeltaVy l'ordonnée du vecteur variation de vitesse au point i
    - utiliser la méthode centrée
    - attention à l'indentation de la formule rajoutée= retrait de ligne avec la touche tab"""
for i in range(2,len(t)-2):
    
    
    arrow(x[i], y[i], deltaVx/30, deltaVy/30,  head_width=0.02, head_length=0.02,color='g',length_includes_head= True,lw=0.5)

"""  affichage  ..............................................."""
plt.show()

