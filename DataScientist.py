from ClassesActeur.Classe_abstraite1 import Classe_abstraite1
from ClassesActeur.Preconsultant import Preconsultant
 
class DataScientist(Preconsultant, Classe_abstraite1):
  def __init__(self,id=None,mdp=None,activite=0,statut='DataScientist'):
      Classe_abstraite1.__init__(self,id,mdp,statut,activite)
