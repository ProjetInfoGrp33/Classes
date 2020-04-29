# -*- coding: utf-8 -*-
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

def choix_n(nmin=-1000000000,nmax=1000000000):
    while True:
        try:
            n = int(input(" >"))    
        except ValueError:
            print("Veuillez rentrer un entier svp")
            continue #on retente
        else:
            if n<nmin or n>nmax:
                print("Veuillez rentrer un entier entre {} et {}".format(nmin,nmax))
                continue #on retente
            else:
                break #on sort de la boucle infinie : pas d'erreur
    return(n)
    
    
 # choix d'une liste de pays
def choix_liste_pays(donnees,nmax=10000):
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
        Continuer=oui_non()
    return(liste_pays)
    
    
def choix_pays(donnees):
    print("Veuillez rentrer le nom du pays")
    while True:
        pays_choisi = input("> ")
        Test=pays_dans_la_base(donnees,pays_choisi)
        if Test:
            break
        else:
            continue
    return(pays_choisi)
    

# reponses Oui Non    
def oui_non():
    while True:
        choice= input(' >')
        if choice.lower() in ['o','oui']:
            Continuer=True
            break
        elif choice.lower() in ['non','n']:
            Continuer=False
            break
        else:
            print("Veuillez rentrer O pour Oui ou N pour Non")
            continue
    return(Continuer)

# choix du critere parmis la liste
def choix_critere(donnees): 
    print("Veuillez choisir le critère dans la liste suivante")
    indice=1
    pays='France'
    for i in donnees[pays].keys():
        if i!= "Classes Age":
            print('[{}]'.format(indice),i)
            indice +=1
    criteres= liste_criteres(donnees,next(iter(donnees)))
    choice = choix_n(1,len(criteres)) # on rentre un n entre 1 et 9
    critere = criteres[choice-1]
    return(critere)

# choix du seuil pour un critere (on donne le min et le max pour aider l'utilisateur) 
def choix_seuil(donnees,critere):
    liste_critere = liste_critere_donnee(donnees,critere)
    nmin=min(liste_critere)
    nmax=max(liste_critere)
    print("Veuillez taper le seuil (sans unité), les valeurs associées à {} se situe entre {} et {}".format(critere, nmin,nmax))
    while True:
        try:
            seuil = input(" >")
            seuil=float(seuil)
        except ValueError:
            print("Erreur: veuillez taper un nombre")
            continue
        else:
            if seuil>nmax or seuil<nmin:
                print("Veuillez taper un nombre entre {} et {}".format(nmin,nmax))
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

# modification d'une valeur d'un critere (ou proposition de correction)
def rentrer_valeur_critere():
    while True:
        try:
            correction = input("> ")
            correction = float(correction)
        except ValueError:
            print("Veuillez rentrer un chiffre (avec un point '.' pour la virgule))")
            continue
        else:
            break
    return(correction)
