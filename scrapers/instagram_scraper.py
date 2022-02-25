from selenium.webdriver.common.by import By
from recorder.recorder import record
import time

def instagram_scraper(driver, url, duration):

    driver.implicitly_wait(5)

    driver.get(url)

    play_button_xpath = '/html/body/div[1]/section/main/div/div/article/div/div[1]/div/div/div[3]'
    play_button_click = driver.find_element(By.XPATH, play_button_xpath).click()

    # unmute_xpath = '/html/body/div[1]/section/main/div/div[1]/article/div/div[1]/div/div/div[4]/button'
    # unmute_click = driver.find_element(By.XPATH, unmute_xpath).click()

    driver.implicitly_wait(5)

    instagram_handle_xpath = '/html/body/div[1]/section/main/div/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/div'
    instagram_handle_text = driver.find_element(By.XPATH, instagram_handle_xpath).text

    time.sleep(duration)

    record(instagram_handle_text, duration)

    # return instagram_handle_text