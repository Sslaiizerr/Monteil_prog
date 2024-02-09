# VÃ©rifiez vos import !
from SujetListeAdj import ListeAdj


# Graphes de tests

def construireGrapheG2():
    g = ListeAdj(5)
    g.ajoutArete(1, 5)
    g.ajoutArete(2, 1)
    g.ajoutArete(2, 4)
    g.ajoutArete(3, 2)
    g.ajoutArete(4, 3)
    g.ajoutArete(5, 2)
    g.ajoutArete(5, 4)
    return g


def construireGrapheG3():
    g = ListeAdj(6)
    g.ajoutArete(1, 3)
    g.ajoutArete(1, 4)
    g.ajoutArete(1, 5)
    g.ajoutArete(1, 6)
    g.ajoutArete(2, 1)
    g.ajoutArete(3, 2)
    g.ajoutArete(3, 4)
    g.ajoutArete(6, 4)
    return g

# -------------------------------------------------------
# PARCOURS
# -------------------------------------------------------

# {parcours en largeur du graphe G à partir du sommet i ex:largeur(g2, 1))}


def largeur(g, i):  # largeur(G,x) :
    # print("à compléter !")
    # visite = [False, False, False, False] ## Nombre de sommets
    visite = [False] * [g.nbSommets() + 1]
    F = [i]
    ordre_de_visite = [i]


# -----------------------------------------------------------

# parcours du graphe g en profondeur Ã  partir de son sommet i

# profRec(G,i,Visite,ordreVisite) :
# fonction auxiliaire récursive qui provoque un parcours en profondeur du graphe à partir du sommet i.
# Cette fonction ne retourne aucun résultat et se contente de mettre à jour les paramètres Visite et ordreVisite.
# profond(G,x) : {parcours en profondeur du graphe G à partir du sommet i}


def profondeurPremiereVisite(g, i):  # profondeurPremiereVisite(g2, 1)
    # print("à compléter !")
    pass


def profondeurRecPremiereVisite(g, i, Visite, ordreVisite):
    # print("à compléter !")
    pass


# -----------------------------------------------------
"""
Les fonctions profondeurRecPremiereVisite et profondeurRecDerniereVisite
sont identiques Ã  un seul dÃ©tail prÃ¨s : la position de la ligne 
ordreVisite.append(i)
Les fonctions profondeurPremiereVisite et profondeurDerniereVisite
sont identiques (sauf qu'elles n'appellent pas la mÃªme fonction auxiliaire Ã©videmment !)
"""


def profondeurDerniereVisite(g, i):
    Visite = [False] * (g.nbAretes()+1)  # initialiser un tableau Visite à Faux
    Visite[i] = True  # Visite[x] = Vrai
    ordreVisite = []  # {premiŁre visite de i}
    # ordreVisite.append(i)
    Visite, ordreVisite = profondeurRecDerniereVisite(
        g, i, Visite, ordreVisite)
    ordreVisite.append(i)
    return ordreVisite


def profondeurRecDerniereVisite(g, i, Visite, ordreVisite):
    for y in g.getAretesSommet(i):  # Pour chaque voisin y de x faire
        if Visite[y] == False:  # Si Visite[y] = faux alors profond(G,y)
            Visite[y] = True
            # ordreVisite.append(i)
            Visite, ordreVisite = profondeurRecPremiereVisite(
                g, y, Visite, ordreVisite)
            ordreVisite.append(y)
    return Visite, ordreVisite


# -----------------------------------------------------
# POUR TESTER VOS FONCTIONS
if __name__ == '__main__':
    # construire et parcourir le graphe g2
    g2 = construireGrapheG2()
    # g2.draw("g2")
    # construire et parcourir le graphe g3
    g3 = construireGrapheG3()
    # g3.draw("g3")
    # print("parcours du graphe G2 en largeur : " + str(largeur(g2, 1)))
    # print("parcours du graphe G3 en largeur : " + str(largeur(g3, 1)))
    # print("parcours du graphe G2 en profondeur (première visite) : " + str(profondeurPremiereVisite(g2, 1)))
    # print("parcours du graphe G3 en profondeur (première visite) : " + str(profondeurPremiereVisite(g3, 1)))
    print("parcours du graphe G2 en profondeur (dernière visite) : " +
          str(profondeurDerniereVisite(g2, 1)))
    print("parcours du graphe G3 en profondeur (dernière visite) : " +
          str(profondeurDerniereVisite(g3, 1)))
