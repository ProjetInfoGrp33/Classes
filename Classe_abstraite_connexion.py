from ClassesActeur.SuperActeur import SuperActeur
from ClassesActeur.Geographe import Geographe
from ClassesActeur.DataScientist import DataScientist
from ClassesActeur.Admin import Admin
from ClassesActeur.fonctions_intermediaires_stat import oui_non

class Classe_abstraite_connexion(SuperActeur):

  def __init__(self,id=None,mdp=None):
    self.id=id
    self.mdp=mdp

    
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
      mdp= dict_compte[value]["Mdp"] 
      if str(value2)==mdp: 
        print("Connexion réussie !")
        break
      else :
        print("Le mot de passe est incorrect. Voulez-vous recommencer ? (O/N)")
        value2 = oui_non()
        if not(value2):
          return(None, None)
        print ("Entrer votre mot de passe :")
        continue
    statut= dict_compte[value]["Statut"]
    return(value,mdp,statut)
    
  def deconnexion(self):
    print ("Au Revoir")
    #on supprime peut etre l'acteur crée?
