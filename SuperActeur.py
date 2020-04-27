class SuperActeur():
  def __init__(self,statut):
    self.statut=statut
    
  def verifier_pays (self, pays): # pour verifier que les paus 
    return dict_pays.has_key(pays)   
  
  def ret_afficher_pays (self, pays): # ce sera 
    print("Entrer le nom du pays à afficher (première lettre majuscule, puis lettres minuscules) :")
    pays = input("> ")
    if verifier_pays (self, pays):
      return dict_pays[pays]
    else:
      return None

  def afficher_pays(self, memory):
    while True: 
      if ret_afficher_pays(self)==None:
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value2 = input("> ")
        if value2 in ["1","Oui","oui","O","o"]:
          continue
      else:
        print(ret_afficher_pays)
    return menu.open_menu.Menu(memory)
  
  
  def set_indices_taches(self,indice_taches):
    self.indicetache=indice_taches
    return(self.indicetache)
  
