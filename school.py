from constants import voice_to_text
from constants import print_say

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time as t

#chrome_driver_path = r
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://mysso.centennialcollege.ca/authenticationendpoint/login.do?commonAuthCallerPath=%2Fsamlsso&forceAuth=false&passiveAuth=false&tenantDomain=carbon.super&sessionDataKey=da67790b-83f1-4263-8c47-fa80a12b96aa&relyingParty=https%3A%2F%2F85b3260b-38d2-4f57-8b10-d2a6357af260.tenants.brightspace.com%2FsamlLogin&type=samlsso&sp=D2LPROD&isSaaSApp=false&authenticators=BasicAuthenticator%3ALOCAL")
# driver.maximize_window()
#
# username = "301171884"
# password = "030200"