import unittest
from loteriacaixa.capturewebdata.connectbrowser import connectEdge
from selenium import webdriver

class TestConnectEdge(unittest.TestCase):
    def test_connectEdge(self):
        browser = connectEdge()
        self.assertIsInstance(browser, webdriver.Edge)

if __name__ == '__main__':
    unittest.main()