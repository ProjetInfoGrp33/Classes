from ClassesActeur.Classe_abstraite1 import Classe_abstraite1 
from ClassesActeur.Classe_abstraite2 import Classe_abstraite2 
  
class Admin (Classe_abstraite1, Classe_abstraite2):
  def __init__(self,id=None,mdp=None,statut='Administrateur',activite=0):
      Classe_abstraite1.__init__(self,id,mdp,statut,activite)
    
  
  def supprimer_pays(self,memory,dico_pays): # j'appelle, par la suite, "dico_pays" le dictionnaire des pays
    while True: 
      pays_a_supprimer=input("Quel pays souhaitez-vous supprimer ?")
      result=pays_deja(pays_a_supprimer,dico_pays)
      if result==False:
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        enlever_pays(pays_a_supprimer,dico_pays) 
        print("Le pays "+ pays_a_supprimer +" est_bien_supprime")
        break
    return memory
  
  def créer_compte(self, memory,liste_comptes): # Par la suite, je vais appeler "dico_compte" le dictionnaire des comptes
    while True: 
      id_newcompte=input("Veuillez renseigner l'id du compte à créer ")
      result= verifier_compte(id_newcompte,liste_comptes)
      if result:
        print("Ce compte existe déjà. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        mdp_newcompte=input("Quel est le mot de passe de ce nouveau compte ? ")
        statut_newcompte=input("Quel est le statut de ce nouveau compte ? ")
        ajouter_compte(id_newcompte, mdp_newcompte, statut_newcompte,liste_comptes)
        break
    return memory
  

 
  def supprimer_compte(self,memory,Liste_comptes):
    while True: 
      id_a_supprimer=input("Quel est l'id du compte que vous souhaitez supprimer ")
      result=verifier_compte(id_a_supprimer,Liste_comptes)
      if result==False:
        print("Le compte n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        enlever_compte(id_a_supprimer,Liste_comptes)
        print("Compte {} supprimé".format(id_a_supprimer))
        break
    return memory

#Fonctions hors classe
      
def pays_deja (pays,dico_pays):
    return (pays in dico_pays)

def enlever_compte(id,Liste_compte): # fonction que l'on va tester 
    del Liste_compte[id]
    
def verifier_compte(id,Liste_comptes):
    return (id in Liste_comptes) # le dictionnaire des comptes s'appelle Liste_comptes 

def ajouter_compte(id, mdp, stat,Liste_compte): # fonction que l'on va tester
    Liste_compte[id]={}
    Liste_compte[id]["Mdp"]=mdp
    Liste_compte[id]["statut"]=stat
    
def enlever_pays(pays,dico_pays): # fonction que l'on va tester
    del dico_pays[pays]
      
    
