from Tableau import Tableau

# import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python


class ListeAdj:

    def __init__(self, nbSommets):
        assert nbSommets >= 1, "le nombre de sommet de liste d'Adjacence supérieur à 1"
        self._listeAdj = []
        for i in range(nbSommets+1):
            self._listeAdj.append([])

# --------------------------------------------------
    # COMPLETER LA CLASSE

    def nbSommets(self):
        return len(self._listeAdj) - 1

    def ajoutArete(self, i, j):
        assert 0 < i <= self.nbSommets(), "le sommet est incorrect"
        if not j in self._listeAdj[i] and not i in self._listeAdj[j]:
            self._listeAdj[i].append(j)
            self._listeAdj[j].append(i)

    def enleveArete(self, i, j):
        assert 0 < i <= self.nbSommets(), "le sommet est incorrect"
        assert 0 < j <= self.nbSommets(), "le sommet est incorrect"
        if j in self._listeAdj[i] == True:
            self._listeAdj[i].remove(j)
        if i in self._listeAdj[j] == True:
            self._listeAdj[j].remove(i)

    def nbAretes(self):
        nbA = 0
        for elt in self._listeAdj:
            nbA = nbA + len(elt)
        # return (nbA / 2) si le graphes est non orienté
        # return nbA
        return (nbA / 2)

    def getAretesSommet(self, i):
        assert 0 < i <= self.nbSommets(), "le sommet est incorrect"
        return self._listeAdj[i]

    def degreSommet(self, i):
        assert 0 < i <= self.nbSommets(), "le sommet est incorrect"
        return len(self._listeAdj[i])

    def degre(self):
        T = Tableau(len(self._listeAdj)-1)
        for i in range(1, len(self._listeAdj)):
            T.setIeme(i, len(self._listeAdj[i]))
        return T

    # GRAPHIQUE NE FONCTIONNE PAS (NE PAS CHERCHER A CE QUE CA FONCTIONNE)
    # def draw(self, g):
    #     # c = graphviz.Digraph(strict=False) # orienté
    #     c = graphviz.Graph(strict=True)  # non orienté
    #     for i in range(1, len(self._listeAdj)):
    #         for j in self._listeAdj[i]:
    #             c.edge(str(i), str(j))

        name = g + '.gv'
        # fermer le lecteur pdf avant de relancer le code python
        c.render(name, view=True)


# ------------------------------------------------------


    def __str__(self):
        return str(self._listeAdj)

    def __repr__(self):
        return "ListeAdj(" + str(self.nbSommets()) + ")"

    def __eq__(self, list):
        return self._listeAdj == list


if __name__ == "__main__":
    A = ListeAdj(5)
    print(A)
    print("le nombre de sommet de ce graphe est", A.nbSommets())
    A.ajoutArete(1, 2)
    # print(A)
    A.ajoutArete(1, 2)
    # print(A)
    A.ajoutArete(2, 1)
    # print(A)
    A.ajoutArete(1, 5)
    # print(A)
    A.ajoutArete(2, 3)
    # print(A)
    A.ajoutArete(2, 4)
    # print(A)
    A.ajoutArete(2, 5)
    # print(A)
    A.ajoutArete(3, 4)
    # print(A)
    A.ajoutArete(4, 5)
    print(A)
    # # A.enleveArete(2,4)
    # # print(A)
    # # A.enleveArete(3,4)
    # # print(A)
    # print("le nombre d'Aretes de ce graphe est", A.nbAretes())
    # print("Les arêtes du sommet 1 sont : ", A.getAretesSommet(1))
    # print("le degré du sommet 1 est :", A.degreSommet(1))
    # print(A)
    # # print(A)
    # print("le degré des sommets", A.degre())
    # A.draw("A") # fermer le lecteur pdf avant de relancer le code python
