from ClassesActeur.Classe_abstraite_connexion import Classe_abstraite_connexion
import pandas
import numpy as np
from ClassesActeur.fonctions_intermediaires_stat import  choix_n , choix_liste_pays , choix_critere , choix_seuil ,oui_non, liste_classes_age , liste_critere_donnee, valeurs_classes_age, liste_pays
import matplotlib.pyplot as plt
from Menus.open_menu import Menu


class Classe_abstraite1(Classe_abstraite_connexion):
    def __init__(self,id=None,mdp=None,statut=None):
        Classe_abstraite_connexion.__init__(self,id,mdp,statut)
  
    def resume_informations(self,memory): # créer un menu pour choisir dans les actions proposées
        # n premiers/derniers pays pour 1 critere 
        # les pays dont critere depasse un seuil
        # tableau des classes d'ages (10 max)
        
        affichage_critere(memory["data"])
        print("--------------------------")
        premiers_derniers(memory["data"])
        print("--------------------------")
        seuil(memory["data"])
        print("--------------------------")
        tableau_classes_age(memory["data"])
        return Menu(memory)
    
    def representation_graphique(self,memory):
        diagramme_barre(memory["data"])
        print("--------------------------")
        boxplot_age(memory["data"])
        return Menu(memory)
    
    def ines(self, memory): #fonction correlation entre 2 variables
        print("Coefficient de corrélation entre 2 critères choisis")
        #on choisit les 2 pays 
        print(" ------- ")
        print("Critere numéro 1")
        critere1= choix_critere(memory["data"])
        print(" ------- ")
        print("Critere numéro 2")
        critere2 = choix_critere(memory["data"])

        # Attention ici on prends uniquement les valeurs non NA pour les DEUX criteres simultannemment
        liste_critere1 = liste_critere_donnee(memory["data"],critere1,critere2) # liste des valeurs pour le critere 1
        liste_critere2 = liste_critere_donnee(memory["data"],critere2,critere1) #liste des valeurs pour le critere 2
        correlation = np.corrcoef(liste_critere1,liste_critere2)[0,1]
        print("Le coefficient de correlation entre {} et {} est de {}".format(critere1,critere2,correlation))
        return Menu(memory)
        

############### LES 6 FONCTIONS A L'INTERIEUR 
### utilisent elles meme des fonctions plus elementaires situées dans fonctions_intermediaires_stat  ###
### pays_dans_la_base , choix_n , choix_pays , choix_critere , choix_seuil , liste_criteres, liste_classes_age , liste_critere_donnee, valeurs_classes_age, liste_pays##

############### FONCTIONS FINALES
def affichage_critere(donnees,liste_pays=None): # affiche criteres en un tableau pandas 
    print('Affichage des 9 informations sur une liste de pays choisis')
    #Choix des pays 
    if liste_pays is None:
        liste_pays= choix_liste_pays(donnees)
    else:
        #on cheack que tous les pays de la liste sont dans la base de donnees, sinon on les enleve
        for pays in liste_pays:
            if not(pays in donnees):
                liste_pays.remove(pays)
        #affichage de la liste
        print("Voici une liste pré-établie de pays :")
        i=0
        for pays in liste_pays:
            i+=1
            print("[{}] {}".format(i,pays))
        print("Voulez vous garder ces pays? (O/N)")
        rep_oui_non = oui_non()
        if not(rep_oui_non):# réponse Non
            liste_pays=choix_liste_pays(donnees) # il rentre les pays un à un (pas de possibilité de modifier juste quelques pays)
    
    # Création tableau avec les infos (une ligne par pays)
    tableau = []
    for pays in liste_pays:
        criteres=[]
        liste_critere=[]
        for i in donnees[pays].keys():
            if i!='Classes Age':
                liste_critere.append(donnees[pays][i])
                criteres.append(i)
        tableau.append(liste_critere)
    dataframe= pandas.DataFrame(data=tableau, columns=criteres,index=liste_pays)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    #on affiche ce tableau
    print(dataframe)
    input("Tapez sur Entrée pour continuer")



