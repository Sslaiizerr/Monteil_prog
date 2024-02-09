from Tableau import Tableau

import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python

class ListeAdj:

    def __init__(self, nbSommets):
        assert nbSommets >= 1, "le nombre de sommet de liste d'Adjacence supérieur à 1"
        self._listA = []
        for i in range(nbSommets + 1):
            self._listA.append([])

# --------------------------------------------------
    # COMPLETER LA CLASSE

    def nbSommets(self):
        return len(self._listA)-1

    def nbAretes(self):
        NbA = 0
        for i in range (1,len(self._listA)):
            NbA = NbA + len(self._listA[i])
        # return int(NbA/2)  # non orienté
        return int(NbA)  # orienté

    def ajoutArete(self, i, j):
        assert 0 < i <= self.nbSommets() , "le sommet est incorrect"
        #if not j in self._listA[i] : # si on veut éviter les doublons, graphe non orienté ?
        #    self._listA[i].append(j) # si on veut éviter les doublons, graphe non orienté ?
        self._listA[i].append(j)

    def enleveArete(self, i, j):
        assert 0 < i <= self.nbSommets() , "le sommet est incorrect"
        assert 0 < j <= self.nbSommets() , "le sommet est incorrect"
        if j in self._listA[i] : # vérifier la présence de j
            self._listA[i].remove(j)
            self._listA[j].remove(i)

    def getAretesSommet(self, i):
        assert 0 < i <= self.nbSommets() , "le sommet est incorrect"
        return self._listA[i]

    def degreSommet(self, i):
        return len(self._listA[i])

    def degre(self):
        T=Tableau(len(self._listA)-1)
        for i in range (1,len(self._listA)):
            # print(self._listA[i])
            T.setIeme(i-1,len(self._listA[i]))
        return T

    def draw(self,g):
        # c = graphviz.Digraph(strict=False) # orienté
        c = graphviz.Graph(strict=False) #non orienté
        for i in range (1,len(self._listA)):
            for j in self._listA[i]:
                c.edge(str(i),str(j))
        name = g + '.gv'
        c.render(name, view=True) # fermer le lecteur pdf avant de relancer le code python

    def drawNonOriente(self,g):
        # c = graphviz.Digraph(strict=False) # orienté
        c = graphviz.Graph(strict=True) #non orienté
        for i in range (1,len(self._listA)):
            for j in self._listA[i]:
                c.edge(str(i),str(j))
        name = g + '.gv'
        c.render(name, view=True) # fermer le lecteur pdf avant de relancer le code python

    def drawNonOriente_nommé(self,g,Tab_Nom):
        # c = graphviz.Digraph(strict=False) # orienté
        c = graphviz.Graph(strict=True) #non orienté
        for i in range (1,len(self._listA)):
            for j in self._listA[i]:
                # print((Tab_Nom[i],Tab_Nom[j]))
                #c.edge(str(i),str(j))
                c.edge(str(Tab_Nom[i]),str(Tab_Nom[j]))
        name = g + '.gv'
        c.render(name, view=True) # fermer le lecteur pdf avant de relancer le code python


    def drawOriente(self,g):
        c = graphviz.Digraph(strict=False) # orienté
        # c = graphviz.Graph(strict=False) #non orienté
        for i in range (1,len(self._listA)):
            for j in self._listA[i]:
                c.edge(str(i),str(j))
        name = g + '.gv'
        c.render(name, view=True) # fermer le lecteur pdf avant de relancer le code python

# ------------------------------------------------------
    def __str__(self):
        return str(self._listA)

    def __repr__(self):
        return "ListeAdj(" + str(self.nbSommets()) + ")"

    def __eq__(self, list):
        return self._listA == list
    
if __name__ == "__main__":
     A = ListeAdj(5)
     print(A)
     print("le nombre de sommet de ce graphe est",A.nbSommets())
     A.ajoutArete(1,2)
     A.ajoutArete(1,2)
     A.ajoutArete(1,5)
     A.ajoutArete(2,1)
     A.ajoutArete(2,3)
     A.ajoutArete(2,4)
     A.ajoutArete(2,5)
     A.ajoutArete(3,2)
     A.ajoutArete(3,4)
     A.ajoutArete(4,2)
     A.ajoutArete(4,3)
     A.ajoutArete(4,5)
     A.ajoutArete(5,1)
     A.ajoutArete(5,2)
     A.ajoutArete(5,4)
     print("le nombre d'Aretes de ce graphe est",A.nbAretes())
     print("Les arêtes du sommet 1 sont : ",A.getAretesSommet(1))
     print("le degré du sommet 1 est :",A.degreSommet(1))
     print(A)
     # A.enleveArete(2,4)
     # A.enleveArete(3,4)
     # print(A)
     print("le degré des sommets",A.degre())
     A.draw("A") # fermer le lecteur pdf avant de relancer le code python
     