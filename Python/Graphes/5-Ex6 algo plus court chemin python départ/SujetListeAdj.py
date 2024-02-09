from Tableau import Tableau

import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python

class ListeAdj:

    def __init__(self, nbSommets):
        assert nbSommets >= 1, "le nombre de sommet de liste d'Adjacence supérieur à 1"
        self._listA = []
        for i in range(nbSommets+1):
            self._listA.append([])

    def nbSommets(self):
        return len(self._listA)-1

    def ajoutArete(self, i, j):
        assert 0 < i <= self.nbSommets() , "le sommet est incorrect"
        # if not j in self._listA[i] : # si on veut éviter les doublons, graphe non orienté ?
            # if not i in self._listA[j] : # si on veut éviter les doublons, graphe non orienté ?
                # self._listA[i].append(j)
                # self._listA[j].append(i) 
        self._listA[i].append(j) # si graphe non orienté

    def enleveArete(self, i, j):
        assert 0 < i <= self.nbSommets() , "le sommet est incorrect"
        assert 0 < j <= self.nbSommets() , "le sommet est incorrect"
        if j in self._listA[i] : # vérifier la présence de j pour le sommet i
            self._listA[i].remove(j)
    
    def nbAretes(self):
        NbA = 0
        for i in range (1,len(self._listA)):
            NbA = NbA + len(self._listA[i])
        # return int(NbA/2)  # non orienté
        return int(NbA)  # orienté

    def getAretesSommet(self, i):
        assert 0 < i <= self.nbSommets() , "le sommet est incorrect"
        return self._listA[i]

    def degreSommet(self, i):
        return len(self._listA[i])

    def degre(self):
        T=Tableau(len(self._listA)-1)
        for i in range (1,len(self._listA)):            
            T.setIeme(i,len(self._listA[i]))
        return T

    def draw(self,g):
        c = graphviz.Digraph(strict=False) # orienté
        #c = graphviz.Graph(strict=True) # non orienté
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
     A.ajoutArete(1,2)
     A.ajoutArete(1,5)
     A.ajoutArete(2,3)
     A.ajoutArete(2,4)
     A.ajoutArete(2,5)
     A.ajoutArete(3,4)
     A.ajoutArete(4,5)
     print(A)
     A.draw("A") # fermer le lecteur pdf avant de relancer le code python
     # A.enleveArete(4,5)
     # print(A)
     # A.draw("A-") # fermer le lecteur pdf avant de relancer le code python
 
     