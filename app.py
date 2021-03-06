from worksheet.worksheet import open_workbook
from scrapers.webdriver_launch import webdriver_launch
from scrapers.tiktok_scraper import tiktok_scraper
from scrapers.instagram_scraper import instagram_scraper

def start_application(filename, duration):
    duration = int(duration)
    urls = open_workbook(filename, 'H')
    driver = webdriver_launch()

    driver.get('https://www.google.com')
    driver.maximize_window()

    for url in urls:
        url = url.value
        if 'tiktok' in url:
            tiktok_scraper(driver, url, duration)
        if 'instagram' in url:
            instagram_scraper(driver, url, duration)