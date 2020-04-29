class SuperActeur():
  def __init__(self,statut):
    self.statut=statut
    

  def afficher_pays(self,dict_pays, memory):
    while True: 
        print("Entrer le nom du pays à afficher (première lettre majuscule, puis lettres minuscules) :")
        pays = input("> ")
        result=ret_afficher_pays(pays,dict_pays)
        if result==None:
            print("Le pays n'existe pas. Voulez-vous recommencer ?")
            print("[1] Oui")
            print("[2] Non")
            value2 = input("> ")
            if value2 in ["2","Non","non","N","n"]:
                break
            else:
                continue
        else:
            print(dict_pays[pays])
            break
    return memory #open_menu.Menu(memory)
  
  
  def set_indices_taches(self,indice_taches):
    self.indicetache=indice_taches
    return(self.indicetache)
  
#fonctions hors classe
def verifier_pays(pays, dict_pays): # pour verifier que les pays sont dans le dictionnaire des pays 
    return pays in dict_pays
  
def ret_afficher_pays(pays,dict_pays): # ce sera la fonction que l'on testera 
    if verifier_pays(pays,dict_pays):
      return dict_pays[pays]
    else:
      return None

  
