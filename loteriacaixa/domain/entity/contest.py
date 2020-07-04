import sys

class Contest():  
    def __init__(self, contest, modality):
        self.contest = contest
        self.date = None
        self.modality = modality
        self.drawn = None
        self.bets = []
    
    def set_drawn(self, value):
        self.drawn = value
        
    def get_drawn(self):
        return self.drawn

    def get_contest_number(self):
        return self.contest

    def set_date(self, value):
        self.date = value

    def set_bets(self, value):
        self.bets.append(value)

    def check(self):
        if (self.drawn):
            print('Concurso: ' ,str(self.contest))
            print('Modalidade: ',str(self.modality))
            print('Números Sorteados: ',str(self.drawn))
            for bet in self.bets:
                if (bet != None) & (bet['status']==True):
                    print('----------------------------------------')
                    print('Aposta: ({:03}) - Números: {}'.format(bet['id'], bet['numbers']))
                    result = set(bet['numbers']) & set(self.drawn)
                    print('Números acertados ', str(result))
                    print('Você teve ', str(len(result)),' acerto(s)')
                    
        else:
            print('Sorteio para o concurso não foi capturado.')