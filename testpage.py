from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
        
    for i in locators['xpath'].keys():
        ids[i] = (By.XPATH, locators['xpath'][i])  
         
    for i in locators['css'].keys():
        ids[i] = (By.CSS_SELECTOR, locators['css'][i])   


class Operations(BasePage, TestLocators):
    
    with open('./testdata.yaml') as f:
        data = yaml.safe_load(f)
        
        
    def enter_login(self):
        logging.debug('Enter login')
        input1 = self.find_element(self.ids["LOCATOR_LOGIN"])
        input1.clear()
        if input1:
            input1.send_keys(self.data["username"])
        else:
            logging.error('Поле для ввода логина не найдено')
            
            
    def enter_pass(self):
        logging.debug('Enter password')
        input2 = self.find_element(self.ids["LOCATOR_PASS"])
        input2.clear()
        if input2:
            input2.send_keys(self.data["password"])
        else:
            logging.error('Поле для ввода пароля не найдено')
            

    def click_login_button(self):
        logging.debug('Click login button')
        btn = self.find_element(self.ids['LOCATOR_LOGIN_BTN'])
        if btn:
            btn.click()
        else:
            logging.error('Кнопка не найдена')
            
    
    def click_about_button(self):
        logging.debug('Click about button')
        btn2 = self.find_element(self.ids['LOCATOR_ABOUT_BTN'])
        if btn2:
            btn2.click()
        else:
            logging.error('Кнопка "About" не найдена')
            
    def header_about(self):
        logging.debug('Header size check')
        h_about = self.find_element(self.ids['HEADER_ABOUT']).value_of_css_property('font-size')
        return h_about    
        