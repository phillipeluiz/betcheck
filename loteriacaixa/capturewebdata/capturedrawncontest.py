#! python3
# Captura numeros sorteados em um concurso do site da Caixa
import re
from domain.entity import contest
from capturewebdata.connectbrowser import connectfirefox
from capturewebdata.waitpageshow import waitvalidpageshow
from selenium.webdriver.common.keys import Keys

"""
Retorna os dados do concurso sorteado atual
"""
def get_last_draw_contest(modality,nrocontest=""):
    try:

        browser = connectfirefox()

        if (browser.current_url != 'http://loterias.caixa.gov.br/wps/portal/loterias/landing/'+ modality + '/'):
            browser.get('http://loterias.caixa.gov.br/wps/portal/loterias/landing/' + modality + '/')
            waitvalidpageshow(browser, 'resultado-lotofacil', 2)

            #Se houver um concurso informado realiza a busca no site
            if (get_custom_draw_contest(browser, nrocontest) == True):
                waitvalidpageshow(browser, 'resultado-lotofacil', 2)
            

            #__elem_drawn_number_list = browser.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[3]/section/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/table/tbody/tr/*')
            __elem_drawn_number_list = browser.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[3]/section/div[2]/div[2]/div/div/div[2]/div/div/div[1]/ul')[0].text.split()
            __elem_contest =  browser.find_element_by_css_selector('.title-bar > h2:nth-child(2) > span:nth-child(1)')
            __drawns_list = []

            for __drawn in __elem_drawn_number_list:
                __drawns_list.append(str(int(__drawn)))

            __regex_contest = re.compile(' (D)*[0-9][0-9][0-9][0-9]')
            __regex_date_contest = re.compile('[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]')

            __contestid = __regex_contest.search(__elem_contest.text).group().strip(' ')
            __contestdate = __regex_date_contest.search(__elem_contest.text).group().strip(' ')

            mycontest = contest.Contest(__contestid,modality)
            mycontest.set_drawn(__drawns_list)
            mycontest.set_date(__contestdate)
        
        return mycontest
        
    except Exception as Err:
        print(str(Err.__traceback__) + '\n' + str(Err))
        return False
        
    finally:
        browser.quit()


# Se for diferente de vazio, preencher com o numero do sorteio o campo com id = buscaConcurso
# enviar a tecla ENTER e aguardar a formação da pagina, a seguir é da mesma forma como
def get_custom_draw_contest(browser, contest):
    if (contest.isdigit()):
        if (len(contest)>=4):
            elemInput = browser.find_element_by_id('buscaConcurso')
            elemInput.send_keys(contest + Keys.RETURN)
            #elemInput.submit() #envia tecla <enter>
            return True
    else:
        return False
        
