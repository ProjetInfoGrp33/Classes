from ClassesActeur.Classe_abstraite_connexion import Classe_abstraite_connexion 
from ClassesActeur.fonctions_intermediaires_stat import choix_proposition, choix_pays,liste_classes_age, rentrer_valeurs_classes_age, rentrer_pays, liste_criteres, valeurs_classes_age, choix_critere, rentrer_valeur_critere
import pandas
from Menus.open_menu import Menu

class Classe_abstraite2(Classe_abstraite_connexion):
    def __init__(self,identifiant=None,mdp=None,statut=None):
        """ La classe est une classe abstraite"""
        Classe_abstraite_connexion.__init__(self,identifiant,mdp,statut)
    
    def accepter_refuser_proposition(self,memory):
        """On accepte les propositions disponibles dans le dictionnaire des corrections"""
        if len(memory["Corrections"])!=0:
            indice_proposition = choix_proposition(memory["Corrections"])# l'utilisateur choisit la proposition qu'il veut
            proposition = memory["Corrections"][indice_proposition] # proposition correspondante
            print("Proposition choisie : ", proposition)

            print("Acceptez vous cette proposition? Oui : O, Non : N, Ne rien faire : touche Entrée")
            rep_oui_non = input(" >")

            if rep_oui_non.upper() in ['OUI','O']:
                pays = proposition[0]
                critere=proposition[1]
                valeur=proposition[2]
                modifier_information(pays, critere, valeur, memory["data"])
                supprimer_proposition (indice_proposition, memory["Corrections"]) # on supprime la proposition du dictionnaire, "proposition" correspond à la clé de la proposition

                print("Modification effectuée avec succès")

            elif rep_oui_non.upper() in ['NON','N']:
                supprimer_proposition (indice_proposition, memory["Corrections"]) # on supprime la proposition du dictionnaire, "proposition" correspond à la clé de la proposition
                print("Proposition effacée.")
            else:
                print("Opération annulée") # on touche à rien
        else:
            print("Il n'y a aucune proposition de corrections")
        input("Tapez sur Entrée pour continuer")
        return Menu(memory)
    

    
    def ajouter_pays(self,memory): # 
        #on rentre le nom du pays a ajouter
        nom_pays=rentrer_pays(memory["data"])
        if nom_pays is None:
            print("Procédure annulée")
        else:  
            criteres = liste_criteres(memory["data"])
            memory["data"][nom_pays]={}
            # on demande la valeur a rentrer pour chaque critere
            for i in criteres:
                print("Veuillez rentrer la valeur de {} ".format(i))
                valeur = rentrer_valeur_critere()
                memory["data"][nom_pays][i]=valeur
                print("Valeur pour {} : {}".format(i,valeur))
            # cas particulier des classes d'age
            memory["data"][nom_pays]['Classes Age']={}
            rentrer_valeurs_classes_age(memory["data"],nom_pays)
            # est-ce qu'on fait confirmer à chaque saisie?
        input("Tapez sur Entrée pour continuer")
        return Menu(memory)
    
    
  
    def modifier_pays(self,memory):
        print("Quel pays souhaitez-vous modifier les informations ?")
        nom_pays = choix_pays(memory["data"])
        if nom_pays is None:
            print("Procédure annulée")
        else:
            print("Quelle information souhaitez vous modifier?")
            critere_a_modifier= choix_critere(memory["data"],True)
            if critere_a_modifier !='Classes Age':
                print("Voici l'information actuelle que vous souhaitez modifier.")
                print(memory["data"][nom_pays][critere_a_modifier])
                print("Veuillez saisir l'information qui remplaçera l'information ci-dessus")
                new_info=rentrer_valeur_critere()
                modifier_information(nom_pays, critere_a_modifier, new_info, memory["data"]) 
            else:
                print("Voici l'information actuelle que vous souhaitez modifier.")
                tableau=valeurs_classes_age(memory["data"],[nom_pays])
                classes= liste_classes_age(memory["data"])
                dataframe= pandas.DataFrame(data=tableau, columns=classes,index=[nom_pays])
                pandas.set_option("display.max_rows", None, "display.max_columns", None)
                print(dataframe)                
                rentrer_valeurs_classes_age(memory["data"],nom_pays)
            print("L'information " + critere_a_modifier + " du pays " + nom_pays + " a été modifié")
        
        input("Tapez sur Entrée pour continuer")
        return Menu(memory)
    
#fonctions hors classe
def pays_dans_la_base(donnees,pays):
    return pays in donnees

def supprimer_proposition(indice, liste_prop):
    del liste_prop[indice]
    
def modifier_information(pays, critere, subs, dico_pays):
    dico_pays[pays][critere]=subs

