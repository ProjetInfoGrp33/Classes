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
    print("L'operation Accepter ou refuser une proposition est effectuee")
    return Menu Principal
  
  def pays_deja(self,pays):
    return data.has_key(pays) # le dictionnaire des pays s'appelle data 
  
  def ret_ajouter_pays(self): # 
    nom_pays=input("Quel est le nom du pays que vous souhaitez créer?")
    
    if pays _deja(self, nom_pays):
      supeficie = input("Quelle est la superficie de"+ nom_pays +" ?")
      population=input ("Quel est le nombre d'habitants de " + nom_pays +" ?")
      croissance_demographique= input("Quel est le taux de croissance de la population de "+nom_pays +" ?")
      inflation = input("Quel est le taux d'inflation de "+nom_pays+" ?")
      dette=input("Quelle est la dette de "+nom_pays+" ?")
      taux_de_chomage=input("Quel est le taux de chomage de "+nom_pays + " ?")
      data[nom_pays]={superficie, population, croissance_demographique, inflation, dette, taux de chomage} # ajout du pays dans le dictionnaire
      return ("Le pays "+nom_pays + " est ajouté")
    else:
      return None
   
  def ajouter_pays(self):
    if ret_ajouter_pays(self)==None:
      
  
  def modifier_pays(pays):
    pays=input("Quel pays souhaitez-vous modifier les informations ?")
    liste_informations=["Superficie","Nombre d'habitants", "Taux de croissance de la population", "Taux d'inflation", "Dette",
                        "taux de chomage", "taux de dépenses", "taux de depenses en sante", "taux de depense en education",
                        "taux de depenses militaires", "cinq classes d'age"]
    for i in len(liste_informations): # on demande quelle information l'utilisateur souhaite modifier 
      print(str("["i+1"]"+liste_informations[i]))
          
    indice=input("Quelle information souhaitez-vous modifier ?")
    info_a_modifier=liste_information[indice-1]
    print("Voici l'information actuelle que vous souhaitez modifier.")
    print(dico_pays[pays][info_a_modifier])
    
    new_info=input("Veuillez saisir l'information qui remplaçera l'information ci-dessus")
    dico_pays[pays][liste_information[indice-1]]=new_info
    print("L'information ("+ info_a_modifier+ ") du pays" pays "a été modifié")
    return Menu Principal
    
    
    
    
    
