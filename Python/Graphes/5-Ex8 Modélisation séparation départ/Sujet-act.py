# VÃ©rifiez vos import !
from SujetListeAdj import ListeAdj
from Matrice import Matrice
import graphviz #cmd exécuter en tant qu’admin et lancer conda install python-graphviz
# fermer le lecteur pdf avant de relancer le code python

# Graphes de tests

# ---------------------------------------------------
# Pour tester vos fonctions

def matrice_etiquettes(larg,long,Tab_act):
    M = Matrice(larg,long) # taille de la matrice
    for i in range (larg+1) : # définition des étiquettes
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
    # print("à compléter !")  
    # M.setIJeme(i,j,1)


def mat_to_liste(M_L): # matrice vers graphe (matToListe)
    listA = ListeAdj(M_L.nbLignes())
    for i in range(1,M_L.nbLignes()+1) :
        # print(M_L[i])
        for j in range (1,M_L.nbLignes()+1):
            # print(M_L[i][j])
            if M_L.getIJeme(i, j) == 1 :
                listA.ajoutArete(i,j)
    return listA

def construireGrapheG_act():
    # print("à compléter !")


def dist_moyenne(dist):
    # print(dist)
    # print("à compléter !")


# -------------------------------------------------------
# PARCOURS
# -------------------------------------------------------

# {parcours en largeur du graphe G à partir du sommet i ex:largeur(g2, 1))}
def largeur(g, i): # largeur(G,x) : 
    tab_viste = [False] * (g.nbAretes()+1) # initialiser un tableau Visite à Faux
    Visite  = [False] * (g.nbAretes()+1)
    F = [i] # F = [x]
    ordreVisite = [i] # enregistrement sous forme de liste des sommets visités par parcours_largeur
    Visite[i] = True  # Visite[i] = vrai
    while F != [] : # Tant que F n’est pas vide
        y= F[0]
        del F[0] # considérer y= F[0]  la t€te de F (et l’enlever de F)
        for z in g.getAretesSommet(y) : # pour chaque successeur z de y
            if Visite[z] == False : # Si visite[z] = faux
                Visite[z] = True # Visite[z] = vrai
                F.append(z) # ajouter z à la fin de la file F
                ordreVisite.append(z) # enregistrement sous forme de liste des sommets visités par parcours_largeur
    return ordreVisite # retour de liste des sommets visités par parcours_largeur

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
    return Dist, Pere # retourne les vecteurs Dist et Pere donnant les plus courts chemins issus du sommet i.

                
# -----------------------------------------------------------

# parcours du graphe g en profondeur Ã  partir de son sommet i

# profRec(G,i,Visite,ordreVisite) : 
# fonction auxiliaire récursive qui provoque un parcours en profondeur du graphe à partir du sommet i. 
# Cette fonction ne retourne aucun résultat et se contente de mettre à jour les paramètres Visite et ordreVisite.
def profondeurRecPremiereVisite(g,i,Visite,ordreVisite) :
    for y in g.getAretesSommet(i) : # Pour chaque voisin y de x faire
        if Visite[y] == False: # Si Visite[y] = faux alors profond(G,y)
            Visite[y] = True
            ordreVisite.append(y)
            Visite,ordreVisite = profondeurRecPremiereVisite(g,y,Visite,ordreVisite)
    return Visite,ordreVisite

# profond(G,x) : {parcours en profondeur du graphe G à partir du sommet i}
def profondeurPremiereVisite(g,i) : # profondeurPremiereVisite(g2, 1)
    Visite  = [False] * (g.nbAretes()+1) # initialiser un tableau Visite à Faux
    Visite[i] = True # Visite[x] = Vrai
    ordreVisite = [] 
    ordreVisite = [i] # {premiŁre visite de i}
    Visite,ordreVisite = profondeurRecPremiereVisite(g,i,Visite,ordreVisite)
    return ordreVisite



           



# -----------------------------------------------------
"""
Les fonctions profondeurRecPremiereVisite et profondeurRecDerniereVisite
sont identiques Ã  un seul dÃ©tail prÃ¨s : la position de la ligne 
ordreVisite.append(i)
Les fonctions profondeurPremiereVisite et profondeurDerniereVisite
sont identiques (sauf qu'elles n'appellent pas la mÃªme fonction auxiliaire Ã©videmment !)
"""

def profondeurRecDerniereVisite(g,i,Visite, ordreVisite) :
    for y in g.getAretesSommet(i) : # Pour chaque voisin y de x faire
        if Visite[y] == False: # Si Visite[y] = faux alors profond(G,y)
            Visite[y] = True
            Visite,ordreVisite = profondeurRecPremiereVisite(g,y,Visite,ordreVisite)
            ordreVisite.append(y)
    return Visite,ordreVisite

def profondeurDerniereVisite(g,i) :
    Visite  = [False] * (g.nbAretes()+1) # initialiser un tableau Visite à Faux
    Visite[i] = True # Visite[x] = Vrai
    ordreVisite = [] # {premiŁre visite de i}
    Visite,ordreVisite = profondeurRecDerniereVisite(g,i,Visite,ordreVisite)
    ordreVisite.append(i)
    return ordreVisite

def distance_nb_station(tab_dist,dest) : # distance_nb_stations(distg1,station de destination)
    return tab_dist[dest-1]

def chemin_plus_court(pere,dep,arr,tab_nom) : #chemin_plus_court(tab_père,depart,arrivée)
    chemin = []
    while arr != dep :
        #chemin.append(arr)
        chemin.append(tab_nom[arr])
        # print(arr)
        arr = pere[arr-1]
    #chemin.append(arr)
    chemin.append(tab_nom[arr])
    chemin.reverse()
    return chemin


# -----------------------------------------------------
# POUR TESTER VOS FONCTIONS

if __name__ == '__main__':
  
    # plus Courts Chemins dans le graphe
    List_act=["  ACT"," 1-GC"," 2-OS"," 3-AD"," 4-JD"," 5-VC"," 6-AT"," 7-FC"," 8-MS"," 9-TH","10-AK"]
    #M = matrice_etiquettes(10,10,List_act) # matrice_etiquettes(larg,long,List_act):
    #M.dump()
    #M.draw()
    #G=mat_to_liste(M)
    #G.drawNonOriente_nommé("M_L",List_act)
    g_act= construireGrapheG_act()
    #g_act.drawNonOriente_nommé("g_acteurs",List_act)
    #distG1, pereG1 = plusCourtChemin(g_act, 1) # plus court chemin depuis George Clooney 
    #print("degré de séparation du sommet 1 au sommet: [1, 2, 3, 4, 5, 6, 7 ,8, 9,10]")
    #print("                              est égal à :",distG1 )
    #print(" ")
    #print("le père du sommet: [1, 2, 3, 4, 5, 6, 7,  8, 9,10]")
    #print("   est le sommet :",pereG1 )
    #print("la distance moyenne = ",dist_moyenne(distG1))

    
    
    
    
    
    
    
    
    
    
    
    
    
    