#-------------------------------------------------------------------------------
# Name:        25.classMagicien
# Purpose:
#
# Author:      stagiaire
#
# Created:     15/11/2023
# Copyright:   (c) stagiaire 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

from random import randint
#randint: random integer
class Personnage:
    def __init__(self, index=0, vie=0, nom="", force=0, endurance=0, rapidite=0, intelligence=0, vitesse=0):
        self.index = index
        self.vie = vie
        self.nom = nom
        self.force = force
        self.endurance = endurance
        self.rapidite = rapidite
        self.intelligence = intelligence
        self.vitesse = vitesse

class Magicien(Personnage):
    def __init__(self, index, vie, nom, force, endurance, intelligence, vitesse, race, magie): #race: "Humain", "Elfe", "Nain", "Orque"

        self.race = race           # __init__ -> CONSTRUCTEUR /BUILDER
        self.magie = magie


# MagicienHumain <= 100, MagicienHobbit <= 200, MagicienElfe <= 300, MagicienNain <= 400, MagicienOrque <= 500
def faireMagie(self,magie):
    if self.magie > 0 and self.magie <= 100:
        race = MagicienHumain
        return f"{self.nom} est un MagicienHumain"
    elif self.magie > 100 and self.magie <= 200:
        race = MagicienHobbit
        return f"{self.nom} est un MagicienHobbit"
    elif self.magie > 200 and self.magie <= 300:
        race = MagicienElfe
        return f"{self.nom} est un MagicienElfe"
    elif self.magie > 300 and self.magie <= 400:
        race = MagicienNain
        return f"{self.nom} est un MagicienNain"
    elif self.magie > 400 and self.magie <= 500:
        race = MagicienOrque
        return f"{self.nom} est un MagicienOrque"
    else:
        race = None
        return f"{self.nom} est un magicien indéfini"

def lancerSort(autrePersonnage, degats, gain, reste):
    if  autrePersonnage.degats >= 0:
        autrePersonnage.perdreDeLaVie()
        return f"{autrePersonnage.nom} a perdu des points, il perd la vie"

    else:
        autrePersonnage.gain += reste
        autrePersonnage.gagnerDeLaVie()
        return f"{autrePersonnage.nom} gagne des points, il est soigné"

def perdreDeLaVie(self, autrePersonnage, vie):
    if autrePersonnage.vie <= 3:
        return f"{autrePersonnage.nom} a presque perdu la vie"
    else:
        autrePersonnage.afficheEtat()

def gagnerDeLaVie(self, autrePersonnage, vie):
    if  autrePersonnage.gain > autrePersonnage.vie:
        return f"{autrePersonnage.nom} est soigné"
    else:
        autrePersonnage.perdreDeLaVie()

DicoPersonnages={}

def creationDicopersonnages(nom,vie,force,endurance,rapidite,intelligence):
    DicoPersonnages[nom]=[vie,force,endurance,rapidite,inetelligence]

def creationDicopersonnagesMagiciens(nom,vie,force,endurance,rapidite,intelligence,race,magie):
    DicoPersonnages[nom]=[vie,force,endurance,rapidite,intelligence,race,magie]

def GetObjetPersonnageByName(nom):
    monPersonnage=Personnage()
    monPersonnage.Nom = nom
    monPersonnage.Vie = DicoPersonnages[nom][0]
    monPersonnage.Force = DicoPersonnages[nom][1]
    monPersonnage.Endurance = DicoPersonnages[nom][2]
    monPersonnage.Rapidite = DicoPersonnages[nom][3]
    monPersonnage.Intelligence = DicoPersonnages[nom][4]
    return monPersonnage

def afficheCaracteristique(self):
    #Affiche les caracteristiques du personnage
    print(self.nom)
    print("_" * len(self.nom))
    print("Force    :",self.force)
    print("Endurance    :",self.endurance)
    print("Rapidite    :",self.rapidite)
    print("Intelligence    :",self.intelligence)
    print("Race    :",self.race)
    if self.magie > 0:
        print("Magie    :",self.magie)
    print("Camps    :","Gentil" if self.camps else "Méchant")
    print()

