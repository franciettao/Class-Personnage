#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      stagiaire
#
# Created:     15/11/2023
# Copyright:   (c) stagiaire 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------
import Personnage as P
import random

class MagicienAleatoire(P.Personnage):
""" creation de magicien aleatoirement """
    def __init__(self, race):
        super().__init__(Race=race)  # Assurez-vous de passer l'argument 'Race' à la classe parente
        self.race = race
        self.vie = random.randint(1, 10)
        self.nom = str(random.randint(1, 10))  # En supposant que le nom est une chaîne de caractères
        self.force = random.randint(1, 10)
        self.endurance = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.vitesse = random.randint(1, 10)
        self.forceMagie = random.randint(1, 10)

    def faire_Magique(self, cible, forceMagie):
    """ faire de la magie """
        self.cible = cible
        if self.estMort():
            print("La magie ne peut pas être effectuée car le magicien est mort.")
        else:
            if forceMagie > 0:
                print(f"{self.race} attaque {self.cible} et lui inflige {forceMagie} points de dégâts.")
            else:
                print("La magie ne peut pas être effectuée.")

    def Caracteristiques(self):
    """ carac """
        return f"{self.nom} a une force de {self.force}, une endurance de {self.endurance}, une intelligence de {self.intelligence}, et court à une vitesse de {self.vitesse}."

# Exemple de création et utilisation du MagicienAleatoire
magicien_aleatoire = MagicienAleatoire(race="elfe")
caracteristique = magicien_aleatoire.Caracteristiques()
print("Les caractéristiques sont les suivantes :", caracteristique)
magicien_aleatoire.faire_Magique("Alice", 3)

""" ------------------------------------------------------------------------------------------- secondaire --------------------------------------------------------------------------------------- """

def generer_groupe(Race):
    # Fonction pour générer un groupe de personnages avec une race spécifique
    groupe = []
    for _ in range(10):
        Vie = random.randint(80, 120)
        Nom = Race
        Force = random.randint(8, 12)
        Endurance = random.randint(7, 13)
        Intelligence = random.randint(10, 15)
        Vitesse = random.randint(16, 22)
        personnage = Personnage(Race, Vie, Nom, Force, Endurance, Intelligence, Vitesse)
        groupe.append(personnage)
    return groupe


groupe_cree = generer_groupe("Elfe")

# Créer un dictionnaire pour stocker les caractéristiques des personnages
dict_groupe = {}
for i, personnage in enumerate(groupe_cree, start=1):
    dict_groupe[f"Personnage_{i}"] = {
        "Race": personnage.Race,
        "Vie": personnage.Vie,
        "Nom": personnage.Nom,
        "Force": personnage.Force,
        "Endurance": personnage.Endurance,
        "Intelligence": personnage.Intelligence,
        "Vitesse": personnage.Vitesse
    }

# Affichage du dictionnaire contenant les caractéristiques des personnages
print("Le dictionnaire du groupe de personnages est :", dict_groupe)

























