from Classe_abstraite_connexion import Classe_abstraite_connexion 
from fonctions_intermediaires_stat import choix_proposition, choix_pays, liste_criteres, choix_critere

class Classe_abstraite2(Classe_abstraite_connexion):
    def __init__(self,identifiant=None,mdp=None,statut=None,activite=0):
        """ La classe est une classe abstraite"""
        Classe_abstraite_connexion.__init__(self,identifiant,mdp,statut,activite)
    
    def accepter_refuser_proposition(self,donnees,liste_correction,memory=" "):
        """On accepte les propositions disponibles dans le dictionnaire des corrections"""
        indice_proposition = choix_proposition(liste_correction)# l'utilisateur choisit la proposition qu'il veut
        proposition = liste_correction[indice_proposition] # proposition correspondante
        print("Proposition choisie : ", proposition)
        
        print("Acceptez vous cette proposition? Oui : O, Non : N, Ne rien faire : touche Entrée")
        rep_oui_non = input(" >")
        
        if rep_oui_non.upper() in ['OUI','O']:
            pays = proposition[0]
            critere=proposition[1]
            valeur=proposition[2]
            donnees[pays][critere]=valeur # on modifie le critere choisie par la modif
            del liste_correction[indice_proposition] # on supprime la proposition du dictionnaire, "proposition" correspond à la clé de la proposition
            print("Modification effectuée avec succès")
            
        elif rep_oui_non.upper() in ['NON','N']:
            del liste_correction[indice_proposition] # on supprime la proposition du dictionnaire, "proposition" correspond à la clé de la proposition
            print("Proposition effacée.")
        else:
            print("Opération annulée") # on touche à rien
        return memory
    

    
    def ajouter_pays(self,donnees,memory): # 
        #on rentre le nom du pays a ajouter
        nom_pays=rentrer_pays(donnees)
        if nom_pays is None:
            print("Procédure annulée")
        else:  
            criteres = liste_criteres(donnees)
            donnees[nom_pays]={}
            # on demande la valeur a rentrer pour chaque critere
            for i in criteres:
                while True:
                    try:
                        print("Veuillez rentrer la valeur de {} (nombre avec un point '.' pour la virgule)".format(i))
                        valeur = float(input(" >"))
                    except ValueError:
                        print("Veuillez rentrer un entier avec un '.' pour la virgule")
                        continue
                    else:
                        # on ajoute la donnée
                        donnees[nom_pays][i]=valeur
                        print("Valeur pour {} : {}".format(i,valeur))
                        break      
            # cas des classes d'ages a rajouter
            
        return memory
    
    
  
    def modifier_pays(self,dico_pays,memory):
        print("Quel pays souhaitez-vous modifier les informations ?")
        nom_pays = choix_pays(dico_pays)
        if nom_pays is None:
            print("Procédure annulée")
        else:
            print("Quelle information souhaitez vous modifier?")
            critere_a_modifier= choix_critere(dico_pays)
            print("Voici l'information actuelle que vous souhaitez modifier.")
            print(dico_pays[nom_pays][critere_a_modifier])
            while True:
                try:
                    print("Veuillez saisir l'information qui remplaçera l'information ci-dessus")
                    new_info=float(input(" >"))
                except ValueError:
                    print("Veuillez rentrer un nombre, avec un '.' pour la virgule")
                    continue
                else:
                    break
            dico_pays[nom_pays][critere_a_modifier]=new_info
            print("L'information " + critere_a_modifier + " du pays " + nom_pays + " a été modifié")
        return memory
    

#fonctions hors classe
    
def pays_dans_la_base(donnees,pays):
    return pays in donnees
    
   
def rentrer_pays(donnees):
    while True: 
        print("Veuillez rentrer le nom du pays que vous souhaitez créer:")
        pays=input(" >")
        if pays_dans_la_base(donnees,pays):
            print("Le pays existe déjà. Voulez-vous recommencer ?")
            print("[1] Oui")
            print("[2] Non")
            value2 = input("> ")
            if value2 in ["2","Non","non","N","n"]:
                pays=None
                break
            else:
                continue
        else:
            break
    return pays
    

