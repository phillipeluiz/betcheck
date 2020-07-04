#! python3
# -*- coding: utf-8 -*-
# Metodos manipulação de novos concursos
# Finalidade criar concursos

import sys
import json

from domain.entity import contest
from domain.repository import contest_repository

def create(contest_number, modality):
    mycontest = contest.Contest(contest_number, modality)
    contestrepo = contest_repository.ContestRepository()
    contestrepo.save(mycontest)
    contestrepo.close()
    return mycontest

def addbets(contest, bet):
    contestrepo = contest_repository.ContestRepository()
    if contestrepo:
        contest.set_bets(bet)
        contestrepo.save(contest)
        contestrepo.close()

def updatecontest(contest):
    contestrepo = contest_repository.ContestRepository()
    contestrepo.save(contest)
    contestrepo.close()
    

def remove(contest_number):
    contestrepo = contest_repository.ContestRepository()
    try:
        #print(contest_number)
        contestrepo.remove_item(str(contest_number))
        return True
    except KeyError:
        #print('Item indisponível para remover \n',str(Err_Remove),'\n', str(Err_Remove.__traceback__))
        return False
    finally:
        contestrepo.close()

def viewcontests():
    contestrepo = contest_repository.ContestRepository()
    print('lista de concursos')
    print(contestrepo.list_values())
    contestrepo.close()

def listcontest():
    try:
        contestrepo = contest_repository.ContestRepository()
        lstcontests = contestrepo.list_values()
        if (lstcontests):
            newcontest = []
            for i in range(len(lstcontests)):
                l = json.loads(lstcontests[i])
                newcontest.append(l)

            return newcontest
    finally:
        contestrepo.close()

def get_contest_by_number(contest_number,modality):
    #recupera concurso do banco de dados pelo numero do concurso
    contestrepo = get_contest_from_repo_by_number(contest_number)
    if contestrepo != None:
        if len(contestrepo['bets'])>=1:
           #bets = contestrepo['bets'][0] //apagar depois
            bets = contestrepo['bets']
        else:
            bets = None

        drawn = contestrepo['drawn']
        #Cria objeto contest com os dados carregados do banco
        mycontest = contest.Contest(contest_number, modality)
        if (bets!=None):
            if len(bets)>=1:
                for bet in bets:
                    mycontest.set_bets(bet)
        if (drawn!=None):
            if len(drawn)>=1:
                mycontest.set_drawn(drawn)

        return mycontest
    else:
        return None

def get_contest_from_repo_by_number(contest_number):
    contestrepo = contest_repository.ContestRepository()
    #print('lista de apostas por concurso')
    try:
        mycontest = contestrepo.get_value(str(contest_number))
        if mycontest:
            d = json.loads(mycontest)
            return d
    except KeyError as Err_Remove:
        print('Item indisponível \n',str(Err_Remove),'\n', str(Err_Remove.__traceback__))

def get_bets_contests(contest_number):
    contestrepo = contest_repository.ContestRepository()
    #print('lista de apostas por concurso')
    
    try:
        mycontest = contestrepo.get_value(str(contest_number))
        if mycontest:
            d = json.loads(mycontest)
            #for bet in d['bets']:
                #print('Apostas: ', str(bet))
            return d['bets']
    except KeyError as Err_Remove:
        print('Item indisponível \n',str(Err_Remove),'\n', str(Err_Remove.__traceback__))


# Criar um novo concurso com opcionalidade de remover um concurso existente pelo numero do concurso    
