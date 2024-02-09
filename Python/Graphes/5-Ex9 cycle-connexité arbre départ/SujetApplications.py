from SujetListeAdj import ListeAdj


# -------------------------------------------------------------------
# tester la connexité d'un graphe à l'aide d'un parcours en largeur

def estConnexe(g):
# {le graphe g est connexe si et seulement si un parcours à partir de 1 visite tous les sommets}
    #print("à compléter !")

# --------------------------------------------------
# tester l'existence d'un cycle
def estCyclique(g):
    #print("à compléter !")

# --------------------------------------------------
# test arbre

def estArbre(g):
    #print("à compléter !")

# --------------------------------------------------
# Plus courts chemins à l'aide d'un parcours en largeur

def plusCourtChemin(g, i): # distG1, pereG1 = plusCourtChemin(g1, 1)
    trouve = False # trouvé = Faux
    Visite  = [False] * (g.nbAretes()+1) # initialiser un tableau Visite à Faux
    Dist = [g.nbSommets()] * (g.nbSommets()) # initialiser un tableau Dist à l’infini supérieur n sommet +1
    Pere = [-1] * (g.nbSommets())  # initialiser un tableau Pere à l’infini supérieur n sommet +1 
    F = [i] # F = [x]
    ordreVisite = [i] # enregistrement sous forme de liste des sommets visités par parcours_largeur
    Visite[i] = True  # Visite[i] = vrai
    Dist[i-1] = 0 # Dist[i] = 0
    Pere[i-1] = i # Pere[i] = i
    # print("sommet visité :",i)
    while F != [] : # Tant que F n’est pas vide
        y= F[0]
        del F[0] # considérer y= F[0]  la t€te de F (et l’enlever de F)
        for z in g.getAretesSommet(y) : # pour chaque successeur z de y
            # print("sommet visité :",z)
            if Visite[z] == False: # Si visite[z] = faux
                Visite[z] = True # Visite[z] = vrai
                F.append(z) # ajouter z à la fin de la file F
                ordreVisite.append(z) # enregistrement sous forme de liste des sommets visités par parcours_largeur
                Dist[z-1] = Dist[y-1] + 1
                Pere[z-1] = y
            # elif z==i :
            #    Pere[z-1] = y
    return Dist, Pere # retourne les vecteurs Dist et Pere donnant les plus courts chemins issus du sommet i.


# ---------------------------------------------------
# Pour tester vos fonctions

def construireGrapheG1():
    g = ListeAdj(5,False) # True si arbre orienté
    g.ajoutArete(1, 5)
    g.ajoutArete(2, 1)
    g.ajoutArete(2, 4)
    g.ajoutArete(3, 2)
    g.ajoutArete(4, 3)
    g.ajoutArete(5, 2)
    g.ajoutArete(5, 4)
    return g


# G1 est connexe et admet un cycle

def construireGrapheG2():  
    g = ListeAdj(5,False) # True si arbre orienté
    g.ajoutArete(1, 5)
    g.ajoutArete(2, 1)
    g.ajoutArete(4, 3)
    return g


# G2 n'est pas connexe, et n'admet pas non plus de cycle

def construireGrapheG3():
    g = ListeAdj(5, False) # True si arbre orienté
    g.ajoutArete(1, 5)
    g.ajoutArete(2, 1)
    g.ajoutArete(1, 3)
    g.ajoutArete(4, 3)
    return g


# G3 est connexe, mais n'a pas de cycle

if __name__ == '__main__':
    # construction des graphes
    
    g1 = construireGrapheG1()
    #g1.draw("g1")
    #print(estConnexe(g1))
    # test  connexité
    # assert estConnexe(g1)," Erreur l'abre G1 est connexe "
    
    g2 = construireGrapheG2()
    #g2.draw("g2")
    #print(estConnexe(g2))
    # test  connexité
    # assert not estConnexe(g2)," Erreur l'abre G2 n'est pas connexe "
    
    g3 = construireGrapheG3()
    # g3.draw("g3")
    #print(estConnexe(g3))
    # test  connexité
    # assert estConnexe(g3)," Erreur l'abre G3 est connexe "    

    # test existence d'un cycle
    #print(estCyclique(g1))
    #assert estCyclique(g1), " Erreur l'abre G1 contient au moins 1 cycle "
    #print(estCyclique(g2))
    #assert not estCyclique(g2),  " Erreur l'abre G2 ne contient pas de cycle "
    #print(estCyclique(g3))
    #assert not estCyclique(g3),  " Erreur l'abre G3 ne contient pas de cycle "

    # test être un arbre
    #print(estArbre(g1))
    #assert not estArbre(g1), " Erreur l'abre G1 n'est pas un arbre"
    #print(estArbre(g2))
    #assert not estArbre(g2), " Erreur l'abre G2 n'est pas un arbre"
    #print(estArbre(g3))
    #assert estArbre(g3), " Erreur l'abre G3 est un arbre"






