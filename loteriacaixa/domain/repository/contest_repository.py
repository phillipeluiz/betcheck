#! python3
# persistencia do dominio contest
import json

from domain.datacontext import DataContext
from domain.entity import contest

class ContestRepository(DataContext):  
    def __init__(self):
        super().__init__('contest')
        super().opendb('contest')

    """def get_betmaxid(self, contest_number):
        objcontest = json.loads(self.get_value(str(contest_number)))
        if objcontest['bets']:
            return objcontest['bets'][-1]
        else:
            return 0
    """
    
    def save(self, objcontest):
        jsoncontest = json.dumps(objcontest.__dict__)
        self.save_keyvalue(str(objcontest.contest), jsoncontest)