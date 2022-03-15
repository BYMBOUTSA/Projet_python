"""
      Projet de PYTHON
      Author : Charly MOUNDOUNGA
      date : 13/03/2021

"""
# création de notre dictionnaire
dic = {}

# Création d'une fonction qui va permettre de récupérer des données dans notre dictionnaire
def recup():
    dic = {}
    name = input('Entrez votre nom : ')
    note = int(input('Entrez votre note : '))
    while len(dic.keys()) != 0:
        name = input('Entrez votre nom : ')
        note = int(input('Entrez votre note : '))
    dic[name] = note

    # création d'une fonction qui permet de donner le nombre de pints qui manque
    def point_manquant():
        return 15 - note

    # traitement des moyennes obtenues par les étudiants
    for nom, note in dic.items():
        if note >= 15:
            print(nom, note, "Félicitation vous avez bien validé")
            with open("admis.txt", 'a+') as file:
                file.write(nom + ' vous avez une note de ' + str(note) + ' ' + "Félicitation vous avez bien validé" + '\n')
                file.close()
        elif note < 15 and note >= 12:
            print(nom, note, "Vous devez encore faire des efforts pour valider")
            with open("suivi.txt", 'a+') as file:
                file.write(nom + ' vous avez une note de ' + str(note) + ' il vous manque ' + str(point_manquant()) + ' point(s) ' + "Vous devez encore faire des efforts pour valider" + '\n')
                file.close()
        else:
            print(nom, note, "Vous devez plus bossé car le compte est encore loin")
            with open("effort.txt", 'a+') as file:
                file.write(nom + ' vous avez une note de ' + str(note) + ' il vous manque ' + str(point_manquant()) + ' point(s) '  + "Vous devez plus bossé car le compte est encore loin" + '\n')
                file.close()
    return dic




# Création d'une classe Etablissement
class Establishment:
    def __init__(self, name, matricule, filière):
        self.name = name
        self.matricule = matricule
        self.filière = filière

    def get_name(self):
        return self.name
    def get_matricule(self):
        return self.matricule
    def get_filière(self):
        return self.filière

# Création de la classe Student qui héritera des paramètres de la classe Establishment
class Student(Establishment):
    def __init__(self, name, matricule, filière, dic):
        Establishment.__init__(self, name, matricule, filière)
        self.dic = dic

    def get_dic(self):
        dic = {}
        return recup()




# Création de l'objet student
student = Student('Charly', '15445478', 'GEII', '14')

print('Name : ', student.get_name(), 'dic : ', student.get_dic())
