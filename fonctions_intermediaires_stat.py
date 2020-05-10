# -*- coding: utf-8 -*-
# FONCTION INTERMEDIAIRES

# Découpage en 4 sections:
# - fonctions de choix (dans une liste souvent)
# - fonctions de saisie
# - fonction d'affichage
# - fonction qui sort une liste ou un tableau 

###############################################"
# # # # # FONCTIONS DE CHOIX (DANS UNE LISTE)
def choix_pays(donnees):
    while True:
        print("Veuillez rentrer le nom du pays")
        pays_choisi = input("> ")
        Test=pays_dans_la_base(donnees,pays_choisi)
        if Test:
            break
        else:
            print("Voulez vous réessayer ? (O/N)")
            choice = oui_non()
            if choice:
                continue
            else:
                pays_choisi=None
                break
    return(pays_choisi)

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
    
    
# choix du critere parmis la liste
def choix_critere(donnees,classes=False): 
    print("Veuillez choisir le critère dans la liste suivante")
    indice=1
    pays='France'
    for i in donnees[pays].keys():
        if i!= "Classes Age" or classes :
            print('[{}]'.format(indice),i)
            indice +=1
    criteres= liste_criteres(donnees,next(iter(donnees)),classes)
    choice = choix_n(1,len(criteres)) # on rentre un n entre 1 et 9
    critere = criteres[choice-1]
    return(critere)
    
# choix d'une proposition parmis une liste
def choix_proposition(liste_correction): 
    print("Veuillez choisir une correction dans la liste suivante")
    indice=1
    for i in liste_correction:
        print('[{}]'.format(indice),i)
        indice +=1
    choice = choix_n(1,len(liste_correction)) # on rentre un n entre 1 et le nb de corrections
    indice_proposition = choice-1
    return(indice_proposition)
    

#################################################
# # # # #   FONCTIONS DE SAISIE

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

# modification d'une valeur d'un critere (ou proposition de correction)
def rentrer_valeur_critere(nmin=None,nmax=None):
    while True:
        try:
            correction = input("> ")
            correction = float(correction)
        except ValueError:
            print("Veuillez rentrer un chiffre (avec un point '.' pour la virgule))")
            continue
        else: # conditions sur nmin, nmax
            if nmin is not None and nmax is None and correction<nmin:
                print("Veuillez rentrer un chiffre plus grand que {}".format(nmin) )
                continue
            elif nmin is None and nmax is not None and correction>nmax:
                print("Veuillez rentrer un chiffre plus petit que {}".format(nmax))
            elif nmin is not None and nmax is not None and (correction<nmin or correction>nmax):
                print("Veuillez rentrer un chiffre entre {} et {}".format(nmin,nmax))
            break
    
    return(correction)
    
#rentre les valeurs pour les classes d'ages pour un pays donnée 
def rentrer_valeurs_classes_age(donnees,pays): #changer (ajouter) valeur pour les classes d'age
    print("Classes d'ages (pourcentage dans la population, entre 0 et 1)")
    classes= liste_classes_age(donnees)
    while True:
        somme=0
        for classe in classes:
            print("Veuillez rentrer la valeur de {} ".format(classe))
            valeur = rentrer_valeur_critere(0,1)
            donnees[pays]['Classes Age'][classe]=valeur
            print("Valeur pour {} : {}".format(classe,valeur))
            somme += valeur
        if somme !=1:
            print("La somme ne fait pas 1, veuillez retaper les valeurs")
            continue
        else:
            break

#choisit le nom d'un pays à ajouter
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
    
#######################################################
# # # # #  FONCTIONS D'AFFICHAGE

#afficher toutes les infos sur le pays choisi
def afficher_infos(dict_pays,pays):
    criteres=liste_criteres(dict_pays,pays)
    classes= liste_classes_age(dict_pays)
    for critere in criteres:
        print(critere + " : " + str(dict_pays[pays][critere]))
    print("Classes d'age (pourcentage de la population):")
    for classe in classes: 
        print(classe + " : " + str(dict_pays[pays]['Classes Age'][classe]))
    

# test si le pays est dans la base
def pays_dans_la_base(donnees,pays): 
    try:
        donnees[pays]
    except KeyError:
        print("Le pays ne se trouve pas dans la base")
        return(False)
    else:
        return(True)
    
########################################################
# # # # # FONCTIONS QUI RENVOIENT UNE LISTE OU UN TABLEAU
        
# liste des criteres["Population","Taux de Chomage" ...]
def liste_criteres(donnees,pays=None, classes=False): 
    if pays==None:
        pays = next(iter(donnees))
    criteres=[]
    for i in donnees[pays].keys():
        if i!='Classes Age' or classes:
            criteres.append(i)
    return(criteres)
    
def liste_classes_age(donnees):
    resultat=[]
    pays = next(iter(donnees))
    for i in donnees[pays]["Classes Age"].keys():
        resultat.append(i)
    return(resultat)
    
# liste des valeurs pour un critere donné (sans NA)
def liste_critere_donnee(donnees,critere,critere2=None):
    liste=[]
    for i in donnees.keys():
        #si on qu'un critere : on regarde si c'est pas un NA pour le pays i
        # si on a 2 criteres : on regarde si les 2 criteres sont pas NA
        if (critere2 is None and donnees[i][critere]!= None) or (critere2 is not None and donnees[i][critere]!=None and donnees[i][critere2]!=None):
            liste.append(donnees[i][critere])
    return(liste)

# liste des pays où le critere choisi n'est pas NA (ajout du critere 2 pour la fonction "Ines")
def liste_pays(donnees,critere,critere2=None):
    liste=[]
    for i in donnees.keys():
        #si on qu'un critere : on regarde si c'est pas un NA pour le pays i
        # si on a 2 criteres : on regarde si les 2 criteres sont pas NA
        if (critere2 is None and donnees[i][critere]!= None) or (critere2 is not None and donnees[i][critere]!=None and donnees[i][critere2]!=None):
            liste.append(i)
    return(liste)


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
    
 
    
    
