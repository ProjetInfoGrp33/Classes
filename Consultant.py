from ClassesActeur.Preconsultant import Preconsultant
from ClassesActeur.SuperActeur import SuperActeur
class Consultant(SuperActeur, Preconsultant):
  
  def __init__(self, statut='Consultant'):
      SuperActeur.__init__(self,statut)
      
  
