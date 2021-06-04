# Packaged Libraries
#from selenium import webdriver

# Configurations
from config import GECKO_DRIVER_PATH
from config import E_LIBRARY_LOGIN

# Custom Classes
from vpn_connectors import ConnectNordVPN


def login(username, password):

    #profile = webdriver.FirefoxProfile()
    #profile.set_preference("general.useragent.override", "New user agent")
    #options = webdriver.FirefoxOptions()
    #options.headless = True
    #browser = webdriver.Firefox(firefox_profile=profile,
    #                            executable_path=GECKO_DRIVER_PATH,
    #                            options=options)
    browser.get(E_LIBRARY_LOGIN)
    browser.find_element_by_id('user_login').send_keys(username)
    browser.find_element_by_id('user_pass').send_keys(password)
    browser.find_element_by_id('submit').click()
    session_id = browser.session_id
    current_url = browser.current_url
    browser.quit()
    
    return session_id, current_url

