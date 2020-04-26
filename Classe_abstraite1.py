from classe_abstraite_connexion import classe_abstraite_connexion
import pandas
import numpy as np

# Codes pour les fonctions statistiques resume_informations du Data Scientist
# A faire : menu pour qu'il choisisse dans les 4 actions possibles (un peu long sinon)
# + tests unitaire à rajouter : lorsqu'on choisit critere dans la liste n entre 1 et 9

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
        



# FONCTION INTERMEDIAIRES

# test si le pays est dans la base
def pays_dans_la_base(donnees,pays): 
    try:
        donnees[pays]
    except KeyError:
        print("Le pays ne se trouve pas dans la base, réessayer")
        return(False)
    else:
        return(True)

def choix_n(nmin=-10000,nmax=100000):
    while True:
        try:
            n = int(input(" >"))
        except ValueError:
            print("Veuillez rentrer un entier svp")
            continue
        else:
            break
    return(n)
    
 # choix d'une liste de pays
def choix_pays(donnees,nmax=10000):
    liste_pays=[]
    i=1
    Continuer = True
    iter=0
    while Continuer and iter<nmax:
        iter+=1
        print("Veuillez rentrer le nom du pays numéro {}".format(i))
        pays_choisi = input("> ")
        Test=pays_dans_la_base(donnees,pays_choisi) # on fait le test unitaire pour voir si le pays appartient à la base
        if Test:
            liste_pays.append(pays_choisi)
            i +=1
        else:
            continue
        print("Voulez vous rajouter un pays? (O/N)")
        choice= input(' >')
        if choice in ['O','Oui']:
            pass
        else:
            Continuer=False
    return(liste_pays)
    
# choix du critere parmis la liste
def choix_critere(donnees): 
    print("Veuillez choisir le critère dans la liste suivante")
    indice=1
    pays='France'
    for i in donnees[pays].keys():
        if i!= "Classes Age":
            print('[{}]'.format(indice),i)
            indice +=1
    choice = int(input(" >"))
    
    critere = liste_criteres(donnees,'France')[choice-1]
    return(critere)

# choix du seuil pour un critere (on donne le min et le max pour aider l'utilisateur) 
def choix_seuil(donnees,critere):
    liste_critere = liste_critere_donnee(donnees,critere)
    print("Veuillez taper le seuil (sans unité), les valeurs associées à {} se situe entre {} et {}".format(critere,min(liste_critere),max(liste_critere)))
    while True:
        try:
            seuil = input(" >")
            seuil=float(seuil)
        except ValueError:
            print("Erreur: veuillez taper un nombre")
            continue
        else:
            break
    return(seuil)
        
# liste des criteres["Population","Taux de Chomage" ...]
def liste_criteres(donnees,pays): 
    criteres=[]
    for i in donnees[pays].keys():
        if i!='Classes Age':
            criteres.append(i)
    return(criteres)
    
def liste_classes_age(donnees,pays):
    resultat=[]
    for i in donnees[pays]["Classes Age"].keys():
        resultat.append(i)
    return(resultat)
    
 # liste des valeurs pour un critere donné (sans NA)
def liste_critere_donnee(donnees,critere):
    resultat=[]
    for i in donnees.keys():
        if donnees[i][critere] != None:
            resultat.append(donnees[i][critere])
    return(resultat)
    
# liste des pays où le critere choisi n'est pas NA
def liste_pays(donnees,critere):
    liste=[]
    for i in donnees.keys():
        if donnees[i][critere]!= None:
            liste.append(i)
    return(liste)


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
    liste_pays = choix_pays(donnees,10)
    
    # on crée un tableau où chaque ligne = un pays et colonnes = classes d'ages
    tableau = []
    classes = liste_classes_age(donnees,liste_pays[0])
    for pays in liste_pays:
        ligne=[]
        for classe in classes:
            ligne.append(donnees[pays]['Classes Age'][classe])
        tableau.append(ligne)
    dataframe= pandas.DataFrame(data=tableau, columns=classes,index=liste_pays)
    pandas.set_option("display.max_rows", None, "display.max_columns", None)
    print(dataframe)
    
