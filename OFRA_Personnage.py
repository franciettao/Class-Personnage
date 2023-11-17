import random



class Personnage:
    def __init__(self, Nom="Solina", Vie=100, Force=100, Rapidite=100, Intelligence=100, Attributs=None, Magie=None):
        """
        Initialize the attributes of the character.
        
        Args:
            Nom (str): The name of the character. Default is "Solina".
            Vie (int): The health points of the character. Default is 100.
            Force (int): The strength points of the character. Default is 100.
            Rapidite (int): The speed points of the character. Default is 100.
            Intelligence (int): The intelligence points of the character. Default is 100.
            Attributs (dict): Additional attributes of the character. Default is None.
            Magie (str): The magic ability of the character. Default is None.
        """
        self.Nom = Nom
        self.Vie = Vie
        self.Force = Force
        self.Rapidite = Rapidite
        self.Intelligence = Intelligence
        self.Attributs = Attributs
        self.Magie = Magie

    def __repr__(self):
        return f"{self.Nom} est un {self.Attributs} de niveau {self.Force}, créateur {self.Intelligence}, court à une vitesse de {self.Rapidite}, possède {self.Vie} points de vie et {self.Magie} points de magie."

    def estMort(self):
        if self.Vie <= 0:
            print(f"{self.Nom} est mort.")
            return True
        else:
            print(f"{self.Nom} est encore en vie.")
            return False

    def afficheEtat(self):
        if self.Vie == 0:
            print(f"{self.Nom} est mort.")
            return f"{self.Nom} est mort."
        else:
            print(f"{self.Nom} est encore en vie.")
            return f"{self.Nom} a {self.Vie} points de vie."

    def afficheCaracteristiques(self):
        print(f"Nom: {self.Nom}, Vie: {self.Vie}, Force: {self.Force}, Rapidite: {self.Rapidite}, Intelligence: {self.Intelligence}, Attributs: {self.Attributs}, Magie: {self.Magie}")

    def perdVie(self, nbPointsDeViePerdus):
        if nbPointsDeViePerdus > 0:
            print(f"{self.Nom} perd {nbPointsDeViePerdus} points de vie.")
            self.Vie -= nbPointsDeViePerdus
        else:
            print(f"{self.Nom} est encore en vie. Nombre de points perdus {nbPointsDeViePerdus}.")

    def gagneVie(self, nbPointDeVieGagne):
        if nbPointDeVieGagne > 0:
            print(f"{self.Nom} gagne {nbPointDeVieGagne} points de vie.")
            self.Vie += nbPointDeVieGagne
        else:
            print("Le nombre de points de vie gagnés doit être supérieur à zéro.")

    def attaque(self, cible):
        if self.estMort() or cible.estMort():
            print("L'attaque ne peut pas être effectuée car l'attaquant ou la cible est morte.")
        else:
            degat = self.Force * 0.6
            degats = round(degat)
            cible.perdVie(degats)
            print(f"{self.Nom} attaque {cible.Nom} et lui inflige {degats} points de dégâts.")

    def soigne(self, autrePersonnage, pointsDeSoin):
        if pointsDeSoin > 0:
            print(f"{autrePersonnage.Nom} se soigne de {pointsDeSoin} points de vie.")
            autrePersonnage.Vie = autrePersonnage.Vie + pointsDeSoin
        else:
            print(f"{self.Nom} n'est pas soigné. Aucun point de vie gagné.")

    def esquiveAttaque(self, autrePersonnage):
        chance_esquiv = self.Rapidite * 1.2
        
        
        
        chance_esquive = round(chance_esquiv)

        if random.random() < chance_esquive:
            print(f"{self.Nom} a esquivé l'attaque!")
            return True
        else:
            print(f"{self.Nom} n'a pas réussi à esquiver l'attaque.")
            return False

    def se_deplacer(self, nb_points_deplacement):
        if nb_points_deplacement > 0:
            print(f"{self.Nom} se déplace de {nb_points_deplacement} mètres.")
            self.Rapidite += nb_points_deplacement
        else:
            print(f"{self.Nom} reste immobile.")

        situation = random.randint(1, 6)
        if situation == 4:
            print(f"{self.Nom} est tombé dans un trou et n'est pas mort.")
            self.Attributs = 10
        elif situation == 5:
            print(f"{self.Nom} avance tranquillement.")
        elif situation == 33:
            print(f"{self.Nom} renforce une jambe et gagne 13 points de vie.")
            self.Attributs += 100
        elif situation == 6:
            print(f"{self.Nom} a trouvé un trésor !")
        else:
            print(f"{self.Nom} se déplace sans incident.")

        return self.Attributs


class Magicien(Personnage):
    def __init__(self, Nom, Vie, Force, Rapidite, Intelligence, Attributs, Magie, Race, ForceMagie):
        personnage().__init__(Nom, Vie, Force, Rapidite, Intelligence, Attributs, Magie)
        self.Race = Race
        self.ForceMagie = ForceMagie

    def faireMagie(self, autrePersonnage, pointDeMagie):
        degats = self.ForceMagie * pointDeMagie
        if degats > 0:
            autrePersonnage.Vie -= degats
            return f"{self.Nom} lance un sort magique sur {autrePersonnage.Nom}, lui infligeant {degats} points de dégâts !"
        elif degats < 0:
            autrePersonnage.Vie += degats
            return f"{self.Nom} lance un sort de guérison sur {autrePersonnage.Nom}, le soignant de {-degats} points de vie !"
        else:
            return f"{self.Nom} tente un sort, mais il n'a aucun effet sur {autrePersonnage.Nom}."


class MagicienHumain(Magicien):
    def __init__(self, Nom, ForceMagie):
        personnage().__init__(Nom, 0, 0, 0, 0, 0, 100, "Humain", ForceMagie)


class MagicienHobbit(Magicien):
    def __init__(self, Nom, ForceMagie):
        personnage().__init__(Nom, 0, 0, 0, 0, 0, 100, "Hobbit", ForceMagie)


class MagicienElfe(Magicien):
    def __init__(self, Nom, ForceMagie):
        personnage().__init__(Nom, 0, 0, 0, 0, 0, 100, "Elfe", ForceMagie)


class MagicienNain(Magicien):
    def __init__(self, Nom, ForceMagie):
        personnage().__init__(Nom, 0, 0, 0, 0, 0, 100, "Nain", ForceMagie)


def Magie(personnage, pointDeMagie):
    if isinstance(personnage, Magicien):
        return personnage.faireMagie(Pers1, pointDeMagie)
    else:
        return f"{personnage.Nom} n'est pas un magicien et ne peut pas utiliser la magie."


def Attributs(personnage):
    return f"{personnage.Nom} a {personnage.Attributs} attributs."


