'''Configuration for Environments'''
import os


# URLs
E_LIBRARY_LOGIN = 'http://elibrary.judiciary.gov.ph/elibsearch'

# Folder Path
_curr_dir = os.getcwd()
_parent_dir = os.path.dirname(_curr_dir)
GECKO_DRIVER_PATH = os.path.join(_parent_dir, 'drivers', 'geckodriver')
CHROME_DRIVER_PATH = os.path.join(_parent_dir, 'chromedriver', 'chromedriver')