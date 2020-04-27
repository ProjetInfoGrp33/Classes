class SuperActeur():
  def __init__(self,statut):
    self.statut=statut
    
  def verifier_pays (self, pays): # pour verifier que les pays sont dans le dictionnaire des pays 
    return dict_pays.has_key(pays)   
  
  def ret_afficher_pays (self): # ce sera la fonction que l'on testera 
    print("Entrer le nom du pays à afficher (première lettre majuscule, puis lettres minuscules) :")
    pays = input("> ")
    if self.verifier_pays (pays):
      return dict_pays[pays]
    else:
      return None

  def afficher_pays(self, memory):
    while True: 
      result=self.ret_afficher_pays()
      if result==None:
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["2","Non","non","N","n"]:
          break
      else:
        print(result)
        break
    return menu.open_menu.Menu(memory)
  
  
  def set_indices_taches(self,indice_taches):
    self.indicetache=indice_taches
    return(self.indicetache)
  
