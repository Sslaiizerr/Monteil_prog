def vigenereCrypte(message):
    clair = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    chiffree = "eobjpwruyhsagnmkivcdzflxqtGXFCAELJMBQNRSDOWUHPIKYZVT_"
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


def vigenereDecrypte(message):
    chiffree = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    clair = "eobjpwruyhsagnmkivcdzflxqtGXFCAELJMBQNRSDOWUHPIKYZVT_"
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


message = "JeSuisEnTrainDeDecrypterLeMessage"
print(vigenereCrypte(message))
messageCrypte = vigenereCrypte(message)
print(vigenereDecrypte(messageCrypte))
