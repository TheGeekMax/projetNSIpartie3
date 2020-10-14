#chargement des autres fichiers
from interogageSystem import *

#chargement des libs
from tkinter.filedialog import askopenfilename
from tkinter import *
from csv import *


#fonction pour demander un fichier a ouvrir
def askFile():
    data = {}
    #demande du fichier
    fichierUrl = askopenfilename(title="selectionnez un fichier CSV")
    fichierRaw = open(fichierUrl,"r",encoding="utf-8")
    dataRaw =  DictReader(fichierRaw,delimiter=",")

    #test de chaque ligne pour l'integrer dans la liste data
    for ligne in dataRaw:
        currentData = dict(ligne)
        data[currentData["Eleve"]] = currentData
        
    #fonction a executer quand le fichier est choisi
    setup(fen,data)

#creation de l'ecran principal
fen = Tk()
fen.geometry("200x200")
fen.title("interogateur 2000")

#ajout du boutton qui va permettre la selection du fichier
selectButton = Button(fen,text="selectionnez un fichier",command=askFile)
selectButton.pack()
fen.mainloop()
