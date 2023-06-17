from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

class BasePage:
    def __init__(self, driver):
      self.address = "https://test-stand.gb.ru"
      self.driver = driver
               
    def start_browser(self):
        try:            
            self.driver.get(self.address)
        except:
            logging.exception('Ошибка при открытии')
            

    def find_element(self, locator, time = 10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                         message= f'Cant find element by locator{locator}')
        except:
            logging.exception('Элемент не найден')
            return None


    def get_element_property(self, locator, property):
        try:
            element = self.find_element(locator)
            return element.value_of_css_property(property)
        except:
            logging.exception('Свойство не найдено')
            return None
        

    def go_to_site(self):
        try:
            return self.driver.get(self.address)
        except:
            logging.exception('Страница не найдена') 
            return None
        
    
