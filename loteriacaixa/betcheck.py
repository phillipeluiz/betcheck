#! python3
# -*- coding: utf-8 -*-
# Console application para chamar funções por linha de comando

import sys
from createbets import iter_create_bet
from createbets import viewbets
from createbets import listbets
from createbets import get_bet_numbers
from createbets import remove as removebets
from checkdrawn import checkdrawn
from createcontest import remove as removecontest
from createcontest import viewcontests
from createcontest import listcontest

# Listar apostas (Parametro 1 = listar-apostas, Parametro 2 Opicional para Apostas Ativas = A ou Inativas = I)        
if (len(sys.argv)>1):
    if ((sys.argv[1]).upper()=='LISTAR'):
        if (len(sys.argv) == 3):
            status = sys.argv[2].upper()
        else:
            status = 'True'
        status = status.replace('I','').replace('A','True')
        listaAposta = listbets(bool(status))
        for i in range(len(listaAposta)):
            print('Id ({:03}) Números apostados {}'.format(listaAposta[i]['id'], listaAposta[i]['numbers']))


#Criar linha de comando para adicionar novas apostas
if (len(sys.argv)>1):
    if((sys.argv[1]).upper()=='ADICIONAR'):
        print('LOTOFÁCIL - 15 Números')
        print('Entre com os números conforme será solicidade.')
        betid = iter_create_bet()
        listaAposta = get_bet_numbers(betid)
        print('Id ({:03}) Números apostados {}'.format(listaAposta['id'], listaAposta['numbers']))

# Remover apostas
if (len(sys.argv)>1):
    if((sys.argv[1]).upper()=='REMOVER-APOSTA'):
        if (len(sys.argv) == 3):
            betid = sys.argv[2].upper()
        if (removebets(str(betid))==True):
            print('Aposta ({:03}) foi removida com sucesso'.format(int(betid)) )
        else:
            print('Erro ao remover ou id da aposta inexistente')


# Conferir concurso
if (len(sys.argv)>1):
    if((sys.argv[1]).upper()=='CONFERIR'):
        contestid = None
        if (len(sys.argv) == 3):
            contestid = sys.argv[2].upper()
        checkdrawn('lotofacil',contestid)


# Remover Concurso
if (len(sys.argv)>1):
    if((sys.argv[1]).upper()=='REMOVER-CONCURSO'):
        if (len(sys.argv) == 3):
            contestnumber = sys.argv[2].upper()
            if (removecontest(str(contestnumber))==True):
                print ('Concurso removido com sucesso')


# Listar apostas (Parametro 1 = listar-apostas, Parametro 2 Opicional para Apostas Ativas = A ou Inativas = I)        
if (len(sys.argv)>1):
    if ((sys.argv[1]).upper()=='LISTAR-CONCURSO'):
        listaConcurso = listcontest()
        for i in range(len(listaConcurso)):
            print('Concurso: ({}) - Nros Sorteados: ({}) - Modalidade: ({})'.format(listaConcurso[i]['contest'],listaConcurso[i]['drawn'], listaConcurso[i]['modality']))
        

final = input()