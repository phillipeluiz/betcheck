#! python3
# Wait Report Empiricus Page

#libs for wait page show
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitvalidpageshow(browser, reportId, popUpDelay):
    try:
        # Valida Pagina do relatorio
        elemValid = ''
        elemPopUp = ''

        if (reportId=='resultado-lotofacil'):
            elemValid = waitElementByFilterType(browser, 'link_text','Resultado',popUpDelay)
            #elif (reportId=='resultado-'):
            #    elemValid = waitElementByFilterType(browser, 'class_name','report__logo', popUpDelay)
            #elif (reportId='empiricus-melhores'):
                #elemValid = validPageShowTypeWait(browser, reportId, 'class_name','products-header__avatar',5)
            #elif (reportId=='login-empiricus'):
            #    elemValid = waitElementByFilterType(browser, 'class_name','icon-base',popUpDelay)
        else:
            print('elemento de wait nao mapeado')

        if (elemValid!=''):
            print(elemValid)
            print(True)
            if (reportId=='empiricus-vacas'):
                print('não ha popups exclusivos ainda...')
            elif(reportId=='empiricus-vacas-popup01'):
                closePopUp(browser,'id','onesignal-popover-cancel-button',2)
                closePopUp(browser,'css_selector','html.theme-light.wf-droidserif-n4-active.wf-droidserif-i4-active.wf-droidserif-n7-active.wf-lato-n4-active.wf-lato-n7-active.wf-lato-n9-active.wf-active.wf-sourcesanspro-n7-active.wf-sourcesanspro-n6-active.wf-sourcesanspro-n4-active.wf-lato-n5-active.wf-lato-n6-active.wf-montserrat-n4-active.wf-bitter-n4-active.wf-ptsans-n5-active.wf-ptsans-n4-active.om-position-popup.wf-fontawesome-n4-inactive body div#om-af6blfqzaaou05cyqg06.Campaign.CampaignType--popup div#om-af6blfqzaaou05cyqg06-optin.nashville.Campaign__canvas div.Campaign__innerWrapper button.nashville-CloseButton.nashville-close',2)
            else:
                print('não ha popups exclusivos ainda...')

            return True
        else:
            print(elemValid)
            return False
    except TimeoutError as ErrTimeOut:
        print('elemento não encontrado /n', str(ErrTimeOut))
        return False
    except Exception:
        #print(Err.__traceback__ , '/n' , Err)
        return False
    

def closePopUp(browser, filterType, filterValue, popUpDelay):
    #Identifica PopUp
    try:
        elemPopUp = waitElementByFilterType(browser,filterType,filterValue,popUpDelay)
        if (elemPopUp!=''):
            print('PopUp encontrado')
            elemButtonPopUp = browser.find_element_by_id(filterValue)
            elemButtonPopUp.click()
        else:
            print('PopUP não encontrado')
    finally:
        return True


def waitElementByFilterType(browser, filterType,filterValue,secondDelay):
    if (filterType=='class_name'):
        return WebDriverWait(browser,secondDelay).until(
            EC.presence_of_element_located((By.CLASS_NAME,filterValue))
        )
    elif (filterType=='id'):
        return WebDriverWait(browser,secondDelay).until(
            EC.presence_of_element_located((By.ID,filterValue))
        )
    elif (filterType=='css_selector'):
        return WebDriverWait(browser,secondDelay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,filterValue))
        )
    elif (filterType=='link_text'):
        return WebDriverWait(browser,secondDelay).until(
            EC.presence_of_element_located((By.LINK_TEXT,filterValue))
        )
    