from testpage import Operations
from testpage import BasePage
import logging
import time


def test_step1(browser):
    
    logging.info('Starting')
    testpage = Operations(browser)
    testpage.go_to_site()
    testpage.enter_login()
    testpage.enter_pass()
    testpage.click_login_button()
    testpage.click_about_button()
    time.sleep(2)
    testpage.get_about_page_text()
    testpage.check_about_page_title_font_size()

   
# def test_page_loading(browser, about_page):
#     page = Operations(browser)
#     page.click_about_button()
#     assert page.get_about_page_text() == about_page, \
#         'Страница About не загружается'


# def test_font_size(browser, font_size):
#     page = Operations(browser)
#     assert page.check_about_page_title_font_size(font_size), \
#         f'Шрифт заголвка About Page не равен {font_size}'