from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def webdriver_launch():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    return driver