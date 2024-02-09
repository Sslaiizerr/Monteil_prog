import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python

# TAD Tableau
#
# Opérations
#       créerTableau : Entier → Tableau
#       nbEléments : Tableau → Entier
#       getIème : Tableau x Entier → Entier
#       setIème : Tableau x Entier x Entier → Tableau
#
# Préconditions
#       créerTableau(n) ssi n > 0
#       getIème(tab, i) ssi 0 <= i < nbElements(tab)
#       setIème(tab, i, e) ssi 0 <= i < nbElements(tab)
#
# Axiomes
#       (A1)    nbEléments(créerTableau(n)) = n
#       (A2)    nbEléments(setIème(tab, i, e)) = nbEléments(tab)
#       (A3)    getIème(créerTableau(n), i) = 0
#       (A4)    getIème(setIème (tab, i, e), i') =
#                   e si i = i'
#                   getIème(tab, i) sinon


class Tableau:

    # créerTableau : Entier → Tableau
    def __init__(self, n):
        assert n > 0, "le nombre d'éléments du tableau doit être strictement positif"
        self._elements = []
        self._elements.append("")
        for i in range(n):
            self._elements.append(0)

    # nbEléments : Tableau → Entier
    def nbElements(self):
        return len(self._elements)-1

    # getIème : Tableau x Entier → Entier
    def getIeme(self, i):
        assert 1 <= i < len(self._elements)+1, "l'indice d'accès n'est pas valide"
        return self._elements[i]

    # setIème : Tableau x Entier x Entier → Tableau
    def setIeme(self, i, e):
        assert 1 <= i < len(self._elements)+2, "l'indice d'accès n'est pas valide"
        self._elements[i] = e

    # retourne une chaine de caractères représentative de l'état de l'instance
    def __str__(self):
        return str(self._elements)

    # donne le schéma de construction de l'instance
    def __repr__(self):
        return "Tableau(" + str(len(self._elements)) + ")"

    # test d'égalité de deux tableaux
    def __eq__(self, tab):
        return self._elements == tab._elements
    
    def draw(self,g):
        c = graphviz.Graph(strict=True)
        for i in range (1,len(self._elements)):
            for j in self._elements[i]:
                c.edge(str(i),str(j))
        name = g + '.gv'
        c.render(name, view=True) # fermer le lecteur pdf avant de relancer le code python
    
if __name__ == "__main__":
    T=Tableau(5)  # tableau )= list , i=0 => nom du graphe ou ""
    print(T)
    print(T.nbElements())
    T.setIeme(1,(2,5))
    print(T)
    T.setIeme(2,(1,3,4,5))
    print(T)
    T.setIeme(3,(2,4))
    print(T)
    T.setIeme(4,(2,3,5))
    print(T)
    T.setIeme(5,(1,2,4))
    print(T)
    print(T.getIeme(5))
    print(T)
    T.draw("T")