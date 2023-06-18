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
             
    
    def get_about_page_text(self):
        about_page = self.find_element(self.ids['HEADER_ABOUT'])
        if about_page:
            text = about_page.text
            logging.info('Указан заголовок About Page')
        else:
            logging.error('Отображается другой заголовок, не About Page')
            text = None
        return text


    def check_about_page_title_font_size(self):
        title = self.find_element(self.ids['HEADER_ABOUT'])
        font_size = title.value_of_css_property('font-size')
        if font_size == "32px":
            logging.info(f'Шрифт заголовка About Page {font_size}')
            return True
        else:
            logging.error(f'Шрифт заголовка "About" Page не равен 32px')
            return False    