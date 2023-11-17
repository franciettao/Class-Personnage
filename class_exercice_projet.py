#-------------------------------------------------------------------------------
# Name:        classe Personnages
# Purpose:
#
# Author:      Dalila DROUICHE
#
# Created:     16/11/2023
# Copyright:   (c) stagiaire 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random

class Personnage:
    def __init__(self):
        self.Vie = 10
        self.Nom = ""
        self.Force = 1
        self.Endurance = 0
        self.Rapidité = 0
        self.Intelligence = 0

    def estMort(self):
        return self.Vie <= 0

    def perdVie(self, nbPointsDeViePerdus):
        self.Vie -= nbPointsDeViePerdus
        if self.estMort():
            return "{} est mort".format(self.Nom)
        else:
            return "il reste des points"

    def gagneVie(self, nbPointVieGagne):
        self.Vie += nbPointVieGagne
        if not self.estMort():
            return "{} a été soigné. Ses points de vies valent maintenant {}".format(self.Nom, self.Vie)
        else:
            return "{} ne peut pas être soigné par {}. {} est mort !".format(self.Nom, self.Nom, self.Nom)

    def attaque(self, autrePersonnage):
        if not self.estMort():
            pointsDeDegats = 0.6 * self.Force
            autrePersonnage.Vie -= pointsDeDegats
        else:
            return "{} ne peut attaquer personne : il est mort!".format(self.Nom)

    def soigne(self, nb_points_de_vie_soin):
        """Soigne le personnage actuel ou un autre personnage"""
        if nb_points_de_vie_soin > 0:
            print("{} se soigne de {} points de vie.".format(self.Nom, nb_points_de_vie_soin))
            self.Vie += nb_points_de_vie_soin
        else:
            print("{} n'est pas soigné. Aucun point de vie gagné.".format(self.Nom))

    def esquive(self):
        chance_esquive = self.Rapidité * 1.2
        chance_esquive = round(chance_esquive)

        if random.random() < chance_esquive:
            print("{} a esquivé l'attaque!".format(self.Nom))
            return True
        else:
            print("{} n'a pas réussi à esquiver l'attaque.".format(self.Nom))

    def se_deplacer(self, nb_points_deplacement):
        if nb_points_deplacement > 0:
            print("{} se déplace de {} mètres.".format(self.Nom, nb_points_deplacement))
            self.Rapidité += nb_points_deplacement
        else:
            print("{} reste immobile.".format(self.Nom))


class Magicien(Personnage):
    def __init__(self, Nom, race, points_de_magie):
        super().__init__()
        self.Nom = Nom
        self.race = race
        self.points_de_magie = points_de_magie

    def faire_magie(self, cible, pointsMagie):
        print("{} Le personnage {} fait de la magie.".format(self.Nom, self.race))
        if pointsMagie > 0:
            print(f"{self.Nom} lance un sort sur {cible} et lui inflige {pointsMagie} points de dégâts.")
            self.Vie -= pointsMagie
        elif pointsMagie < 0:
            soin = abs(pointsMagie)
            print(f"{self.Nom} lance un sort de soin sur {cible} et lui restaure {soin} points de vie.")
        else:
            print(f"{self.Nom} lance un sort sur {cible}, mais il n'y a aucun effet.")


class MagicienHumain(Magicien):
    def __init__(self, nom, points_de_magie=90):
        super().__init__(nom, race="Humain", points_de_magie=points_de_magie)


class MagicienHobbit(Magicien):
    def __init__(self, nom, points_de_magie=90):
        super().__init__(nom, race="Hobbit", points_de_magie=points_de_magie)


class MagicienElfe(Magicien):
    def __init__(self, nom, points_de_magie=90):
        super().__init__(nom, race="Elfe", points_de_magie=points_de_magie)


class MagicienNain(Magicien):
    def __init__(self, nom, points_de_magie=90):
        super().__init__(nom, race="Nain", points_de_magie=points_de_magie)


class MagicienOrque(Magicien):
    def __init__(self, nom, points_de_magie=90):
        super().__init__(nom, race="Orque", points_de_magie=points_de_magie)


if __name__ == '__main__':
    person1 = Magicien("test", "lapin", 10)
    person1.faire_magie("cible1", -1)

    p2 = MagicienHumain("hum", points_de_magie=54)

    Personnages = []

    # Ajout d'un personnage à la liste en utilisant la classe Magicien
    person1 = Magicien(
        Nom="Bilbo",
        race="Humain",
        points_de_magie=random.randint(1, 10)
    )

    Personnages.append(person1)

    # Exemple d'affichage des caractéristiques du premier personnage dans la liste
    print(f"Nom: {Personnages[0].Nom}")
    print(f"Race: {Personnages[0].race}")
    print(f"Points de magie: {Personnages[0].points_de_magie}")



    '''Creation des dictionnaire'''
    def creationDicoPersonnagesMagiciens(_nom,_vie,_force,_endurence,_rapidite,_intelligence,_race,_forcemagie):
        DicoPersonnages[_nom]=[_vie,_force,_endurence,_rapidite,_intelligence,_race,_forcemagie]

    def creationDicoPersonnagesmagiciens(_nom,_vie,_force,_endurance,_rapidite,_intelligence,_race,_forcemagie):
        DicoPersonnages[_nom]=[_vie,_force,_endurance,_rapidite,_intelligence,_race,_forcemagie]

    def GetobjetPersonnagebyName(_nom):
        _monPersonnage = personnage()
        _monPersonnage.Nom = _nom
        _monPersonnage.Vie = DicoPersonnages[_nom][0]
        _monPersonnage.Force = DicoPersonnages[_nom][1]
        _monPersonnage.Endurance = DicoPersonnages[_nom][2]
        _monPersonnage.rapidite = DicoPersonnages[_nom][3]
        _monPersonnage.Intelligence = DicoPersonnages[_nom][4]
        return _monPersonnage

    DicoPersonnages={}
    creationDicoPersonnagesmagiciens("Magic-Lalapo",10,4,3,1,10,"Humain",10)




