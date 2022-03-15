# Création de notre dictionnaire
dic = {}

# Affectation des valeurs et des clées
dic['Charly'] = 20
dic['Angel'] = 15
dic['Jean'] = 12

# On demande à l'utilisateur  Jean d'entrée sa moyenne lui même
dic['Jean'] = int(input("Entrez votre moyenne : "))

# On itère sur notre dictionnaire afin de récupérer nos noms et nos notes les unes à la suite des autres
for nom, note in dic.items():
    # print(nom, note)


    # On félicite l'élève si il a obtenu une moyenne inférieure ou égal à 15
    if note >= 15:
        print(nom, 'Tu as obtenu une note de', note, 'Félicitation vous êtes retenu')
        with open("note.txt", 'a+') as file:
            file.write(nom + ' ' + str(note) + '\n')
            file.close()

    else:
        print(nom, 'Tu as obtenu une note de', note, 'Heuresement que vous pouvez faire mieux')


