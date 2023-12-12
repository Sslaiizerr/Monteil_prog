tableDeRoutage = [
    ["192.200.7.8", "192.200.7.253", 3],
    ["192.200.7.0", "192.200.7.254", 3],
    ["192.200.8.0", "192.200.7.254", 7],
    ["défault", "192.200.7.254", 3]
]

trouve = False

adresse_destination = input("Quelle est l'addresse IP de destination ? ")

# Passe toutes les lignes de la liste
for adresse, routeur_saut_suivant, vecteur_de_saut in tableDeRoutage:
    if adresse_destination == adresse and trouve == False:
        trouve = True
        print("datagramme est envoyé à ", routeur_saut_suivant)

    # Teste si l'adresse de destination est dans défault
    if trouve == False:
        for adresse, adresse_resau_destination, vecteur_de_saut in tableDeRoutage:
            if adresse_destination == adresse_resau_destination and trouve == False:
                trouve = True
                print("Le datagramme est envoyé à ", adresse_resau_destination)

    #
    if trouve == False:
        for adresse, routeur_saut_suivant, vecteur_de_saut in tableDeRoutage:
            if adresse == adresse_destination and trouve == False:
                trouve = True
                print("Le datagramme est envoyé à ", routeur_saut_suivant)

if trouve == False:
    print("Impossible d'envoyer le datagramme")
