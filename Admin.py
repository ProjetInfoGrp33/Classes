from ClassesActeur.Classe_abstraite1 import Classe_abstraite1 
from ClassesActeur.Classe_abstraite2 import Classe_abstraite2
from ClassesActeur.fonctions_intermediaires_stat import oui_non
from Menus.open_menu import Menu
  
class Admin (Classe_abstraite1, Classe_abstraite2):
  def __init__(self,id=None,mdp=None,statut='Administrateur'):
      Classe_abstraite1.__init__(self,id,mdp,statut)
    
  
  def supprimer_pays(self,memory): # j'appelle, par la suite, "dico_pays" le dictionnaire des pays
    while True: 
      print("Quel pays souhaitez-vous supprimer ?")
      pays_a_supprimer=input(">")
      result=pays_deja(pays_a_supprimer,memory["data"])
      if result==False:
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        value2 = oui_non()
        if not(value2):
          break
      else:
        print("Etes-vous sûr de vouloir supprimer le pays "+ pays_a_supprimer + "? (O/N)")
        sur=oui_non()
        if sur :
          enlever_pays(pays_a_supprimer,memory["data"]) 
          print("Le pays "+ pays_a_supprimer +" est bien supprimé")
          break
        else:
          break
    input("Tapez sur Entrée pour continuer")
    return Menu(memory)
  
  def creer_compte(self, memory): # Par la suite, je vais appeler "dico_compte" le dictionnaire des comptes
    liste_statut=["Geographe", "Data Scientist", "Admin"]
    while True: 
      id_newcompte=input("Veuillez renseigner l'id du compte à créer ")
      result= verifier_compte(id_newcompte,memory["Liste_comptes"])
      if result:
        print("Ce compte existe déjà. Voulez-vous recommencer ? (O/N)")
        value2= oui_non()
        if not(value2):
          break
      else:
        print("Quel est le mot de passe de ce nouveau compte ? ")
        mdp_newcompte=input(">")
        for i in range(len(liste_statut)):
          print("["+str(i+1)+"]" + liste_statut[i])
        print("Quel est le statut de ce nouveau compte ?")
        statut_newcompte=input(">")
        ajouter_compte(id_newcompte, mdp_newcompte, liste_statut[int(statut_newcompte)-1],memory["Liste_comptes"])
        break
    input("Tapez sur Entrée pour continuer")
    return Menu(memory)
  

 
  def supprimer_compte(self,memory):
    while True: 
      print("Quel est l'id du compte que vous souhaitez supprimer ?")
      id_a_supprimer=input(">")
      result=verifier_compte(id_a_supprimer,memory["Liste_comptes"])
      if result==False:
        print("Le compte n'existe pas. Voulez-vous recommencer ?")
        value2 = oui_non()
        if not(value2):
          break
      else:
        print("Etes-vous sur de vouloir supprimer ce compte ? (O/N)") 
        sur = oui_non()
        if sur :
          enlever_compte(id_a_supprimer,memory["Liste_comptes"])
          print("Compte {} supprimé".format(id_a_supprimer))
          break
        else:
          break
    input("Tapez sur Entrée pour continuer")
    return Menu(memory)

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
      
    
