import class_abstraite_connexion from class_abstraite_connexion

class class_abstraite2 (class_abstraite_connexion):
  
  def __init__(self):
    """ La classe est une classe abstraite"""
    pass
  def accepter_refuser_proposition (proposition):
    """On accepte les propositions disponibles dans le dictionnaire des corrections"""
    print(proposition)
    rep_oui_non= input("Acceptez-vous cette proposition ? (O/N)")
    if rep_oui_non=="O": # Je ne connais la syntaxe des corrections ou propositions 
    
    del liste_correction["proposition"] # on supprime la proposition du dictionnaire, "proposition" correspond à la clé de la proposition
    return("L'operation Accepter ou refuser une proposition est effectuee")
  def ajouter_pays(): # par la suite le dictionnaire des pays sera appelé, liste_pays
    nom_pays=input("Quel est le nom du pays que vous souhaitez créer?")
    pays_deja=True
    while pays_deja: # on vérifie que le pays à ajouter  n'existe pas 
      if liste_pays.has_key(nom_pays):
        nom_pays=input("Ce pays existe deja dans la base de donnees. Veuillez saisir à nouveau le pays que vous voulez créer.")
      else:
        pays_deja=False
    supeficie = input("Quelle est la superficie de"+ nom_pays +" ?")
    population=input ("Quel est le nombre d'habitants de " + nom_pays +" ?")
    croissance_demographique= input("Quel est le taux de croissance de la population de "+nom_pays +" ?")
    inflation = input("Quel est le taux d'inflation de "+nom_pays+" ?")
    dette=input("Quelle est la dette de "+nom_pays+" ?")
    taux_de_chomage=input("Quel est le taux de chomage de "+nom_pays + " ?")
    liste_pays[nom_pays]=[superficie, population, croissance_demographique, inflation, dette, taux de chomage] # ajout du pays dans le dictionnaire
    return("le pays est ajoute")
  
  def modifier_pays(pays):
    pays=input("Quel pays souhaitez-vous modifier les informations ?")
    print ("[1] Superficie")
    print("[2] Nombre d'habitants")
    print ("[3] Taux de croissance de la population")
    indice=input("Quelle information souhaitez-vous modifier ?")
    
    
    
