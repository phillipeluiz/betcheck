#! python3
# Login empiricus
import time

def connectFireFox():
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
        binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')    
        browser  = webdriver.Firefox(firefox_binary=binary, executable_path=r'C:\\Drivers\\geckodriver.exe')
        return browser
    except Exception as Err:
        print(str(Err.__traceback__) + '\n' + str(Err))
        raise


    
def connectEdge():
    try:
        from selenium import webdriver
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        browser = webdriver.Edge(options=options)
        #browser = webdriver.Chrome('C:\\Drivers\\msedgedriver.exe')

        if not isinstance(browser, webdriver.Edge):
            raise Exception('Failed to initialize Edge WebDriver')
        return browser
    except Exception as Err:
        print(str(Err.__traceback__) + '\n' + str(Err))
        raise