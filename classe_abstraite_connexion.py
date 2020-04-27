from SuperActeur import SuperActeur
Class classe_abstraite_connexion(SuperActeur):

  def __init__(self,id=None,mdp=None,statut=None,activite=0):
    self.id=id
    self.mdp=mdp
    self.statut=statut
    self.activite=activite
    
  def connexion(self):
    print("Entrer votre identifiant:")
    while True:
      value=input("> ")
      if not dict_compte.has_key(value):
        print("Identifiant inexistant, veuillez réessayer")
        continue
    print ("Entrer votre mot de passe :")
    while True:
      value2=input("> ")
      if str(value2)==dict_compte[value]["mdp"] : 
        print "Connexion réussie !"
      else :
        print("Le mot de passe est incorrect. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","N","non","n"]:
          return(None, None)
        print ("Entrer votre mot de passe :")
        continue
    if dict_compte[value]["Statut"]=="Géographe":
      return Geographe(value,dict_compte[value]["mdp"],dict_compte[value]["Statut"],1) , "indice_taches_geo"
    if dict_compte[value]["Statut"]=="Data_Scientist":
      return Data_Scientist(value,dict_compte[value]["mdp"],dict_compte[value]["Statut"],1), "indice_taches_ds"
    if dict_compte[value]["Statut"]=="Administrateur":
      return Administrateur(value,dict_compte[value]["mdp"],dict_compte[value]["Statut"],1), "indice_taches_admin"
  
  def deconnexion(self):
    print ("Au Revoir")
    self.activite=0
    
