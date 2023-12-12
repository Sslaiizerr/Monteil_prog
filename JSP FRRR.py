from math import *

arbre = ["1", "2", "3", "4", "5", " ", "6",
         " ", " ", "7", "8", " ", " ", "9", " "]

# print(arbre[0:1])
# print(arbre[1:3])
# print(arbre[3:7])
# print(arbre[7:15])

for i in range(4):
    # print(2**i - 1)
    print(arbre[2**i - 1: 2**i - 1 + 2**i])


class Noeud:

    def __init__(self, valeur):
        self.donnee = valeur
        self.gauche = None
        self.droite = None

    def SAG(self, value):
        self.gauche = value

    def SAD(self, value):
        self.droit = value

    def assemblage(self, ag, ad):
        self.gauche = ag
        self.droite = ad

    def __str__(self):
        # return (str(self.donnee) + " a pour enfant : " + str(self.SAG) + " à gauche et " + str(self.SAD) + " à droite.")
        return (str(self.SAG) + str(self.donnee) + str(self.SAD))
