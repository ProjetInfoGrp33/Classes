Class Preconsultant():
  def __init__(self):
  
  def proposer_correction(self,memory):
    while True : 
      print ("Entrer le nom du pays à corriger :")
      temp=0
      pays = input("> ")
      if not dict_pays.has_key(pays):
        print("Le pays n'existe pas. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        value = input("> ")
        if value in ["2","Non","non","N","n"]:
          break
      else break
    print ("Entrer le numéro de l'information à corriger :")
    while True:
      num_info = input("> ")
      try : num_info=int(num_info) and 0<= num_info and num_info <= len(dict_pays[str(pays)])
      except ValueError : 
        print ("La réponse attendue est un nombre entier compris entre 0 et le nombre maximum d'informations")
        continue
      print ("Entrer le contenu de la correction :")
      correction = input("> ")
      indice=0
      for cle in dict_correction : 
        indice=max(indice, cle)
      indice+=1
      dict_correction[indice] = [pays, info, correction]
      break
    return menu.open_menu.Menu(memory)
