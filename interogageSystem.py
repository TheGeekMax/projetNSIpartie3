#########################################
#je precise que cette faute d'orthographe est volontaire #
#########################################
from saveSystem import *
from tkinter import *
from miscellaneous import *
from pointSystem import *

#variable contenant les infos sur l'utilisateur intérogé
student = {
    "nom":"",
    "nee":"",
    "interogage":0
}

#variable qui stockera les Labels et bouttons
toShow = {
    "nom":None,
    "nee":None,
    "interogage":None,
    "save":None,
    "ask":None
}

fen = None
data = None
usersData = None

#fonction qui interoge et actualise l'utilisateur
def askNewUser():
    chooseStudent()
    configure(student)
    

#permet d'ajouter un point d'interogage a l'utilisateur actuel
def addPointCurrentUser():
    addPoint(usersData,student["nom"])
    saveData(usersData)
    
    student["interogage"] += 1
    configure(student)

#fonction qui retourne le profil d'un eleve au hasard
def chooseStudent():
    """
    permet de choisir un eleve au hasard et la stock dans la variable global studdent
    """
    global student
    global usersData
    
    #chargement des données
    usersData = loadData()
    chosenUser = choiceDict(data)
    savedData = getData(usersData,chosenUser["Eleve"])
    
    #modification dans student
    student["nom"] = chosenUser["Eleve"]
    student["nee"] = chosenUser["Né(e) le"]
    student["interogage"] = savedData

#fonction pour set le profil choisi
def configure(data={"nom":"TAPIE Bernard","nee":"26/01/1943","interogage":3}):
    """
    data -> dict , contient les données de l'utilisateur
    
    permet d'afficher l'utilisateur sur la fenetre
    """
    toShow["nom"].configure(text="nom : "+ data["nom"])
    toShow["nee"].configure(text="née : "+ data["nee"])
    toShow["interogage"].configure(text="nb fois intérogé : " + str(data["interogage"]))

#fonction pour la mise en place du  syteme d'interogage (j'adore le francais)
def setup(fene,studdentData):
    """
    fene -> Tkinter Object, contient les données de la fenetre actuelle
    studdentData -> dict , contient les données de tout les eleves
    
    permet de mettre en place pour le choix des eleves
    """
    global toShow
    
    #pour obtenir les infos de la fenetre pour pouvoir la modifier
    global fen
    fen = fene
    global data
    data = studdentData
    
    #clear de la frame
    for widget in fen.winfo_children():
        widget.destroy()
    
    #set des Labels
    toShow["nom"] = Label(fen,text="")
    toShow["nee"] = Label(fen,text="")
    toShow["interogage"] = Label(fen,text="")
    
    toShow["nom"].pack()
    toShow["nee"].pack()
    toShow["interogage"].pack()
    
    #definit un profile par defaut
    askNewUser()
    
    #ajout des boutons utiles au bon fonctionnement
    toShow["ask"] = Button(fen,text="chercher un autre eleve",command=askNewUser)
    toShow["ask"].pack()
    
    toShow["save"] = Button(fen,text="interoger l'eleve",command=addPointCurrentUser)
    toShow["save"].pack()