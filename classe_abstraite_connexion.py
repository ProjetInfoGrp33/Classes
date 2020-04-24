
Class classe_abstraite_connexion(SuperActeur):

  def __init__(self,statut,0):
    self.id=id
    self.mdp=mdp
    self.statut=statut
    self.activite=activite
    
  def connexion(self):
    if self.activite==1:
      print("Erreur : utilisateur déjà connecté :")
      return menu.open_menu.Menu(memory)
    print("Entrer votre identifiant:")
    while True:
      temp=0
      value=input("> ")
      for id in dict_compte:
        if value==id:
          temp=1
      if not temp:
        print("Identifiant inexistant, veuillez réessayer")
        continue
    print ("Entrer votre mot de passe :")
    while True:
      value2=input("> ")
      if str(value2)==dict_compte[value][0] : 
        print "Connexion réussie !"
        self.id=value
        self.mdp=value2
        self.statut=dict_compte[value][1]
        self.activite=1
      else :
        print("Le mot de passe est incorrect. Voulez-vous recommencer ?")
        print("[1] Oui")
        print("[2] Non")
        while True:
          value2 = input("> ")
          if value2 in ["1","Oui","oui","O","o"]:
            break
        print ("Entrer votre mot de passe :")
        continue
    return menu.open_menu.Menu(memory)
  
  def deconnexion(self):
    print ("Au Revoir")
    self.activite=0
    
