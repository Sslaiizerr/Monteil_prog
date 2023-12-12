def rot13(message):
    clair = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chiffree = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    # strip permet de supprimer certains caractères d'une chaîne de caractère) exemple clair.strip('a')
    clair = list(clair.strip())
    chiffree = list(chiffree.strip())

    transform = [" "] * len(message)
    message = list(message.strip())

    for i in range(len(message)):
        car = message[i]
        for j in range(len(clair)):
            if car == clair[j]:
                transform[i] = chiffree[j]

    # ','.joint(list-str) joint chaque élément de la lsite avec ,
    return ''.join(transform)


def rot13_chr_ord(message, n):
    rot = n
    transform = []
    for car in message:
        # print(car)
        #  print(ord(car))
        # print((ord(car)+rot-97)%26+97)
        chiffree = ((ord(car)+rot-97) % 26)+97
        # print(chr(chiffree))
        transform.append(chr(chiffree))
    return ''.join(transform)


""""
message = "xthexrussiansxarexcoming"


print(rot13(message))
# résulat kgurkehffvnafknerkpbzvat
print(rot13(rot13(message)))
"""
print(' ')

message = "xthexrussiansxarexcoming"
message = message.lower()
transf = rot13_chr_ord(message, 8)
print(transf)
# résulat kgurkehffvnafknerkpbzvat
print(rot13_chr_ord(transf, 18))  # 26 - 8 (8 du dessus, lié au décalage)
chifrée = ((ord('z') + 4 - 97) % 26) + 97
print(chifrée)
print(chr(chifrée))
