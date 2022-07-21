
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#Importing Selenium because Splinter refuses to operate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def scrape_all():
    # Initiate headless driver for deployment

    # Grabbing executable path
    executable_path = {'executable_path': 'C:/Users/kinto/.wdm/drivers/chromedriver/win32/103.0.5060.134/chromedriver.exe'}
    executable_path


    #Setting up Selenium since Splinter refuses to work
    options = Options()
    options.headless = True
    browser = webdriver.Chrome('C:/Users/kinto/.wdm/drivers/chromedriver/win32/103.0.5060.134/chromedriver.exe')

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_new(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.get(url)

    # Optional delay for loading the page
    browser.implicitly_wait(1)





    html = browser.page_source
    news_soup = soup(html, 'html.parser')
    
        # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    
    
    slide_elem = news_soup.select_one('div.list_text')


    slide_elem.find('div', class_='content_title')



    # Use the parent element to find the first `a` tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
    





    # Use the parent element to find the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    return news_title, news_p




def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.get(url)


    # Find and click the full image button
    full_image_elem = browser.find_elements(By.TAG_NAME, 'button')[1]
    full_image_elem.click()



    html = browser.page_source
    # Parse the resulting html with soup
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    img_url_rel



    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url


# ## Mars Facts
def mars_facts():

    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    df = pd.read_html('https://galaxyfacts-mars.com')[0]
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    df.to_html()

    browser.quit()



