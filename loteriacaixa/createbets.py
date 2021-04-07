#! python3
# -*- coding: utf-8 -*-
# Metodos de inclusão de novas apostas
# Finalidade criar apostas novas com base em inclusão dinamica ou dado uma lista de numeros completa

#TODO: Necessario melhorar a criação de apostas condicionando ela a modalidade de sorteio, pois cada um deve ter um tamanho máximo de numeros que podem ser apostados.

import json

from domain.entity import bet
from domain.repository import bet_repository

def create(bet_numbers):
    betrepo = bet_repository.BetRepository()
    betid = betrepo.get_maxid()
    mybet = bet.Bet(betid, bet_numbers)
    betrepo.save(mybet)
    betrepo.close()
    return mybet.get_id()

def remove(id):
    betrepo = bet_repository.BetRepository()
    try:
        betrepo.remove_item(str(id))
        return True
    except KeyError as Err_Remove:
        return False
    finally:
        betrepo.close()


def viewbets():
    try:
        betrepo = bet_repository.BetRepository()
        return betrepo.list_values()
    finally:
        betrepo.close()

def listbets(status):
    try:
        betrepo = bet_repository.BetRepository()
        lstbets = betrepo.list_values()
        if (lstbets):
            newbets = []
            for i in range(len(lstbets)):
                l = json.loads(lstbets[i])
                if (l['status']==status):
                    newbets.append(l)

            return newbets
    finally:
        betrepo.close()
    
def get_bet_numbers(betid):
    betrepo = bet_repository.BetRepository()
    try:
        mybet = betrepo.get_value(str(betid))
        if mybet:
            d = json.loads(mybet)
            #print('Aposta: ', str(d['numbers']))
            return d
    except Exception as Err:
            print(str(Err),str(Err.__traceback__))
    finally:
        betrepo.close()

def iter_create_bet():
    numbers = []
    for i in range(1,18):
        print('(',str(i),') Entre com um número da aposta ou X para sair')
        item_number = input()
        if (item_number != 'X'):
            numbers.append(str(int(item_number)))
        else:
            break

    if numbers:
        betid = create(numbers)
        return betid    
    

