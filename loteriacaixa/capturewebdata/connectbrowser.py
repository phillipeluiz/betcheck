#! python3
# Login empiricus
import time

def connectfirefox():
    try:
        
        from selenium import webdriver
        
        # Ajustes para resolver um problema com o PATH do windows para o driver geckodriver do firefox selenium
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')    
        browser  = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\geckodriver.exe')
        
        return browser

    except Exception as Err:
        return False
       # print(str(Err.__traceback__) + '\n' + str(Err))
    #finally:
    #    print('finally')