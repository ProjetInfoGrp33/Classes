# -*- coding: utf-8 -*-

# KMEANS
from sklearn import cluster
import pandas
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt



def Kmeans(donnees,n_cluster=3):
    dataframe=0
    #Gestion de la base de données 
    dataframe = pandas.DataFrame.from_dict(donnees,orient='index')
    del dataframe["Classes Age"]
    # on enleve les pays qui ont une valeur manquante
    pays =[]
    for names in dataframe.columns:
        for index in dataframe.index:
            if str(dataframe[names][index])== 'nan':
                pays.append(index)
    dataframe  = dataframe.drop(pays,axis=0)
    # on centre réduit
    sc = StandardScaler()
    Z = pandas.DataFrame(sc.fit_transform(dataframe),index=dataframe.index,columns=dataframe.columns)
    
    # K means à 3 classes
    kmeans = cluster.KMeans(n_clusters=n_cluster)
    kmeans.fit(Z)
    #index triés des groupes
    idk = np.argsort(kmeans.labels_)
    #affichage des observations et leurs groupes
    z = pandas.DataFrame(Z.index[idk],kmeans.labels_[idk])  
    
    
    # Projection des classes sur l'ACP
    #ACP
    print("Projection des {} classes sur l'ACP".format(n_cluster))
    pca= PCA(n_components=2)
    coord = pca.fit_transform(Z)
    #projeter dans le plan factoriel  avec un code couleur différent selon le groupe
    fig, ax = plt.subplots()
    plt.axhline(0)
    plt.axvline(0)    
    for couleur,k in zip(['red','blue','lawngreen','aqua','yellow','purple','black','grey'],[0,1,2,3,4,5,6,7]):
        ax.scatter(coord[kmeans.labels_==k,0],coord[kmeans.labels_==k,1],c=couleur)
    # on rajoute le nom des pays dessus
    nom_pays = Z.index
    for txt in range(len(nom_pays)):
        ax.annotate(nom_pays[txt], (coord[txt,0],coord[txt,1]))
        
    plt.show() 
    plt.close()
    # Correlation variables pour l'interpretation
    n= len(dataframe)
    p=2
    eigval =  (n-1)/n*pca.explained_variance_
    corr = pca.components_ 
    corr[0,:]=corr[0,:]*np.sqrt(eigval[0])
    corr[1,:]=corr[1,:]*np.sqrt(eigval[1])
    correlation = pandas.DataFrame(corr.T,index=Z.columns,columns=['Axe 1','Axe 2'])
    print("Les coefficients de corrélations des variables avec les axes")
    print(correlation)
    ordrevar1= np.argsort(abs(corr[0,:]))
    var1 = Z.columns[ordrevar1]
    ordrevar2 = np.argsort(abs(corr[1,:]))
    var2 = Z.columns[ordrevar2]
    print("L'axe 1 est expliqué majoritairement par {} et {}".format(var1[-1],var1[-2]))
    print("L'axe 2 est expliqué majoritairement par {} et {}".format(var2[-1],var2[-2]))

