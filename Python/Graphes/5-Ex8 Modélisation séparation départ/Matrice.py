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


import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python



class Matrice:

    # créerMatrice : Entier x Entier → Matrice
    def __init__(self, n, m):
        assert n > 0, "le nombre de lignes de la matrice doit être positif"
        assert m > 0, "le nombre de colonnes de la matrice doit être positif"
        self._n = n+1
        self._m = m+1
        self._elements = []
        for i in range(self._n):
            ligne = []
            for j in range(self._m):
                ligne.append(0)
            self._elements.append(ligne)

    # nbLignes : Matrice → Entier
    def nbLignes(self):
        return self._n-1

    # nbColonnes : Matrice → Entier
    def nbColonnes(self):
        return self._m-1

    # getIJème : Matrice x Entier x Entier → Entier
    def getIJeme(self, i, j):
        assert 0 <= i < self._n, "l'indice des lignes n'est pas valide"
        assert 0 <= j < self._m, "l'indice des colonnes n'est pas valide"
        return self._elements[i][j]

    # setIJème : Matrice x Entier x Entier x Entier → Matrice
    def setIJeme(self, i, j, e):
        assert 0 <= i < self._n, "l'indice des lignes n'est pas valide"
        assert 0 <= j < self._m, "l'indice des colonnes n'est pas valide"
        self._elements[i][j] = e

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
            # print(self._elements[i])
            for j in range(len(self._elements[i])):
                if i != 0 and not j==0:
                    print("  ",end='  ')
                print(self._elements[i][j],end=' ')
            print("")
    
    def draw(self):
        c = graphviz.Graph(strict=True) # ne trace pas les arêtes en double (non orienté)
        for i in range (1,len(self._elements)):
            for j in range (1,len(self._elements[i])):
                if self._elements[i][j] == 1 :
                    c.edge(self.getIJeme(0,i),self.getIJeme(0,j))
        c.render('round-table3.gv', view=True) # fermer le lecteur pdf avant de relancer le code python

def matrice_etiquettes(larg,long,Tab_act):
    M = Matrice(larg,long) # taille de la matrice
    for i in range (larg+1) : # définitin des étiquettes
        #print(i)
        for j in range (long+1) :
            # print("   ",j,Tab_act[j])
            if i ==0 and j == 0 :
                M.setIJeme(0,j,Tab_act[0])
            if i==0 :
                M.setIJeme(0,j,Tab_act[j])
            if j==0 :
                M.setIJeme(i,0,Tab_act[i])
    # définition des relations
    M.setIJeme(1,4,1)
    M.setIJeme(4,1,1)
    M.setIJeme(1,5,1)
    M.setIJeme(5,1,1)
    M.setIJeme(1,10,1)
    M.setIJeme(10,1,1)
    M.setIJeme(2,7,1)
    M.setIJeme(7,2,1)
    M.setIJeme(2,9,1)
    M.setIJeme(9,2,1)
    M.setIJeme(3,5,1)
    M.setIJeme(5,3,1)
    M.setIJeme(3,6,1)
    M.setIJeme(6,3,1)
    M.setIJeme(4,7,1)
    M.setIJeme(7,4,1)
    M.setIJeme(5,7,1)
    M.setIJeme(7,5,1)
    M.setIJeme(6,9,1)
    M.setIJeme(9,6,1)
    M.setIJeme(8,9,1)
    M.setIJeme(9,8,1)
    M.setIJeme(8,10,1)
    M.setIJeme(10,8,1)
    return M

def construireMatrice():
    m = Matrice(5, 5)
    m.setIJeme(0, 1, 1)
    m.setIJeme(0, 4, 1)
    m.setIJeme(1, 0, 1)
    m.setIJeme(1, 2, 1)
    m.setIJeme(1, 3, 1)
    m.setIJeme(1, 4, 1)
    m.setIJeme(2, 1, 1)
    m.setIJeme(2, 3, 1)
    m.setIJeme(3, 1, 1)
    m.setIJeme(3, 2, 1)
    m.setIJeme(3, 4, 1)
    m.setIJeme(4, 0, 1)
    m.setIJeme(4, 1, 1)
    m.setIJeme(4, 3, 1)
    return m

            
if __name__ == "__main__":
    # List_act = étiquettesnuméroté des lignes et colonnes
    List_act=["  ACT"," 1-GC"," 2-OS"," 3-AD"," 4-JD"," 5-VC"," 6-AT"," 7-EC"," 8-MS"," 9-TH","10-AK"]
    M = matrice_etiquettes(10,10,List_act) # matrice_etiquettes(larg,long,List_act):

    #print(M)
    M.dump()
    M.draw()
    print(M.nbLignes())
    
    



    
    
    
    
    
