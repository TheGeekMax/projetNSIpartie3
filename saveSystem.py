from pickle import *
import os.path

#constantes
save_name = "UserData"

#fonction pour charger/faire un nouveau fichier si non existant
def loadData():
    """
        permet de charger le fichier de sauvegarde
    """
    #si le fichier n'existe pas , generer un dictionaire vide
    donnees = {}
    
    if(os.path.isfile(save_name)):
        #si le fichier existe le charger
        dataRaw = open(save_name,"rb")
        donnees = load(dataRaw)
        dataRaw.close()
    
    return donnees

#fonction pour save les informations
def saveData(data):
    """
        data -> dict , objet a enregistrer
        
        save_name -> constante , nom du fichier
        
        permet d'enregistrer les informations des eleves
    """
    file = open(save_name,"wb")
    dump(data,file)
    file.close()