from ClassesActeur.fonctions_intermediaires_stat import choix_critere , rentrer_valeur_critere, choix_pays
from Menus.open_menu import Menu

class Preconsultant():
  def __init__(self, statut='Consultant'):
      pass
      
  def proposer_correction(self,memory):
      pays = choix_pays(memory["data"])
      if pays is None:
          print("Procédure abandonnée")
      else:
          print ("Choix du critere a modifier")
          critere = choix_critere(memory["data"])
          donnees=memory["data"]
          print("La valeur actuelle de {} pour {} est {}".format(critere,pays,donnees[pays][critere]))
          print ("Entrer le contenu de la correction :")
          correction = rentrer_valeur_critere()
          memory["Corrections"].append([pays, critere, correction])
      input("Tapez sur Entrée pour continuer")
      return Menu(memory)  #Menus.open_menu.Menu(memory)
  
