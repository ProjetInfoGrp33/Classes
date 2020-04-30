from fonctions_intermediaires_stat import  choix_pays, afficher_infos
class SuperActeur():
    """
    Classe SuperActeur : Tous les acteurs en héritent : Admin, DataScientist, Géographe et Consultant
    ...
 
    Attribut
    ----------
    indicetache : list
        les indices correspondants aux taches accessibles par l'acteur (pour le déroulement des menus)
    Methods
    -------
    afficher_pays(dict_pays,memory)
        Affiche les 10 informations sur un pays.
    set_indices_taches(indicetache)
        La liste des taches accessibles donnée est rentré en attribut, et redonné en sortie.
    """
    def __init__(self,indicetache=None):
        self.indicetache=indicetache
        """
        Parametres
        ----------
        name : list
            les indices correspondants aux taches accessibles par l'acteur (pour le déroulement des menus)
        """

    def afficher_pays(self,dict_pays, memory=' '):
        """Affiche les 10 informations sur un pays.

        Parametres
        ----------
        dict_pays : dict
            Le dictionnaire des pays
        memory : menu
            Le menu a sortir après l'exécution de cette fonction.

        Returns
        ------
        menu
            Le menu affiché en suivant.
        """
        print("Affichage des informations sur un pays:")
        #choix du pays
        pays = choix_pays(dict_pays)
        if pays is None:
            print("Procédure arrêtée")           
        else: # affichage des infos sur le pays choisi
            afficher_infos(dict_pays,pays)
        return memory #open_menu.Menu(memory)
  
    def set_indices_taches(self,indice_taches):
        """La liste des taches accessibles donnée est rentré en attribut, et redonné en sortie.

        Parametres
        ----------
        indicetache : list
            les indices correspondants aux taches accessibles par l'acteur (pour le déroulement des menus)
        Returns
        ------
        list
            La liste des indices des taches autorisées donnée en paramètre.
        """
        self.indicetache=indice_taches
        return(self.indicetache)
  
#fonctions hors classe
def verifier_pays(pays, dict_pays):# pour verifier que les pays sont dans le dictionnaire des pays 
    """ Vérifie qu'un pays appartient bien a la base de donnée
    Parametres
    ----------
    pays : str
        Pays dont on souhaite savoir si il appartient à la base de données (1ere lettre en majuscule et les autres en minuscules)
    dict_pays : dict
        Dictionnaire complet des pays
        
    Returns
    ------
    bool
        True si le pays appartient au dictionnaire, False sinon
    """
    
    return pays in dict_pays
  
def ret_afficher_pays(pays,dict_pays): # ce sera la fonction que l'on testera 
    """ Renvoie le dictionnaire des informations correspondant au pays souhaité si il existe, None sinon
    Parametres
    ----------
    pays : str
        Pays dont on souhaite savoir si il appartient à la base de données (1ere lettre en majuscule et les autres en minuscules)
    dict_pays : dict
        Dictionnaire complet des pays
        
    Returns
    ------
    dict
        Dictionnaire correspondant au pays donné en paramètre (ou None si le pays n'est pas dans la base)
    """
    if verifier_pays(pays,dict_pays):
      return dict_pays[pays]
    else:
      return None
  

    

