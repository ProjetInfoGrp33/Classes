import Classe_abstraite1 from Classe_abstraite1
import Classe_abstraite2 from Classe_abstraite2
  
class Admin (Classe_abstraite1, Class_abstraite2):
  def __init__(id_admin, motdepasse_admin, activite_admin):
    self.id_admin=id_admin
    self.motdepasse_admin=motdepasse_admin
    self.activite_admin = activite_admin
  
  def supprimer_pays(self):
    pays_a_supprimer=input("Quel pays souhaitez-vous supprimer ?")
    pays_deja=True 
    