def premiers_derniers(donnees):
    print('Affichage des n premiers ou n derniers pays selon un critère choisis')

    # choix du critere parmis la liste
    critere= choix_critere(donnees)
    #on sort 2 listes : la liste des pays et la liste du critere correspondant (sans NA)
    liste_critere_choisi= liste_critere_donnee(donnees,critere)
    pays = liste_pays(donnees,critere)
    #choix du n
    print('Veuillez choisir n')
    n = choix_n(1,len(pays))

    #on fait argsort de la liste des criteres
    ordre = np.argsort(liste_critere_choisi)  # on sort les indices des pays trié dans l'ordre croissant 
    pays_trie=[]
    for i in ordre:
        pays_trie.append(pays[i]) # sort la liste des pays triée (par ordre croissant)

    print('Souhaitez vous les {} premiers (P) ou les {} derniers (D)?'.format(n,n))
    while True:
        choice = input(' >')
        if choice.upper() in ['P','PREMIER','PREMIERS']:
            pays_trie=list(reversed(pays_trie)) # on inverse la liste
            break
        elif choice not in ['D','DERNIER','DERNIERS']:
            print("Veuillez taper P pour Premiers ou D pour Derniers")
            continue
    
    print(pays_trie[0:n])
    input("Tapez sur Entrée pour continuer")

    # on sort les pays correspondant au n premiers (derniers) de cette liste trié



def seuil(donnees):
    print("Pays dont un critère dépasse un seuil donnée")
    #choix du critere
    critere = choix_critere(donnees)
    #choix du seuil
    seuil= choix_seuil(donnees,critere)
    #on sort la liste du critere correspondant + liste pays:
    liste= liste_critere_donnee(donnees,critere)
    pays = liste_pays(donnees,critere)
    resultat=[]
    #on parcourt la liste correspondant au critere pour sortir ceux > seuil
    for i in range(len(liste)):
        if liste[i]>seuil:
            resultat.append(pays[i])
    print(resultat)
    input("Tapez sur Entrée pour continuer")


def tableau_classes_age(donnees):
    print("Tableau des classes d'age pour 10 pays maximum")
    #on choisit les 10 pays max
    pays = choix_liste_pays(donnees,10)
    # on crée un tableau où chaque ligne = un pays et colonnes = classes d'ages
    tableau = valeurs_classes_age(donnees,pays)
    classes=liste_classes_age(donnees) # classes en string (1-12 years, 13-20 years )
    #on convertie en data frame pour faciliter l'affichage
    dataframe= pandas.DataFrame(data=tableau, columns=classes,index=pays)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    print(dataframe)


#diagramme en barre pour un critere donné
def diagramme_barre(donnees):
    print("Diagramme en barre pour un critère donné")
    critere = choix_critere(donnees)
    #on sort la liste avec valeurs du critere choisi (sans NA)
    liste_critere = np.log(liste_critere_donnee(donnees,critere))

    plt.hist(liste_critere, bins = 5, color = 'yellow',
            edgecolor = 'red', rwidth = 0.8, log = False)
    plt.ylabel('Effectif')
    plt.xlabel('{} (échelle logarithmique)'.format(critere))
    plt.title('Diagramme en barre')
    plt.show()

def boxplot_age(donnees):
    print("Boxplot de la répartition de la population par classes d'age")
    #liste des classes [0-10 years, ...]
    classes = liste_classes_age(donnees)
    #tableau des valeurs : [france [22%,11%,50%,17%]],[]
    valeurs = valeurs_classes_age(donnees)
    # on convertie en dataframe
    dataframe= pandas.DataFrame(data=valeurs, columns=classes)
    #on sort le boxplot pour toutes les variables 
    dataframe.boxplot(column=classes)
    
    input("Tapez sur Entrée pour continuer")


    
    

    
