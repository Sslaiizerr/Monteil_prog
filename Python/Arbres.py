# from math import *
# import matplotlib.pyplot as plt

# arbre = ["1", "2", "3", "4", "5", " ", "6",
#          " ", " ", "7", "8", " ", " ", "9", " "]

# # print(arbre[0:1])
# # print(arbre[1:3])
# # print(arbre[3:7])
# # print(arbre[7:15])

# for i in range(4):
#     # print(2**i - 1)
#     print(arbre[2**i - 1: 2**i - 1 + 2**i])


# class Noeud:

#     def __init__(self, valeur):
#         self.donnee = valeur
#         self.gauche = None
#         self.droit = None

#     def __str__(self):
#         # return (str(self.donnee) + " a pour enfant : " + str(self.SAG) + " à gauche et " + str(self.SAD) + " à droite.")
#         return "({}, {}, {})".format(self.gauche, self.donnee, self.droit)
#         # return (str(self.gauche) + ", " + str(self.donnee) + ", " + str(self.droit))

#     def SAG(self, value):
#         self.gauche = value

#     def SAD(self, value):
#         self.droit = value

#     def assemblage(self, ag, ad):
#         if self.gauche == None:
#             self.gauche = ag
#         if self.gauche == None:
#             self.droite = ad

#     def dump(self):
#         self._dump(0)

#     def _dump(self, level):
#         if self.droit:
#             self.droit._dump(level + 1)
#         print("({}, {}, {})".format('' * 4 * level, self.donnee, "<"))
#         if self.gauche:
#             self.gauche._dump(level + 1)


# N_A = Noeud("A")
# print("noeud", N_A.donnee, "= ", N_A)

# N_B = Noeud("B")
# print("noeud", N_B.donnee, "= ", N_B)

# N_A.SAG(N_B)
# print("noeud", N_A.donnee, "= ", N_A)

# N_C = Noeud("C")
# print("noeud", N_C.donnee, "= ", N_C)

# N_A.SAD(N_C)
# print("noeud", N_A.donnee, "= ", N_A)

# N_A.dump()


# ///////////////////////////////////////////////////////////////////////////////////// #


# TAD Arbre[E]
#
# Opérations
#       créerArbre: → Arbre[E]
#       estVide : Arbre[E] → Booléen
#       racine : Arbre[E] → E
#       sag : Arbre[E] → Arbre[E]
#       sad: Arbre[E] → Arbre[E]
#       ajouter : Arbre[E] x E → Arbre[E]
#       existe : Arbre[E] x E → Booléen
#       hauteur : Arbre[E] → Entier
#       hauteurNoeud : Arbre[E] → Entier
#       minimum : Arbre[E] → Entier
#       maximum : Arbre[E] → Entier

import matplotlib.pyplot as plt


