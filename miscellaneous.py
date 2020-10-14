from random import *

#fonction pour prendre le nom d'un eleve au hasard
def choiceDict(donnees):
    """
        donnees -> dictionnaires d'eleve
        
        retourne un eleve au hasard 
    """
    index = randint(0,len(donnees)-1)
    nom = ""
    
    #passage dans toute la liste pour trouver par rapport a un index 
    currentIndex = 0
    for identite in donnees.values():
        if currentIndex == index:
            nom = identite["Eleve"]
            break
        currentIndex += 1        
    
    return donnees[nom]



#permet de demander une question a choix fermé
def securInput(question = "oui ou non ?",asksep="/",data=["o","n"]):
    """
        question -> str , la question a poser
        asksep -> str , la separation entre les proposition de choix
        data -> str[] , [OUI,NON] , str a entrer pour faire le choix 
    """
    infos = ""
    while not (infos in data):
        infos = input(question+ " ("+data[0]+asksep+data[1]+")")
        
    if infos == data[0]:
        return True
    else:
        return False