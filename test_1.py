from testpage import Operations
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
    testpage.header_about()
   
    