class Arbre:

    # créerArbre: → Arbre[E]
    def __init__(self):
        self._racine = None
        self._gauche = None
        self._droit = None

    # estVide : Arbre[E] → Booléen
    def estVide(self):
        return self._racine is None

    # racine : Arbre[E] → E
    def racine(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._racine

    # sag : Arbre[E] → Arbre[E]
    def sag(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._gauche

    # sad: Arbre[E] → Arbre[E]
    def sad(self):
        assert not self.estVide(), "l'arbre est vide"
        return self._droit

    # parcours préfixé  de l'arbre a (ou parcours RGD)
    def parcoursPre(self):
        if self.estVide():
            return []
        else:
            return self._parcoursPre([])

    def _parcoursPre(self, l):
        l.append(self._racine)
        if self._gauche:
            self._gauche._parcoursPre(l)
        if self._droit:
            self._droit._parcoursPre(l)
        return l

    # parcours infixé de l'arbre a (ou parcours GRD)
    def parcoursInf(self):
        if self.estVide():
            return []
        else:
            return self._parcoursInf([])

    def _parcoursInf(self, l):
        print("compléter _parcoursInf")

    # parcours postfixé de l'arbre a (ou parcours GDR)

    def parcoursPost(self):
        if self.estVide():
            return []
        else:
            return self._parcoursPost([])

    def _parcoursPost(self, l):
        print("compléter _parcoursPost")

    # ajouter : Arbre[E] x E → Arbre[E]
    # l'arbre est sans doublons : ajouter une valeur déjà existante est sans effet

    def ajouter(self, valeur):
        if self.estVide():
            self._racine = valeur
        else:
            if valeur == self._racine:
                return
            # print("compléter ajouter")
            elif valeur > self._racine:
                if not self._droit:
                    self._droit = Arbre()
                    self._droit._parent = self
                self._droit.ajouter(valeur)
            else:
                print("compléter ajouter")

    # existe: Arbre[E] x E → Booléen

    def existe(self, valeur):
        if self.estVide():
            return False
        else:
            if valeur < self._racine:
                if self._gauche is None:
                    return False
                else:
                    return self._gauche.existe(valeur)
            elif valeur > self._racine:
                if self._droit is None:
                    return False
                else:
                    return self._droit.existe(valeur)
            else:
                return True

    #  hauteur : Arbre[E] → Entier
    def hauteur(self):
        if self.estVide():
            return 0
        else:
            return self._hauteur()

    def _hauteur(self):
        if self._gauche is None:
            hg = 0
        else:
            hg = 1 + self._gauche._hauteur()
        if self._droit is None:
            hd = 0
        else:
            hd = 1 + self._droit._hauteur()
        return max(hg, hd)

    #  hauteurNoeud : Arbre[E] → Entier
    def hauteurNoeud(self, valeur):
        if self.estVide():
            assert False, "l'arbre est vide"
        return self._hauteurNoeud(valeur)
        # if self.existe(valeur):
        #    print("la valeur existe")
        #    return self._hauteurNoeud(valeur)
        # else:
        #    return "la valeur n'existe pas"

    def _hauteurNoeud(self, valeur):
        if valeur < self._racine:
            if self._gauche is None:
                assert False, "la valeur n'existe pas dans l'arbre "
            else:
                return 1 + self._gauche._hauteurNoeud(valeur)
        elif valeur > self._racine:
            if self._droit is None:
                assert False, "la valeur n'existe pas dans l'arbre "
            else:
                return 1 + self._droit._hauteurNoeud(valeur)
        else:
            return 0

    #  minimum : Arbre[E] → Entier
    def minimum(self):
        if self.estVide():
            assert False, "l'arbre est vide"
        while self._gauche:
            self = self._gauche
        return self._racine

    #  maximum : Arbre[E] → Entier
    def maximum(self):
        if self.estVide():
            assert False, "l'arbre est vide"
        while self._droit:
            self = self._droit
        return self._racine

    # retourne une chaine de caractères représentative de l'état de l'instance
    def __str__(self):
        return "({},{},{})".format(self._gauche, self._racine, self._droit)

    # donne le schéma de construction de l'instance
    def __repr__(self):
        return "Arbre()"

    # égal : Arbre[T] x Arbre[T] → Booléen
    def __eq__(self, a):
        if self.estVide() and a.estVide():
            return True
        if self.estVide() and not a.estVide():
            return False
        if not self.estVide() and a.estVide():
            return False
        if self._gauche is None and a._gauche is not None:
            return False
        if self._gauche is not None and a._gauche is None:
            return False
        if self._droit is None and a._droit is not None:
            return False
        if self._droit is not None and a._droit is None:
            return False
        return self._racine == a._racine and self._gauche == a._gauche and self._droit == a._droit

    # imprime un arbre binaire de recherche
    def dump(self):
        if self.estVide():
            print("arbre vide")
        else:
            self._dump(0)

    def _dump(self, level):
        if self._droit:
            self._droit._dump(level + 1)
        print(f"{' ' * 4 * level}{self._racine}")
        if self._gauche:
            self._gauche._dump(level + 1)

    # affiche un arbre binaire de recherche
    def _draw(self):
        plt.rcParams.update({'font.size': 14})
        # parcours en largeur
        an = []  # stockage des noeuds visités
        res = []  # stockage des noeuds parcourus en largeur
        posInit = 10 * self.hauteur()  # pour calculer la position des noeuds
        # racine affichée en (0, posInit)
        an.append((self, 0, posInit, "root"))
        # le parcours est terminé quand tous les noeuds ont été traités
        while (len(an) > 0):
            n = an[0]  # conservation du noeux courant pour gérer l'affichage
            res.append(n)
            # on le traite, donc on l'enlève de la liste des noeuds visités
            an.pop(0)
            h = n[2] - 10  # calcul de la position en y du noeud
            ecart = 10 * self.hauteur()  # pour améliorer l'affichage
            # les fils du noeud courant sont ajoutés
            # tracé de l'arc entre le noeud courant et les fils gauche et droit
            if (n[0]._gauche is not None):
                an.append((n[0]._gauche, n[1] - (ecart + h), h, "left"))
                plt.plot([n[1], n[1] - (ecart + h)],
                         [n[2] - 3, h + 3], color='red', marker='o')
            if (n[0]._droit is not None):
                an.append((n[0]._droit, n[1] + (ecart + h), h, "right"))
                plt.plot([n[1], n[1] + (ecart + h)],
                         [n[2] - 3, h + 3], color='green', marker='o')
        # une fois les noeuds positionnés, on les affiche, tout en calculant
        # la taille de graphique nécessaire
        xmin = res[0][1]
        xmax = res[0][1]
        # pour calculer le décalage nécessaire pour que les noeuds ne se chevauchent pas
        nbNoeuds = len(res)
        for x in res:
            if (x[0] is not None):
                if (x[3] == "left"):  # décalage adapté pour fils gauche ou droit
                    decalage = (-nbNoeuds) * 4 + 40
                else:
                    decalage = nbNoeuds - 30
                # la valeur du noeud est affichée
                plt.annotate(str(x[0]._racine), (x[1] + decalage, x[2]))
                #    print(str(x[0]._racine), (x[1] +decalage, x[2]), x[3])
                if (x[1] < xmin):
                    xmin = x[1]
                if (x[1] > xmax):
                    xmax = x[1]
        # taille du graphique
        plt.xlim(xmin - 100, xmax + 100)
        plt.ylim(-10, posInit + 10)
        # affichage du graphique
        plt.show()

    # construire l'arbre 12,20,20,8,10,14,13,16,18,17,19,21
    def construireArbre():
        # print("compléter construireArbre")
        a = Arbre()
        a.ajouter(15)
        a.ajouter(12)
        a.ajouter(20)
        a.ajouter(20)
        a.ajouter(8)
        a.ajouter(10)
        a.ajouter(14)
        a.ajouter(13)
        a.ajouter(16)
        a.ajouter(18)
        a.ajouter(17)
        a.ajouter(19)
        a.ajouter(21)
        return a

    # rechercher: Arbre[E] x E → Booléen
    def rechercher(self, valeur):
        print("compléter rechercher")


if __name__ == '__main__':
    print("compléter pour tester")
