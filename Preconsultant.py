from ClassesActeur.fonctions_intermediaires_stat import choix_critere , rentrer_valeur_critere, choix_pays

def __init__(self, statut='Consultant'):
      pass
      
  def proposer_correction(self,memory,dict_pays,liste_correction):
      pays = choix_pays(dict_pays)
      print ("Choix du critere a modifier")
      critere = choix_critere(dict_pays)
      print ("Entrer le contenu de la correction :")
      correction = rentrer_valeur_critere()
      liste_correction.append = [pays, critere, correction]
      return memory  #menu.open_menu.Menu(memory)
