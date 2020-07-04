#! python3
# -*- coding: utf-8 -*-

from checkdrawn import addbets_contest
from checkdrawn import checkdrawn

from createbets import iter_create_bet
from createbets import viewbets
from createbets import remove as removebets

from createcontest import create as createcontest
from createcontest import viewcontests
from createcontest import get_bets_contests
from createcontest import remove as removecontest

def menu_checkdrawn():
    option=''
    while (option != 'X'):
        print('1 = Checar apostas / 2 = Incluir apostas no concurso / X = Sair')
        option = input()
        if (option == '1'):
            checkdrawn('lotofacil',None)
        elif (option == '2'):
            print('digite o concurso para adicionar apostas:')
            contest_number = input()
            print('lista de apostas')
            print(viewbets())
            print('Digite o id da aposta que será incluida no concurso')
            betid = input()
            addbets_contest(contest_number,'lotofacil',betid)
            print('Aposta adicionada')

def menu_createbets():
    option=''
    while (option != 'X'):
        print('1 = Criar nova aposta / 2 = visualizar aposta / 3 = remover aposta / X = Sair')
        option = input()
        if (option == '1'):
            print('Criar nova aposta')
            iter_create_bet()
        elif (option == '2'):
            print('lista de apostas')
            print(viewbets())
        elif (option == '3'):
            print('Digite o id da aposta para excluir:')
            bet_number = input()
            removebets(str(bet_number))

def menu_createcontest():
    option=''
    while (option != 'X'):
        print('1 = Criar novo concurso \n 2 = visualizar concurso \n 3 = visualizar apostas de um concurso \n 4 = remover concurso / X = Sair')
        option = input()
        if (option == '1'):
            print('Digite o novo concurso:')
            contest_number = input()
            print('Digite a modalidade do concurso')
            modality = input()
            print('concurso ', createcontest(contest_number, modality), ' cadastrado com sucesso')
        elif (option == '2'):
            viewcontests()
        elif (option == '3'):
            print('Digite o concurso:')
            contest_number = input()
            x = get_bets_contests(str(contest_number))
        elif (option == '4'):
            print('Digite o concurso para excluir:')
            contest_number = input()
            removecontest(str(contest_number))

option=''
while (option != 'X'):
    print('1 = Checar concurso \n 2 = Criar Apostas \n 3 = Criar Concursos \n X = Sair')
    option = input()
    if (option == '1'):
        menu_checkdrawn()
    elif (option == '2'):
        menu_createbets()
    elif (option =='3'):
        menu_createcontest()