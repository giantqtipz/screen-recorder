from worksheet.worksheet import open_workbook
from scrapers.tiktok_scraper import tiktok_scraper
from scrapers.instagram_scraper import instagram_scraper

def start_application():
    urls = open_workbook('./excel/gymshark_influencers.xlsx', 'H')

    for i, cell in enumerate(urls):
        url = cell.value
        if 'tiktok' in url:
            tiktok_scraper(url, 20)
        if 'instagram' in url:
            instagram_scraper(url, 20)

start_application()