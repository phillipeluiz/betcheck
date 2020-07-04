#! python3
# persistencia do dominio contest
import json

from domain.datacontext import DataContext
from domain.entity import bet

class BetRepository(DataContext):  
    def __init__(self):
        super().__init__('bet')
        super().opendb('bet')

    def save(self, objbet):
        jsonbet = json.dumps(objbet.__dict__)
        self.save_keyvalue(str(objbet.id), jsonbet)
    
    def get_maxid(self):
        totalkeys = self.list_keys()
        if totalkeys:
            return int(totalkeys[-1])
        else:
            return 1
        
        
    