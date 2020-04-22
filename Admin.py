import Classe_abstraite1 from Classe_abstraite1
import Classe_abstraite2 from Classe_abstraite2
  
class Admin (Classe_abstraite1, Class_abstraite2):
  def __init__(id_admin, motdepasse_admin, activite_admin):
    self.id_admin=id_admin
    self.motdepasse_admin=motdepasse_admin
    self.activite_admin = activite_admin
  
  def supprimer_pays(self): # j'appelle, par la suite, "dico_pays" le dictionnaire des pays
    pays_a_supprimer=input("Quel pays souhaitez-vous supprimer ?")
    pays_deja=False 
    while pays_deja==False:
      if dico_pays.has_key(pays_a_supprimer)==True:
        pays_deja=True
      else:
        pays_a_supprimer = input ("Ce pays n'existe pas, dans notre base de données. Veuillez ressaisir le nom du pays à supprimer")
    del dico_pays[pays_a_supprimer] # suppression du pays 
    print("Le pays "+ pays_a_supprimer + est bien supprime")
    return Menu Principal
  
  def créer_compte(self): # Par la suite, je vais appeler "dico_compte" le dictionnaire des comptes
    id_newcompte=input("Veuillez renseigner l'id du compte à créer"
    id_deja=True
    while id_deja:
        if 
      
    
