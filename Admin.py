import Classe_abstraite1 from Classe_abstraite1
import Classe_abstraite2 from Classe_abstraite2
  
class Admin (Classe_abstraite1, Class_abstraite2):
  def __init__(id_admin, motdepasse_admin, activite_admin):
    self.id_admin=id_admin
    self.motdepasse_admin=motdepasse_admin
    self.activite_admin = activite_admin
    
  def pays_deja (self,pays):
    return (pays in dico_pays)
 
  def enlever_pays(self,pays): # fonction que l'on va tester
    del dico_pays[pays]
  
  def supprimer_pays(self): # j'appelle, par la suite, "dico_pays" le dictionnaire des pays
    while True: 
      pays_a_supprimer=input("Quel pays souhaitez-vous supprimer ?")
      result=self.pays_deja(pays_a_supprimer)
      if result==False:
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        self.enlever_pays(pays_a_supprimer) 
        print("Le pays "+ pays_a_supprimer + est bien supprime")
        break
    return menu.open_menu.Menu(memory)
  
  def verifier_compte (self,id):
    return (id in Liste_comptes) # le dictionnaire des comptes s'appelle Liste_comptes 
  
  def ajouter_compte(self, id, mdp, stat): # fonction que l'on va tester
    Liste_compte["id"]["Mdp"]=mdp
    Liste_compte["statut"]=stat
  
  def créer_compte(self, memory): # Par la suite, je vais appeler "dico_compte" le dictionnaire des comptes
    while True: 
      id_newcompte=input("Veuillez renseigner l'id du compte à créer")
      result=self.verifier_compte(id_newcompte)
      if result:
        print("Ce compte existe déjà. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        mdp_newcompte=input("Quel est le mot de passe de ce nouveau compte ?")
        statut_newcompte=input("Quel est le statut de ce nouveau compte ?")
        self.ajouter_compte(id_newcompte, mdp_newcompte, statut_newcompte)
        break
    return menu.open_menu.Menu(memory)
  
  def enlever_compte(self, id): # fonction que l'on va tester 
    del Liste_compte[id]
 
  def supprimer_compte(self,memory):
    while True: 
      id_a_supprimer=input("Quel est l'id du compte que vous souhaitez supprimer")
      result=self.verifier_comte(id_a_supprimer)
      if result==False:
        print("Le compte n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        self.enlever_compte(id_a_supprimer)
        break
    return menu.open_menu.Menu(memory)
    
     
      
    
