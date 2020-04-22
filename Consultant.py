Class Consultant(SuperActeur):
  
  def __init__(self, statut, id_cons):
    self.id_cons=id_cons
    self.statut="Consultant"
   
  def proposer_correction(self):
    print ("Entrer le nom du pays à corriger :")
    while True:
      temp=0
      value = input("> ")
      for cle in dict_pays : 
        if str(value)==cle :
          print dict_pays[str(value)]
          temp=1
          break
      if not temp :
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        while True:
          value2 = input("> ")
          if value2 in ["1","Oui","oui","O","o"]:
            proposer_correction(self)
    print ("Entrer le numéro de l'information à corriger :")
    while True:
      temp=0
      value3 = input("> ")
      try : value3=int(value3) and 0<= value3 and value3 <= len(dict_pays[str(value)])
      except ValueError : 
        print ("La réponse attendue est un nombre entier compris entre 0 et le nombre maximum d'informations")
        continue
      break
    print ("Entrer le contenu de la correction :")
    while True:
      value4 = input("> ")
      dict_pays[str(value)][value3]=value4
    return menu.open_menu.Menu(memory)
      
