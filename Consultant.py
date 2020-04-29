from Preconsultant import Preconsultant
from SuperActeur import SuperActeur
class Consultant(SuperActeur, Preconsultant):
  
  def __init__(self, statut='Consultant'):
      SuperActeur.__init__(statut)
      Preconsultant.__init__()
      
  
