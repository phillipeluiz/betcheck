#! python3
# -*- coding: utf-8 -*-
#  Conferir sorteio da loterias da caixa

import os
import re
import json

from createbets import viewbets
from createbets import get_bet_numbers

from createcontest import viewcontests
from createcontest import get_contest_by_number
from createcontest import addbets
from createcontest import updatecontest
from createcontest import get_bets_contests

from capturewebdata.waitpageshow import waitvalidpageshow
from capturewebdata.capturedrawncontest import get_last_draw_contest

from domain.entity import contest
from domain.entity import bet
from domain.repository import contest_repository
from domain.repository import bet_repository

def checkdrawn(modality,contest_number):
    mycontest = choosecontest(modality,contest_number)
    if (type(mycontest) is contest.Contest):
        mycontest.check()
    else:
        if (mycontest!=None and mycontest.isdigit()):
            mycontestdrawn = get_last_draw_contest(modality, mycontest)
        else:
            mycontestdrawn = get_last_draw_contest(modality)

        if mycontestdrawn!=None:
            numbercontest = mycontestdrawn.get_contest_number()
            if numbercontest.isdigit():
                mycurrentcontest = get_contest_by_number(numbercontest,modality)

                mycurrentcontest = refresh_if_new_contest(mycontestdrawn,mycurrentcontest,numbercontest,modality)

                if mycurrentcontest != None:
                    if len(mycurrentcontest.bets)>0:
                        mycurrentcontest.set_drawn(mycontestdrawn.get_drawn())
                        updatecontest(mycurrentcontest)
                        mycurrentcontest.check()
                    else:
                        print('Nao existem apostas para o concurso ' + str(numbercontest))
                else:
                    updatecontest(mycontestdrawn)
                    print('Concurso novo, (',str(mycontestdrawn.contest),') inclua uma aposta')
            else:
                print('Erro ao recuperar concurso')
        else:
            print('Página da Loterias da Caixa está fora do ar.')

def choosecontest(modality,contest_number):
    #print('Digite o concurso a ser conferido, ou vazio para checar o mais recente')
    #contest_number = input()
    if (contest_number == ''):
        return None
    else:
        mycontest = get_contest_by_number(str(contest_number), modality)
        if (mycontest):
            return mycontest
        else:
            return contest_number

def addbets_contest(contest_number,modality, betid):
    jsonbet = get_bet_numbers(betid)
    mycontest = get_contest_by_number(contest_number,modality)
    bets = []
    bets.append(jsonbet)
    addbets(mycontest, bets[0])



def refresh_if_new_contest(contestdrawn,currentcontest,numbercontest,modality):
    #Quando o concurso é novo ou nao tem apostas associadas 
    #essa funcao insere o concurso novo e adiciona todas as apostas no concurso
    if currentcontest == None:
        updatecontest(contestdrawn)
        currentcontest = refreshcontest(currentcontest,numbercontest, modality)
    if len(currentcontest.bets)<=0:
        lstBets = viewbets()
        for bet in lstBets:
            d = json.loads(bet)
            addbets_contest(numbercontest,modality,d["id"]) 
        currentcontest = refreshcontest(currentcontest,numbercontest, modality)
    return currentcontest

def refreshcontest(currentcontest,numbercontest,modality):
    currentcontest = None
    currentcontest = get_contest_by_number(numbercontest,modality)
    return currentcontest