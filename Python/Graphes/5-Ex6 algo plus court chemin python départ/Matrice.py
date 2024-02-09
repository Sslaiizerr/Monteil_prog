import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python
# TAD Matrice
#
# Opérations
#       créerMatrice : Entier x Entier → Matrice
#       nbLignes : Matrice → Entier
#       nbColonnes : Matrice → Entier
#       getIJème : Matrice x Entier x Entier → Entier
#       setIJème : Matrice x Entier x Entier x Entier → Matrice
#
# Préconditions
#       créerMatrice(n, m) ssi n > 0 et m > 0
#       getIJème(mat, i, j) ssi 0 <= i < nbLignes(mat) et 0 <= j < nbColonnes(mat)
#       setIème(mat, i, j, e) ssi ssi 0 <= i < nbLignes(mat) et 0 <= j < nbColonnes(mat)
#
# Axiomes
#       (A1)    nbLignes(créerMatrice(n, m)) = n
#       (A2)    nbColonnes(créerMatrice(n, m)) = m
#       (A3)    nbLignes(setIJème(mat, i, j, e)) = nbLignes(mat)
#       (A4)    nbColonnes(setIJème(mat, i, j, e)) = nbColonnes(mat)
#       (A5)    getIJème(créerMatrice(n, m), i, j) = 0
#       (A6)    getIJème(setIJème (mat, i, j, e), i', j') =
#                   e si i = i' et j = j'
#                   getIJème(mat, i, j) sinon

class Matrice:

    # créerMatrice : Entier x Entier → Matrice
    def __init__(self, n, m):
        assert n > 0, "le nombre de lignes de la matrice doit être positif"
        assert m > 0, "le nombre de colonnes de la matrice doit être positif"
        self._n = n + 1
        self._m = m + 1
        self._elements = []
        for i in range(self._n):
            ligne = []
            if i==0 :
                ligne.append("  ")
            else :
                ligne.append("N"+str(i))
            for j in range(1,self._m):
                if i==0 :
                    ligne.append("N"+str(j))
                else :
                    ligne.append(0)
            self._elements.append(ligne)

    # nbLignes : Matrice → Entier
    def nbLignes(self):
        return self._n -1

    # nbColonnes : Matrice → Entier
    def nbColonnes(self):
        return self._m -1

    # getIJème : Matrice x Entier x Entier → Entier
    def getIJeme(self, i, j):
        assert 0 < i <= self._n  , "l'indice des lignes n'est pas valide"
        assert 0 < j <= self._m  , "l'indice des colonnes n'est pas valide"
        return self._elements[i][j]

    # setIJème : Matrice x Entier x Entier x Entier → Matrice
    def setIJeme(self, i, j, e):
        assert 1 <= i < self._n , "l'indice des lignes n'est pas valide"
        assert 1 <= j < self._m , "l'indice des colonnes n'est pas valide"
        self._elements[i][j] = e
        # self._elements[j][i] = e # si graphe non orienté

    # retourne une chaine de caractères représentative de l'état de l'instance
    def __str__(self):
        return str(self._elements)

    # donne le schéma de construction de l'instance
    def __repr__(self):
        return "Matrice(" + str(self._n) + "," + str(self._m) + ")"

    # test d'égalité de deux matrices
    def __eq__(self, mat):
        return self._n == mat._n and self._m == mat._m and self._elements == mat._elements

    # affiche l'instance sous une forme matricielle
    def dump(self):
        for i in range(self._n):
            for j in range (self._n):
                if i==0 :
                    print(self._elements[i][j],"",end="")
                else :                    
                    print(self._elements[i][j]," ",end="")
            print("")
     
        
    def draw(self,g):
        c = graphviz.Digraph(strict=False) # orienté
        # c = graphviz.Graph(strict=True) #non orienté
        for i in range (1,len(self._elements)):
            for j in range (1,len(self._elements[i])):
                if self._elements[i][j] == 1 :
                    c.edge(str(i),str(j))
        name = g + '.gv'
        c.render(name, view=True) # fermer le lecteur pdf avant de relancer le code python

if __name__ == "__main__":
    M = Matrice(5,5)
    M.setIJeme(1,2,1)
    M.setIJeme(1,5,1)
    M.setIJeme(2,3,1)
    M.setIJeme(2,4,1)
    M.setIJeme(2,5,1)
    M.setIJeme(3,4,1)
    M.setIJeme(4,5,1)
    M.dump()
    M.draw("M")


    
    

