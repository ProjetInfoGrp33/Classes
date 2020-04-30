from fonctions_intermediaires_stat import liste_criteres, liste_classes_age, choix_pays
class SuperActeur():
  def __init__(self):
    pass

  def afficher_pays(self,dict_pays, memory):
      print("Affichage des informations sur un pays:")
      #choix du pays
      pays = choix_pays(dict_pays)
      if pays is None:
          print("Procédure arrêtée")
      else: # affichage des infos sur le pays choisi
          afficher_infos(dict_pays,pays)
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

def afficher_infos(dict_pays,pays):
    criteres=liste_criteres(dict_pays,pays)
    classes= liste_classes_age(dict_pays)
    for critere in criteres:
        print(critere + " : " + str(dict_pays[pays][critere]))
    print("Classes d'age (pourcentage de la population):")
    for classe in classes:
        print(classe + " : " + str(dict_pays[pays]['Classes Age'][classe]))
    

