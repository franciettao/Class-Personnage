import random

class Personnage:
    """ defini l'objet personnage """
    def __init__(self, Race, Vie=0, Nom="0", Force=0, Endurance=0, Intelligence=0, Vitesse=0):
        # Initialisation des attributs du personnage
        self.Race = Race
        self.Vie = Vie
        self.Nom = Nom
        self.Force = Force
        self.Endurance = Endurance
        self.Intelligence = Intelligence
        self.Vitesse = Vitesse

    def estMort(self):
    """ inferieur a zero tu es mort..."""
        return self.Vie <= 0

    def afficheEtat(self):
    """ definis l'etat """
        if self.estMort():
            return f"{self.Nom} est mort."
        else:
            return f"{self.Nom} a {self.Vie} points de vie."

    def Caracteristiques(self):
    """ definis les carateristiques des perso """
        # Méthode pour afficher les caractéristiques du personnage
        return f"{self.Nom} a une force de {self.Force}, une endurance de {self.Endurance}, une intelligence de {self.Intelligence}, et court à une vitesse de {self.Vitesse}."

    def ViePerdue(self, nbPointsDeViePerdus):
    """ dega subie attaque mortelle """
        # Méthode pour infliger des dégâts au personnage
        self.Vie -= nbPointsDeViePerdus
        if self.estMort():
            return f"{self.Nom} a subi une attaque mortelle !!!"

    def attaque(self, autrePersonnage):
    """ degat d'attaque """
        # Méthode pour attaquer un autre personnage
        frappe = int(0.6 * self.Force)
        autrePersonnage.Vie -= frappe
        if autrePersonnage.estMort():
            return f"{self.Nom} a vaincu {autrePersonnage.Nom}."
        return f"{self.Nom} attaque {autrePersonnage.Nom}."

    def gagneVie(self, autrePersonnage, nbPointVieGagne):
    """ gain de vie """
        # Méthode pour soigner un autre personnage
        autrePersonnage.Vie += nbPointVieGagne
        return f"{self.Nom} soigne {autrePersonnage.Nom} et lui donne {nbPointVieGagne} points de vie supplémentaires."

    def esquiveAttaque(self, autrePersonnage):
    """ permet d'esquiver les attaques """
        # Méthode pour esquiver une attaque
        if self.Vie > 0 and autrePersonnage.Vie > 0:
            if self.Vitesse * 1.2 > autrePersonnage.Force:
                return f"{self.Nom} esquive l'attaque de {autrePersonnage.Nom}."
            else:
                return f"{self.Nom} ne parvient pas à esquiver l'attaque de {autrePersonnage.Nom}."

    def seDeplace(self):
    """ se déplace """
        # Méthode pour déplacer le personnage
        deplacement = random.choice(["haut", "bas", "gauche", "droite"])
        pointsDeDeplacement = random.randint(1, 5)

        if deplacement == "haut":
            return f"{self.Nom} se déplace vers le haut de {pointsDeDeplacement} pas."
        elif deplacement == "bas":
            return f"{self.Nom} se déplace vers le bas de {pointsDeDeplacement} pas."
        elif deplacement == "gauche":
            return f"{self.Nom} se déplace vers la gauche de {pointsDeDeplacement} pas."
        elif deplacement == "droite":
            return f"{self.Nom} se déplace vers la droite de {pointsDeDeplacement} pas."
    def MagicienAleatoire(self):
        self.race = race
        self.vie = random.randint(1, 10)
        self.nom = str(random.randint(1, 10))  # En supposant que le nom est une chaîne de caractères
        self.force = random.randint(1, 10)
        self.endurance = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.vitesse = random.randint(1, 10)
        self.forceMagie = random.randint(1, 10)

    def faire_Magique(self, cible, forceMagie):
    """ magie """
        self.cible = cible
        if self.estMort():
            print("La magie ne peut pas être effectuée car le magicien est mort.")
        else:
            if forceMagie > 0:
                print(f"{self.race} attaque {self.cible} et lui inflige {forceMagie} points de dégâts.")
            else:
                print("La magie ne peut pas être effectuée.")

    def Caracteristiques(self):
        return f"{self.nom} a une force de {self.force}, une endurance de {self.endurance}, une intelligence de {self.intelligence}, et court à une vitesse de {self.vitesse}."


def generer_groupe(Race):
""" generer un grpe """
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
#groupe_cree = generer_groupe("Elfe")

""" Créer un dictionnaire pour stocker les caractéristiques des personnages """
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
#print("Le dictionnaire du groupe de personnages est :", dict_groupe)




# Exemple d'utilisation pour générer un groupe d'orques et afficher leurs caractéristiques
#groupe_orques = generer_groupe("orque")
#for orc in groupe_orques:
    #print(orc.Caracteristiques())

#personnage1 = Personnage(Race="elfe", Vie=100, Nom="Grom", Force=10, Endurance=8, Intelligence=15, Vitesse=20)
#personnage2 = Personnage(Race="orque", Vie=120, Nom="Throk", Force=12, Endurance=7, Intelligence=12, Vitesse=18)
#personnage3 = MagicienAleatoire("Alice", 3)
# Affichage de l'état initial des personnages







# Création des deux magiciens humains
#magicien_humain1 = Personnage(Race="humain", Vie=100, Nom="Merlin", Force=8, Endurance=9, Intelligence=14, Vitesse=18)
#magicien_humain2 = Personnage(Race="humain", Vie=110, Nom="Gandalf", Force=9, Endurance=8, Intelligence=15, Vitesse=17)

# Groupe d'orques
#groupe_orques = generer_groupe("orque")

# Attaque des orques sur les magiciens humains
#for orc in groupe_orques:
    #print(orc.attaque(magicien_humain1))
   # print(orc.attaque(magicien_humain2))

# Tentative d'esquive des magiciens humains
#for magicien in [magicien_humain1, magicien_humain2]:
 #   for orc in groupe_orques:
  #      print(magicien.esquiveAttaque(orc))