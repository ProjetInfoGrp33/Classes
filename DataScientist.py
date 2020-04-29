from Classe_abstraite1 import Classe_abstraite1
from Consultant import Consultant
 
class DataScientist(Consultant, Classe_abstraite1):
  def __init__(self,id=None,mdp=None,activite=0,statut='DataScientist'):
      Classe_abstraite1.__init__(id,mdp,statut,activite)
