from Tableau import Tableau
from Matrice import Matrice

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

def mat_to_liste(M_L): # matrice vers graphe (matToListe)
    listA = ListeAdj(M_L.nbLignes())
    for i in range(1,M_L.nbLignes()+1) :
        # print(M_L[i])
        for j in range (1,M_L.nbLignes()+1):
            # print(M_L[i][j])
            if M_L.getIJeme(i, j) == 1 :
                listA.ajoutArete(i,j)
    return listA

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
    
if __name__ == "__main__":
    # List_act = étiquettesnuméroté des lignes et colonnes
    List_act=["  ACT"," 1-GC"," 2-OS"," 3-AD"," 4-JD"," 5-VC"," 6-AT"," 7-EC"," 8-MS"," 9-TH","10-AK"]
    M_acteurs = matrice_etiquettes(10,10,List_act) # matrice_etiquettes(larg,long,List_act):
    M_acteurs.dump()
    #M.draw()
    #List_adj_act = mat_to_liste(M_acteurs)
    #M_acteurs.draw("M_acteurs")
    #print(List_adj_act)
    #List_adj_act.drawNonOriente("List_adj_act")
    #List_adj_act.drawNonOriente_nommé("List_adj_act",List_act)
    
    """
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
    """
     