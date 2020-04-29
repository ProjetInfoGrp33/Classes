from fonctions_intermediaires_stat import choix_critere , rentrer_valeur_critere, choix_pays

class Preconsultant():
  def __init__(self):
      pass
  def proposer_correction(self,memory,dict_pays,dict_correction):
      pays = choix_pays(dict_pays)
      print ("Choix du critere a modifier")
      critere = choix_critere(dict_pays)
      print ("Entrer le contenu de la correction :")
      correction = rentrer_valeur_critere()
      indice=1
      nombre_corrections = len(dict_correction)
      indice=max(indice, nombre_corrections)
      dict_correction[indice] = [pays, critere, correction]
      return memory  #menu.open_menu.Menu(memory)
