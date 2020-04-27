from classe_abstraite_connexion import classe_abstraite_connexion
import pandas
import numpy as np

# Codes pour les fonctions statistiques resume_informations du Data Scientist
# A faire : menu pour qu'il choisisse dans les 4 actions possibles (un peu long sinon)
# + tests unitaire à rajouter : lorsqu'on choisit critere dans la liste n entre 1 et 9

from fonctions_intermediaires_stat import pays_dans_la_base , choix_n , choix_pays , choix_critere , choix_seuil , liste_criteres, liste_classes_age , liste_critere_donnee, valeurs_classes_age, liste_pays
import matplotlib.pyplot as plt

Class classe_abstraite1(classe_abstraite_connexion):
  def __init__(self,id=None,mdp=None,statut=None,activite=0):
    classe_abstraite_connexion.__init__(self,id,mdp,statut,activite)
  
    def resume_informations(self,donnees): # créer un menu pour choisir dans les actions proposées
        # n premiers/derniers pays pour 1 critere 
        # les pays dont critere depasse un seuil
        # tableau des classes d'ages (10 max)
        
        affichage_critere(donnees)
        print("--------------------------")
        premiers_derniers(donnees)
        print("--------------------------")
        seuil(donnees)
        print("--------------------------")
        tableau_classes_age(donnees)
    
    def representation_graphique(self,donnees):
        diagramme_barre(donnees)
        print("--------------------------")
        boxplot_age(donnees)
        

############### FONCTIONS FINALES
def affichage_critere(donnees): # affiche criteres en un tableau pandas 
    print('Affichage des 9 informations sur une liste de pays choisis')
    liste_pays= choix_pays(donnees)
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
    print(dataframe)


def premiers_derniers(donnees):
    print('Affichage des n premiers ou n derniers pays selon un critère choisis')
    #choix du n
    n = choix_n()
    # choix du critere parmis la liste
    critere= choix_critere(donnees)
    #on sort 2 listes : la liste des pays et la liste du critere correspondant (sans NA)
    liste_critere_choisi= liste_critere_donnee(donnees,critere)
    pays = liste_pays(donnees,critere)
    
    #on fait argsort de la liste des criteres
    ordre = np.argsort(liste_critere_choisi)  # on sort les indices des pays trié dans l'ordre croissant 
    pays_trie=[]
    for i in ordre:
        pays_trie.append(pays[i]) # sort la liste des pays triée (par ordre croissant)

    print('Souhaitez vous les {} premiers (P) ou les {} derniers (D)?'.format(n,n))
    choice = input(' >')
    if choice in ['P','PREMIER']:
        pays_trie=list(reversed(pays_trie)) # on inverse la liste
    print(pays_trie[0:n])
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

def tableau_classes_age(donnees):
    print("Tableau des classes d'age pour 10 pays maximum")
    #on choisit les 10 pays max
    pays = choix_pays(donnees,10)
    # on crée un tableau où chaque ligne = un pays et colonnes = classes d'ages
    tableau = valeurs_classes_age(donnees,pays)
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
    n = len(classes) #nombre de classes
    #tableau des valeurs : [france [22%,11%,50%,17%]],[]
    valeurs = valeurs_classes_age(donnees)
    # on convertie en dataframe
    dataframe= pandas.DataFrame(data=valeurs, columns=classes)
    #on sort le boxplot pour toutes les variables 
    dataframe.boxplot(column=classes)
    
    input("Tapez sur Entrée pour continuer")

