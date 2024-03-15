def algo_naif(motif, chaine):
    pos_chaine = []
    present = False
    for j in range(len(chaine)-len(motif)+1):  # pour chaque lettre de la chaine
        i = 0
        # comparer chaque lettre suivante de la chaine au motif
        while i < len(motif) and motif[i] == chaine[j+i]:
            # print("i=",i,"motif[i]",motif[i],"j=",j,)
            i = i + 1
        if i == len(motif):  # toutes les lettres suivantes de la chaine correspondent au motif}
            # print("chaine présente")
            pos_chaine.append(j)  # position de la chaine
            present = True  # chaine présente au moins une fois
    return pos_chaine, present


motif0 = "PLE"
chaine0 = "VOICI UN SIMPLE EXEMPLE"
present = (motif0 in chaine0)
# print(present)
position0, presence0 = algo_naif(motif0, chaine0)
print(position0, presence0)


motif1 = "CGGCAG"
chaine1 = "CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGG"
# position1, presence1 = algo_naif(motif1,chaine1)
# print(position1, presence1)


motif2 = "CA"
chaine2 = "CAATGTCTGCACCAAGACGCCGGCAGGTGCAGACCTTCGTTATAGG"
# position2, presence2 = algo_naif(motif2,chaine2)
# print(position2, presence2)
