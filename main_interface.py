
import sys
import tkinter as tk
import personnages.HDAG_Personnage as hdag
import personnages.OFRA_Personnage as ofra


joueur1 = ofra.Personnage()
joueur2 = hdag.Personnage("2XTerminator")
class FenetreCombat():

    class CustomPrint:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, text):
            self.text_widget.insert(tk.END, text)


    def __init__(self, personnage, autrePersonnage):
        # creation de la fenetre
        self.window = tk.Tk()

        # definition de la text box
        self.text_box = tk.Text(self.window,height=12)
        self.text_box.pack(expand=True, fill="both")

        # recuperation de la sortie standard et ajout du text dans le widget
        sys.stdout = self.CustomPrint(self.text_box)

        # creation des boutons de combat
        self.left_frame = self.createFrame(personnage, autrePersonnage)
        self.right_frame = self.createFrame(autrePersonnage, personnage)

    # fonction qui cree les bouton par joueur
    def createFrame(self, personnage, autrePersonnage):
        # creation de la frame
        frame = tk.Frame(self.window, width=200, height=200)
        
        
        # creation des boutons
        attack = tk.Button(frame, text='attack', command=lambda: personnage.attaque(autrePersonnage))
        attack.pack(side="left",)

        soin = tk.Button(frame, text='soin', command=lambda: personnage.soigne(personnage, 10))
        soin.pack(side="left",)

        esquive = tk.Button(frame, text='esquive', command=lambda: personnage.esquiveAttaque(autrePersonnage))
        esquive.pack(side="left",)

        frame.pack(side="left", fill="both", expand=True)

        return frame
    
    def resize_text_box(self, e):
        # resize the image with width and height of root
        resized = self.text_box.resize((e.width, e.height), Image.LANCZOS)

# initialisation de la fenetre
fenetreCombat = FenetreCombat(joueur1, joueur2)

# affichage de la fenetre
fenetreCombat.window.mainloop()

