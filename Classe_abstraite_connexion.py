from ClassesActeur.SuperActeur import SuperActeur
from ClassesActeur.fonctions_intermediaires_stat import oui_non

class Classe_abstraite_connexion(SuperActeur):

  def __init__(self,id=None,mdp=None,statut=None):
    self.id=id
    self.mdp=mdp
    self.statut=statut

    
  def connexion(self,memory):
    while True:
      print("Entrer votre identifiant:")
      value=input("> ")
      if value not in memory["Liste_comptes"]:
        print("Identifiant inexistant, voulez-vous réessayer ?")
        rep = oui_non()
        if not(rep):
           return (None, None, Consultant)
      else:
        break
    
    print ("Entrer votre mot de passe :")
    i=1
    while True:
      value2=input("> ")
      mdp= memory["Liste_comptes"][value]["Mdp"] 
      if str(value2)==mdp: 
        print("Connexion réussie !")
        break
      else :
        i+=1
        if i>3:
          print("3 essais non concluants : la connexion est abandonnée")
          return (None, None, Consultant)
        print("Le mot de passe est incorrect. Voulez-vous recommencer ? (O/N)")
        value2 = oui_non()
        if not(value2):
          return(None, None, Consultant)
        print ("Entrer votre mot de passe :")
        continue
    statut= memory["Liste_comptes"][value]["Statut"]
    return(value,mdp,statut)
    
  def deconnexion(self):
    print ("Au Revoir")
    #on supprime peut etre l'acteur crée?
