def affichage_position(pos_chaine, present, motif, chaine):
    if present:
        if len(pos_chaine) == 1:
            print("la position du motif", motif, "est :", pos_chaine)
            print("affichage de la chaine : ", end='')
            print(chaine[0:pos_chaine[0]], motif,
                  chaine[pos_chaine[0]+len(motif):])
            print()
        else:
            print("les", len(pos_chaine), "positions du motif",
                  motif, "sont :", pos_chaine)
            print("affichage de la chaine : ", end='')
            print(chaine[0:pos_chaine[0]], end='')
            for i in range(len(pos_chaine)-1):
                # print(i)
                print(motif, chaine[pos_chaine[i]+len(motif):pos_chaine[i+1]], " ", end='')
            print(motif, chaine[pos_chaine[i]+len(motif):])
    else:
        print("le motif n'est pas présent dans la chaîne")
        print()


# algorithme Boyer Moore recherche modif dans un texte algo_boyerMore(texte,motif):
def algo_boyerMore(texte, motif):
    # Initialisation des variables
    # print("à compléter !")
    # longTexte =
    # longMotif =
    # resultat =
    # present =
    # decalage =
    # monDico =

    # Pré traitement du motif
    # print("à compléter !")
    # print(monDico)

    # à supprimer (départ)
    for i in range(longMotif):  # Pour i de 0 à longMotif :
        c = motif[i]
        if c in monDico:  # Si c appartient monDico :
            monDico[c].append(i)  # ajouter i dans la liste monDico[c]
        else:  # Sinon
            monDico[c] = [i]
    # print(monDico)

    # On cherche TOUTES les occurrences du motif dans le texte
    # Donc TANT qu’on n’est pas arrivé à la fin du texte :
    while decalage <= longTexte - longMotif:
        # Je fais la comparaison de droite à gauche
        iMotif = longMotif - 1  # position des caratères comparés
        while iMotif >= 0 and motif[iMotif] == texte[decalage + iMotif]:
            iMotif = iMotif - 1
        # print("position à droite du motif=",iMotif)
        # print("décalage =",decalage)
        # print()

        # La comparaison aboutit
        if iMotif < 0:
            resultat.append(decalage)
            present = True
            # Ai-je encore la possibilité de trouver le motif dans le texte
            # ou suis-je arrivée à la fin du texte ?
            if decalage < longTexte - longMotif:
                # Je calcule le nouveau décalage
                # en observant la première lettre qui suit le motif trouvé dans le texte
                car = texte[decalage+longMotif]
                if car in motif:
                    # j’aligne car avec sa dernière occurrence dans motif
                    # print(car)
                    # rint(monDico[car])
                    # print(decalage)
                    indice = monDico[car][-1]
                    # print(indice)
                    decalage = decalage + (longMotif - indice)
                    # print(decalage)
                    # print("")
                else:
                    # je peux décaler directement de toute la longueur du motif
                    decalage = decalage + longMotif
            else:  # j’ai terminé l’étude du texte
                decalage = decalage + 1
                # entraine la sortie de la boucle while principale

        # La comparaison n’a pas aboutit
        else:
            # Le caractère qui n’a pas satisfait la comparaison
            car = texte[decalage + iMotif]
            if car in motif:
                # J’aligne car avec l’occurence pertinente de car dans motif
                # print("position caractère = ",monDico[car],"position à droite du motif=",iMotif," ",end=""),
                # indice = plusGrand(monDico[car]), inférieur(iMotif)
                indice = -1
                for val in monDico[car]:
                    if val < iMotif:
                        indice = val
                # indice = min(min(monDico[car]),iMotif)
                # print("indice =", indice,"car = ",car,end=" ")
                # comme son nom l’indique, plusGrandInferieur(L,x) cherche le
                # plus grand entier appartenant à la liste L inférieur à x
                decalage = decalage + iMotif - indice
                # print("décalage suivant",decalage)
                # print("")
            else:
                # je peux décaler directement de toute la longueur du motif
                decalage = decalage + iMotif + 1

    return resultat, present


motif1 = "CGGCAG"
chaine1 = "CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGG"
position1, presence1 = algo_boyerMore(chaine1, motif1)
print(position1, presence1)
affichage_position(position1, presence1, motif1, chaine1)

motif2 = "CA"
chaine2 = "CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGG"
position2, presence2 = algo_boyerMore(chaine2, motif2)
print(position2, presence2)
affichage_position(position2, presence2, motif2, chaine2)
