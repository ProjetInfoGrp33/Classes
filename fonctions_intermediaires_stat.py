# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 10:43:27 2020

@author: Inès
"""

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
    
def liste_classes_age(donnees):
    resultat=[]
    pays = next(iter(donnees))
    for i in donnees[pays]["Classes Age"].keys():
        resultat.append(i)
    return(resultat)

#retourne le tableau des classes d'age pour une liste de pays donnée ou la table entiere 
def valeurs_classes_age(donnees,pays=None):
    classes = liste_classes_age(donnees)
    tableau = []
    classes = liste_classes_age(donnees)    
    if pays is None:
        pays = liste_pays(donnees,'Classes Age')
        
    for i in pays:
        ligne=[]
        for classe in classes:
            ligne.append(donnees[i]['Classes Age'][classe])
        tableau.append(ligne)
    return(tableau)
    
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

