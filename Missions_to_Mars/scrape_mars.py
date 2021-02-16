#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def scrape():
    # Setup splinter
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)
    

    #Get nasa news article
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)

    #Setting variables for the top news story
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.body.find('div', class_='bottom_gradient').text
    news_p = soup.body.find('div', class_='article_teaser_body').text

    #Getting table from mars-facts
    url_m = 'https://space-facts.com/mars/'
    tables = pd.read_html(url_m)
    tables_dict = {}
    
    
    for i in range(0, len(tables)):
        iterator = str(i)
        key = "Dataframe"+iterator
        tables_dict[key] = tables[i]

    frame_dict = {}
#debugging the key error for Mongo
    for key, frame in tables_dict.items():
        key = key
        frame = frame.to_dict()
            for key, value in frame.items():
                key = "Column"
                for key, valu in value.items():
                    key = "Row"
        frame_dict[key] = frame

    #urls for the Mars Hemisphere images
    hemisphere_images = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
    ]   

    #dictionary for everything
    mars = {"top_story_title": news_title, "top_story_blurb": news_p, "tables": frame_dict, "hemi_images": hemisphere_images}
    
    #return mars
    return frame_dict

print(scrape())