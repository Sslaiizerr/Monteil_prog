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
        assert n > 0, "le nombre d'éléments du tableau doit être positif"
        self._elements = []
        for i in range(n):
            self._elements.append(0)

    # nbEléments : Tableau → Entier
    def nbElements(self):
        return len(self._elements)

    # getIème : Tableau x Entier → Entier
    def getIeme(self, i):
        assert 0 <= i < len(self._elements), "l'indice d'accès n'est pas valide"
        return self._elements[i]

    # setIème : Tableau x Entier x Entier → Tableau
    def setIeme(self, i, e):
        assert 0 <= i < len(self._elements), "l'indice d'accès n'est pas valide"
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
    
if __name__ == "__main__":
    T=Tableau(5)
    print(T)
    print(T.nbElements())
    print(T.getIeme(2))
    T.setIeme(0,(1,5))
    T.setIeme(1,(0,2,3,4))
    T.setIeme(2,(1,3))
    T.setIeme(3,(1,2,4))
    T.setIeme(4,(0,1,3))
    print(T)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    