from Preconsultant import Preconsultant
drom SuperActeur import SuperActeur
Class Consultant(SuperActeur, Preconsultant):
  
  def __init__(self, id_cons):
    self.id=id_cons
    self.Statut=Consultant
   
  
