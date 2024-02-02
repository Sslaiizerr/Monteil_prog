from SujetListeAdj import ListeAdj
from Matrice import Matrice

# import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python


# -----------------------------------------------
# CONVERSIONS ENTRE LES REPRESENTATIONS

def listeToMatrice(liste): # liste à convertir
    #print("à compléter !")

def areteToListe(n, l):  # nbre de sommet, liste des aretes à convertir,
    #print("à compléter !")

def matToListe(M_L):
    #print("à compléter !")

def A_liste_A():
    A = ListeAdj(5)
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
    return A

def M_matrice():
    M = Matrice(5,5)
    M.setIJeme(1,2,1)
    M.setIJeme(1,5,1)
    M.setIJeme(2,1,1)
    M.setIJeme(2,3,1)
    M.setIJeme(2,4,1)
    M.setIJeme(2,5,1)
    M.setIJeme(3,2,1)
    M.setIJeme(3,4,1)
    M.setIJeme(4,2,1)
    M.setIJeme(4,3,1)
    M.setIJeme(4,5,1)
    M.setIJeme(5,1,1)
    M.setIJeme(5,2,1)
    M.setIJeme(5,4,1)
    return M

if __name__ == "__main__":
    

    # Test ListeAdj
    A = A_liste_A()
    print(A)
    A.draw("list-A") # fermer le lecteur pdf avant de relancer le code python
    # Fin Test ListeAdj

    
    """
    # Test Matrice
    M = Matrice(5,5)
    print(M) 
    M.dump()
    M.draw("Matrice_M")
    # Fin Test Matrice

    

    # Test listeToMatrice
    A = A_liste_A()
    print(A)
    MB = listeToMatrice(A)
    MB.dump()
    # Fin Test listeToMatrice


    # Test arete_To_Liste
    L = [    [1,2],[1,5],
             [2,1],[2,3],[2,4],[2,5],
             [3,2],[3,4],
             [4,2],[4,3],[4,5],
             [5,1],[5,2],[5,4]
        ]
    ListeAdj = areteToListe(5,L)
    print(ListeAdj)
    ListeAdj.draw("Arete_Liste")
    # Fin Test arete_To_Liste
 
    
    # Test mat_to_liste
    M = [   ["  ","N1","N1","N3","N4","N5"],
            ["N1",   0,   1,   0,   0,   1],   
            ["N2",   1,   0,   1,   1,   1], 
            ["N3",   0,   1,   0,   1,   0], 
            ["N4",   0,   1,   1,   0,   1], 
            ["N5",   1,   1,   0,   1,   0]
        ]
    

    print(M)
    ListeAdj = matToListe(M)
    print(ListeAdj)
    ListeAdj.draw("liste-g")
    # Fin Test mat_to_liste
    
    """
