#! python3
# -*- coding: utf-8 -*-
# Classe de Apostas

#TODO: criar novo método de append na lista de numbers que trate se existe repetição

class Bet():  
    def __init__(self,id, numbers):
        self.id = self.stepupid(id)
        self.numbers = numbers
        self.status = True

    def stepupid(self,max_id):
        max_id += 1
        return max_id

    def get_id(self):
        return self.id

    def check(self, contest):
        try:
            print('bet.contest= ',str(contest.contest))
            print('bet.modality= ',str(contest.modality))
            print('contest.drawn= ',str(contest.drawn))
            if (self.status==True ):
                print('bet.id= ',str(self.id))
                print('bet.numbers= ',str(self.numbers))
                result = set(self.numbers) & set(contest.drawn)
                print('Números acertados ', str(result))
                print('Você teve ', str(len(result)),'acerto(s)')
        except Exception:
            return False
