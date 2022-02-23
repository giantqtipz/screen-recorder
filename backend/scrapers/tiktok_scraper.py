from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from recorder.recorder import record

import time

def tiktok_scraper(url, duration):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.implicitly_wait(5)
    driver.get(url)
    driver.maximize_window()

    close_button_xpath = '/html/body/div[7]/div/div[1]/div[1]'
    driver.find_element(By.XPATH, close_button_xpath).click()
    
    video_xpath = '/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]'
    driver.find_element(By.XPATH, video_xpath).click()

    driver.implicitly_wait(5)
    tiktok_handle_xpath = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/a[2]/span[1]'
    tiktok_handle_text = driver.find_element(By.XPATH, tiktok_handle_xpath).text

    # tiktok_nickname_xpath = '/html/body/div[2]/div[2]/div[3]/div[2]/div[1]/a[2]/span[2]'
    # tiktok_nickname_text = driver.find_element(By.XPATH, tiktok_nickname_xpath).text

    record(tiktok_handle_text, duration)

    time.sleep(duration)

    # driver.close()
    # driver.quit()

    # return tiktok_handle_text