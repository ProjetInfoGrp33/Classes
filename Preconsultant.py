from ClassesActeur.fonctions_intermediaires_stat import choix_critere , rentrer_valeur_critere, choix_pays

class Preconsultant():
  def __init__(self, statut='Consultant'):
      pass
      
  def proposer_correction(self,memory):
      pays = choix_pays(memory["data"])
      print ("Choix du critere a modifier")
      critere = choix_critere(memory["data"])
      print ("Entrer le contenu de la correction :")
      correction = rentrer_valeur_critere()
      memory["Corrections"].append = [pays, critere, correction]
      return memory  #menu.open_menu.Menu(memory)
