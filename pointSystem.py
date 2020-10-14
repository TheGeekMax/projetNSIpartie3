#fonction pour ajouter un point a un eleve quand il est intérogé
def addPoint(data,user):
    """
        data -> dict , contien le nombre de fois qu'un eleve est interrogé
        user -> nom de l'utilisateur interrogé
        
        ajoute un point a l'utilisateur intérogé
    """
    
    if user in data.keys():
        data[user]["count"] += 1
    else:
        data[user] = {"count":1}
        
#permet de recuperer le nombre de fois qu'un certain eleve est été choisi
def getData(data, user):
    """
        data -> dictionnaire contenant les données utilisateur
        user -> utilisateur choisi
        
        permet de donner le nombre de fois qu'un élève ait été choisi
        renvoie 0 si l'eleve n'a jamais été choisi
    """
    
    if user in data.keys():
        return data[user]["count"]
    else:
        return 0