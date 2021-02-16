def scrape():
    #import dependencies
    from splinter import Browser
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager
    import pandas as pd

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
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
    

    #urls for the Mars Hemisphere images
    hemisphere_images = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"}
    ]   

    #dictionary for everything
    mars_dict = {"top_story_title": news_title, "top_story_blurb": news_p, "tables": tables, "hemi_images": hemisphere_images}
    
    return mars_dict

#print(scrape())