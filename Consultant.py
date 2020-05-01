from Preconsultant import Preconsultant
from SuperActeur import SuperActeur
class Consultant(SuperActeur, Preconsultant):
  
  def __init__(self, statut='Consultant'):
      SuperActeur.__init__(self,statut)
      Preconsultant.__init__(self)
      
  
