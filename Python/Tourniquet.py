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

i_instruction = 0
existe_instruction = 1

while existe_instruction != 0:
    i_processus = 0
    existe_instruction = 0
    while i_processus < len(liste_processus):
        if i_instruction < len(liste_processus[i_processus]):
            print(liste_processus[i_processus][i_instruction])
            existe_instruction = 1
        i_processus += 1
    i_instruction += 1
