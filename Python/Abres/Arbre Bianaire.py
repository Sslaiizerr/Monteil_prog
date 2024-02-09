arbre = ['1', '*', '2', '+', '3', ' ', '+',
         '8', '-', '5', '-', ' ', ' ', '4', ' ']


a = ' '
print("Le résultat de l'équation est ", end="")
for i in arbre:
    a += i
b = eval(a)
print('= ', end='')
print(b)
