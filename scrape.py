from bs4 import BeautifulSoup
from selenium import webdriver
import time

browser = webdriver.Chrome()
for place in ["Cuba", "Belgum", "France"]:
    url = ("https://www.google.nl/destination/compare?site=destination&output=search")
    browser.get(url) # you may not need to do this every time if you clear the search box
    time.sleep(2)
    element = browser.find_element_by_name('q') # get the query box
    time.sleep(2)
    element.send_keys(place) # populate the search box
    time.sleep (2)
    search_box=browser.find_element_by_class_name('sbsb_c') # get the first element in the list
    search_box.click() # click it
    time.sleep (2)
    destinations=browser.find_element_by_id('DESTINATIONS') # Click the destinations link
    destinations.click()
    time.sleep (2)
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "lxml")
    # Get the headings
    hs = [tag.text for tag in soup.find_all('h2')]
    # get the text containg divs
    divs = [tag.text for tag in soup.find_all('div', {'class': False})]
    # Delete surplus divs
    del divs[:22]
    del divs[-1:]
    print(list(zip(hs,divs)))

browser.quit()