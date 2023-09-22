# définition de la stucture de donnée
liste_processus = [
    # processus 1
    ["P1_instruction_1",
     "P1_instruction_2",
     "P1_instruction_3",
     "P1_instruction_4",
     "P1_instruction_5",
     "P1_instruction_6"],
    # processus 2
    ["P2_instruction_1",
     "P2_instruction_2",
     "P2_instruction_3"],
    # processus 3
    ["P3_instruction 1",
     "P3_instruction 2",
     "P3_instruction 3",
     "P3_instruction 4",
     "P3_instruction 5"],
]

print("Ordonnancement des instructions exécutés par le processeur")
for indice_processus in range(len(liste_processus)):
    for indice_instruction in range(len(liste_processus[indice_processus])):
        print(liste_processus[indice_processus][indice_instruction])
