# projetNSIpartie3
**petite precision avant l'explication**

vous avez pu voir mon abscence la derniere semaine avant les vacances et soyons honete , c'est assez embetant , j'ai pas avancé sur le projet , mais je l'ais testé a fond !

## les explications
quand on lance **main.py** (avec thonny ou IDLE bien sur) on tombe sur une fenetre comme ca

![][./assets/img1.png]

il suffi de cliquer sur le bouton et de selectionner le **.csv** qui represente la classe

l'interface evolue alors !!

*image 2*

maintenant 2 boutons s'affiche
* le bouton **chercher un autre eleve**
* le bouton **interoger l'eleve**

### chercher un autre eleve
ce bouton a une utilité , et vous l'avez deviné c'est d'interoger un nouvel eleve !

### interoger l'eleve
ce bouton sert a interoger un eleve , alors le nombre de fois où il a été interogé seras enregistré 


## si vous vous interessez au code 
voici 2/3 explication sur mon code pour vous simplifier la vie

**avant de commencer !**

je sais que faire des global c'est horrible , mais pour le bien etre du code et de mon cerveau , j'ai préféré en mettre , meme si j'ai esseyé de les minimiser

# Le projet

la partie 3 est composé de 5 fichier

* main.py
* interogageSystem.py
* miscellaneous.py
* pointSystem.py
* saveSystem.py

voici leurs utilité !

### main
le fichier main et le fichier qui s'execute une fois lancé,
elle permet la creation de la fenetre et le chargement du csv selectionné

une fois le fichier chargé , elle va executer une fonction contenue dans **interogageSystem.py**

### interogageSystem
ce fichier va contenir tout ce qu'il faut pour faire fonctioner le programme , meme si elle va utiliser comme aide les autre fichier **.py** (expliqué si dessous)

### miscellaneous
ce fichier contient certaine fonction utile au programme

#### choiceDict
qui permet de choisir un eleve au hasard dans un dictionnaire (malgrès le faite que ce sois un objet non indexable)

#### secureInput
pas très utile ici mais qui permet de faire un Input avec une question fermé

### pointSystem
ce fichier va permettre de s'occuper du nombre de fois qu'un eleve est interogé

#### addPoint
qui va permettre d'ajouter un point a un eleve

#### getData
permet d'obtenir le nombre de fois qu'un eleve est interogé (si l'eleve n'a jamais été intérogé , alors le programme renvoie 0 (logique)

### saveSystem
contients ce qu'il faut pour save

#### save_name
constante qui contient le nom du fichier qui contient les infos sur le nombre de fois intérogé

#### loadData
revoie les données comportant le nombre de fois où chaque eleve a été interogé

#### saveData
permet de sauvegarder les données dans un fichier
