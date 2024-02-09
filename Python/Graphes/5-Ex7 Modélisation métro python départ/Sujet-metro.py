# VÃ©rifiez vos import !
from SujetListeAdj import ListeAdj


# Graphes de tests

# ---------------------------------------------------
# Pour tester vos fonctions

def construireGrapheG_metro():
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
    # print("à compléter !")

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
  
    # plus Courts Chemins dans le graphe g1
    g_metro = construireGrapheG_metro()
    #g_metro.drawNonOriente("g_metro")
    # tab_nom_court = [[],"Aé","Ar","CC","DS" ," Es" ,"FC" ,"FV" ,"JA","JJ" ,"PJ" ,"Pu" ,"Zé" ]
    # g_metro.drawNonOriente_nommé("g_metro_nommé_court",tab_nom_court)
    # tab_nom_long = [[],"Aéroport","Arènes","Compans-Caffarelli","Déodat de Sévérac" ,"Esquirol" ,"Fer à Cheval" ,"François Verdier" ,"Jeanne d’Arc","Jean Jaurès" ,"Palais de Justice" ,"Purpan" ,"Zénith" ]
    # g_metro.drawNonOriente_nommé("g_metro_nommé_long",tab_nom_long)
    tab_nom_long_num = [[],"1-Aéroport","2-Arènes","3-Compans-Caffarelli","4-Déodat de Sévérac" ,"5-Esquirol" ,"6-Fer à Cheval" ,"7-François Verdier" ,"8-Jeanne d’Arc","9-Jean Jaurès" ,"10-Palais de Justice" ,"11-Purpan" ,"12-Zénith" ]
    # g_metro.drawNonOriente_nommé("g_metro_nommé_long_num",tab_nom_long_num)
    distG1, pereG1 = plusCourtChemin(g_metro, 1) # plus court départ station 1-Aéroport
    # print("distance du sommet 1 au sommet: [1, 2, 3, 4, 5, 6, 7 ,8, 9,10,11,12]")
    # print("       la distance est égal à :",distG1 )
    # print(" ")
    # print("le père du sommet: [1,  2, 3, 4, 5, 6, 7, 8, 9,10,11, 12]")
    # print("   est le sommet :",pereG1 )
    # print("le nbre minimal de station de 1-Aéroport à 10-Palais de Justice est de" ,distance_nb_station(distG1,10),"stations")  # distance_nb_stations(distg1,station de destination)
    # print(" ")
    # print("dans ce cas parcourir les stations dans l'ordre suivants",chemin_plus_court(pereG1,1,10,tab_nom_long_num ))


    
    
    
    
    
    
    
    
    
    
    
    
    
    