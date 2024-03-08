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
    # initialiser un tableau Visite à Faux
    Visite = [False] * (g.nbSommets()+1)
    F = [i]  # F = [x]
    # enregistrement sous forme de liste des sommets visités par parcours_largeur
    ordreVisite = [i]
    Visite[i] = True  # Visite[i] = vrai
    while F != []:  # Tant que F n’est pas vide
        y = F[0]
        print(y)  # sommet(visité)
        del F[0]  # considérer y= F[0]  la t€te de F (et l’enlever de F)
        for z in g.getAretesSommet(y):  # pour chaque successeur z de y
            if Visite[z] == False:  # Si visite[z] = faux
                Visite[z] = True  # Visite[z] = vrai
                # print(Visite)
                F.append(z)  # ajouter z à la fin de la file F
                print(F)
                # enregistrement sous forme de liste des sommets visités par parcours_largeur
                ordreVisite.append(z)
                print(ordreVisite)
                print("")
            else:
                print(z, "déjà visité")
                print("")
    return ordreVisite  # retour de liste des sommets visités par parcours_largeur

# Plus courts chemins à l'aide d'un parcours en largeur


def plusCourtChemin(g, i):  # distG1, pereG1 = plusCourtChemin(g1, 1)
    # print("à compléter !")
    Visite = [False] * (g.nbAretes()+1)  # initialiser un tableau Visite à Faux
    # initialiser un tableau Dist à l’infini supérieur n sommet +1
    Dist = [g.nbSommets()] * (g.nbSommets())
    # initialiser un tableau Pere à l’infini supérieur n sommet +1
    Pere = [-1] * (g.nbSommets())
    F = [i]  # F = [x]
    # enregistrement sous forme de liste des sommets visités par parcours_largeur
    ordreVisite = [i]
    Visite[i] = True  # Visite[i] = vrai
    Dist[i-1] = 0  # Dist[i] = 0
    Pere[i-1] = i  # Pere[i] = i
    print("sommet visité :", i)
    while F != []:  # Tant que F n’est pas vide
        y = F[0]
        del F[0]  # considérer y= F[0]  la t€te de F (et l’enlever de F)
        for z in g.getAretesSommet(y):  # pour chaque successeur z de y
            print("sommet visité :", z)
            if Visite[z] == False:  # Si visite[z] = faux
                Visite[z] = True  # Visite[z] = vrai
                F.append(z)  # ajouter z à la fin de la file F
                # enregistrement sous forme de liste des sommets visités par parcours_largeur
                ordreVisite.append(z)
                Dist[z-1] = Dist[y-1] + 1
                Pere[z-1] = y
            elif z == i:
                Pere[z-1] = y
    # retourne les vecteurs Dist et Pere donnant les plus courts chemins issus du sommet i.
    return Dist, Pere

# -----------------------------------------------------------

# parcours du graphe g en profondeur Ã  partir de son sommet i

# profRec(G,i,Visite,ordreVisite) :
# fonction auxiliaire récursive qui provoque un parcours en profondeur du graphe à partir du sommet i.
# Cette fonction ne retourne aucun résultat et se contente de mettre à jour les paramètres Visite et ordreVisite.
# profond(G,x) : {parcours en profondeur du graphe G à partir du sommet i}


def profondeurPremiereVisite(g, i):  # profondeurPremiereVisite(g2, 1)
    Visite = [False] * (g.nbAretes()+1)  # initialiser un tableau Visite à Faux
    Visite[i] = True  # Visite[x] = Vrai
    ordreVisite = []
    ordreVisite.append(i)  # {première visite de i}
    Visite, ordreVisite = profondeurRecPremiereVisite(
        g, i, Visite, ordreVisite)
    return ordreVisite


def profondeurRecPremiereVisite(g, i, Visite, ordreVisite):
    for y in g.getAretesSommet(i):  # Pour chaque voisin y de x faire
        if Visite[y] == False:  # Si Visite[y] = faux alors profond(G,y)
            Visite[y] = True
            ordreVisite.append(y)
            Visite, ordreVisite = profondeurRecPremiereVisite(
                g, y, Visite, ordreVisite)
    return Visite, ordreVisite


# -----------------------------------------------------
"""
Les fonctions profondeurRecPremiereVisite et profondeurRecDerniereVisite
sont identiques Ã  un seul dÃ©tail prÃ¨s : la position de la ligne 
ordreVisite.append(i)
Les fonctions profondeurPremiereVisite et profondeurDerniereVisite
sont identiques (sauf qu'elles n'appellent pas la mÃªme fonction auxiliaire Ã©videmment !)
"""


def profondeurDerniereVisite(g, i):
    # print("à compléter !")
    Visite = [False] * (g.nbAretes()+1)  # initialiser un tableau Visite à Faux
    Visite[i] = True  # Visite[x] = Vrai
    ordreVisite = []  # {premiŁre visite de i}
    # ordreVisite.append(i)
    Visite, ordreVisite = profondeurRecDerniereVisite(
        g, i, Visite, ordreVisite)
    ordreVisite.append(i)
    return ordreVisite


def profondeurRecDerniereVisite(g, i, Visite, ordreVisite):
    # print("à compléter !")
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
    # plus Courts Chemins dans le graphe g1
    g2 = construireGrapheG2()
    distG2, pereG2 = plusCourtChemin(g2, 1)
    print("distance du sommet 1 au sommet: [1, 2, 3, 4, 5]")
    print("       la distance est égal à :", distG2)
    print(" ")
    print("le père du sommet: [1, 2, 3, 4, 5]")
    print("   est le sommet :", pereG2)
    # g1.draw("g1")
    assert distG2 == [
        0, 2, 3, 2, 1], "Le vecteur des distances n'est pas correctement rempli"
    assert pereG2 == [1, 5, 4, 5,
                      1], "Le vecteur des pères n'est pas correctement rempli"
