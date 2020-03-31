from ruler import Ruler

ruler = Ruler('abcdfgh', 'abcdefg')

#On lance le calcul de la comparaison des deux séquences
ruler.compute()

#Expression de la distance entre les deux séquences
print(ruler.distance)

#Impression des deux séquences avec éléments de comparaison en couleur
top, bottom = ruler.report()
print(top)
print(bottom)