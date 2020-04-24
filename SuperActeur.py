class SuperActeur():
  def __init__(self,statut):
    self.statut=statut
    self.id=id
    self.motdepasse=motdepasse

  def afficher_pays(self):
    print("Entrer le nom du pays à afficher :")
    temp=0
    value = input("> ")
    for cle in dict_pays : 
      if str(value)==cle :
        print dict_pays[cle]
        temp=1
        break
    if not temp :
      print("Le pays n'existe pas. Voulez-vous recommencer ?")
      print("[1] Oui")
      print("[2] Non")
      value2 = input("> ")
        if value2 in ["1","Oui","oui","O","o"]:
          afficher_pays(self)
    return menu.open_menu.Menu(memory)
  def set_indices_taches(self,indice_taches):
    self.indicetache=indice_taches
    return(self.indicetache)
  
