#! python3
# Conectar com Shelve

import shelve

class DataContext():
    

    def __init__(self, dbname):
        self.dbname = dbname
        self.dbinstance=''

    def set_dbname(self, value):
        self.dbname = value

    def opendb(self, dbname):
        self.dbinstance = shelve.open(dbname)

    def save_keyvalue(self, key, value):
        self.dbinstance[key] = value

    def list_keys(self):
        return list(self.dbinstance.keys())

    def list_values(self):
        return list(self.dbinstance.values())
    
    def get_value(self,key):
        return self.dbinstance[key]

    def remove_item(self, key):
        del self.dbinstance[key]

    def close(self):
        self.dbinstance.close()