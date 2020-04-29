from SuperActeur import SuperActeur
#from Geographe import Geographe
#from DataScientist import DataScientist
#from Administrateur import Administrateur 

class Classe_abstraite_connexion(SuperActeur):

  def __init__(self,id=None,mdp=None,statut=None,activite=0):
    self.id=id
    self.mdp=mdp
    self.statut=statut
    self.activite=activite
    
  def connexion(self,dict_compte):
    print("Entrer votre identifiant:")
    while True:
      value=input("> ")
      if value not in dict_compte:
        print("Identifiant inexistant, veuillez réessayer")
        continue
      else:
        break
    
    print ("Entrer votre mot de passe :")
    while True:
      value2=input("> ")
      if str(value2)==dict_compte[value]["Mdp"] : 
        print("Connexion réussie !")
        self.activite=1
        break
      else :
        print("Le mot de passe est incorrect. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","N","non","n"]:
          return(None, None)
        print ("Entrer votre mot de passe :")
        continue
    if dict_compte[value]["Statut"]=="Geographe":
      return("geographe crée")#Geographe(value,dict_compte[value]["Mdp"],dict_compte[value]["Statut"],1) , "indice_taches_geo"
    if dict_compte[value]["Statut"]=="DataScientist":
      return("data scientist cree") #DataScientist(value,dict_compte[value]["mdp"],dict_compte[value]["Statut"],1), "indice_taches_ds"
    if dict_compte[value]["Statut"]=="Administrateur":
      return("admin crée" )#Administrateur(value,dict_compte[value]["mdp"],dict_compte[value]["Statut"],1), "indice_taches_admin"
  
  def deconnexion(self):
    print ("Au Revoir")
    self.activite=0
    #on supprime peut etre l'acteur crée?
    