personnages = [
    Personnage("Alice", 10, 5, 8, 7),
    Personnage("Bob", 8, 7, 6, 9),
    Personnage("Charlie", 6, 9, 10, 5)
]
#Affichage de la liste des personnages
for perso in personnages:
        #perso.afficheEtat()
    print(perso.afficheCaracteristique())

creationDicopersonnagesMagiciens("Magic-Lalapo",10,4,3,1,10,"Humain",10)

#Création des Gentils
personnages.append(Personnage(index=len(personnages)+1,nom="Bilbo",vie=randint(80,100),force=randint(20,40),endurance=randint(60,80),rapidite=randint(0,20),intelligence=(10,30)))
personnages.append(Personnage(index=len(personnages)+1,nom="Bilbo",vie=randint(80,100),force=randint(20,40),endurance=randint(60,80),rapidite=randint(0,20),intelligence=(10,30)))
personnages.append(Personnage(index=len(personnages)+1,nom="Bilbo",vie=randint(80,100),force=randint(20,40),endurance=randint(60,80),rapidite=randint(0,20),intelligence=(10,30)))
personnages.append(Personnage(index=len(personnages)+1,nom="Bilbo",vie=randint(80,100),force=randint(20,40),endurance=randint(60,80),rapidite=randint(0,20),intelligence=(10,30)))

#Création des Méchants
personnages.append(Personnage(index=len(personnages)+1,nom="Gollum",vie=randint(80,100),force=randint(20,60),endurance=randint(60,100),rapidite=randint(0,35),intelligence=(15,45)))
#Création de 10 Orques (Orque0...Orque9)
for i in range(10):
    personnages.append(Personnage(index=len(personnages)+1,nom="Orque"+str(i),vie=randint(20,25),force=randint(20,35),endurance=randint(60,80),rapidite=randint(0,30),intelligence=(10,40)))



def joueur(nom,personnages):
    #Retourne l'objet 'personnage' de la liste à partir de sa propriété 'NOM'
    for n in personnages:
        if n.nom == nom:
            return n

def combat(attaquant, adversaire):
    #combat de deux personnages
    if type(attaquant).__name__ =="Personnage" and type(adversaire).__name__ == "Personnage": #Test si la class est bonne pour éviter
        if attaquant.nom == adversaire.nom:
            print(attaquant.nom, "ne peut pas s'attaquer lui même !!")
            print()
        else:
            if attaquant.camps == adversaire.camps:
                print(attaquant.nom, "ne peut pas attaquer", adversaire.nom, "car ils sont dans le même camp !!")
                print()
            else:
                attaquant.attaque(adversaire)
        return

#Figth
combat(joueur, "L'Elfe",personnages),joueur("Gollum",personnages)
combat(joueur, "Gollum",personnages),joueur("Bilbo",personnages)
combat(joueur, "Bilbo",personnages),joueur("Orque7",personnages)
combat(joueur, "Le copain à Bilbo",personnages),joueur("Orque7",personnages)
combat(joueur, "Gandalf",personnages),joueur("Gollum",personnages)
combat(joueur, "Le nain",personnages),joueur("Orque7",personnages)

#test cohérence entre personnage
combat(joueur("Le nain",personnages), joueur("Gandalf",personnages)) #Attaque copain
'''
# Création de deux personnages
personnage1 = Magicien(vie=100, nom="Alice", force=10, endurance=8, intelligence=15, vitesse=20, race="MagicienHumain", magie=120)
personnage2 = Magicien(vie=120, nom="Bob", force=10, endurance=7, intelligence=12, vitesse=18, race="MagicienHobbit", magie=240)
personnages.append(Magicien(vie=120, nom="Bob", force=randit(0,10), endurance=7, intelligence=12, vitesse=18, race=random.choice(race), magie=240))
print(personnage1.nom)

'''







