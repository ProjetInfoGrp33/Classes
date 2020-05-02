import matplotlib.pyplot as plt

def graph2d(self, dico_pays, memory):
  liste_info=["Superficie", "Population", "Croissance démographique", "Inflation", "Dette", "Taux de Chomage", "Taux de Dépenses Santé", 
              "Taux de Dépenses Education", "Taux de Dépenses Militaire"]
  for i in range(len(liste_info)):
    print("["+str(i+1)+"]"+liste_info[i])
  print("Quelle variable souhaitez-vous mettre en abscisse ?")
  indice_info_x=input(">")
  info_x=liste_info[int(indice_info_x)-1]
  x=[]
  for cle in dico_pays.keys():
    x.append(dico_pays[cle][info_x])
  x_croissant=sorted(x)
  rangs_x=[]
  for j in range(len(x)):
    rangs_x.append(x_croissant.index(x[j]))
    
  for k in range(liste_info):
    print("["+str(k+1)+"]"+liste_info[k])
  print("Quelle variable souhaitez-vous mettre en ordonné ?")
  indice_info_y=input(">")
  info_y=liste_info[int(indice_info_y)-1]
  y=[]
  for cle in dico_pays.keys():
    y.append(dico_pays[cle][info_y])
  y_selon_x=[]
  
  for l in range(len(y)):
    y_selon_x.append(0)
  
  for m in range (len(y_selon_x)):
    y_selon_x[m]=y[rangs_x[m]]
  
  plt.scatter(x_croissant,y_selon_x)
  plt.title(info_x+" en fonction de " + info_y)
  
  plt.xlabel(info_x)
  plt.ylabel(info_y)
  
  plt.show()
  
  
              
