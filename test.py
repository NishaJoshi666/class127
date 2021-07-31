from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

starturl = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome('/Users/pc/Downloads/chromedriver_win32')
browser.get(starturl)
time.sleep(10)

def scrape():
    headers = ['name','light_years_from_earth','planet_mass','steller_magnitute','discovery_date']
    planetdata = []
    soup = BeautifulSoup(browser.page_source,'html.parser')
    for ultag in soup.find_all('ul',attrs = {'class','exoplanet'}):
        templist = []
        for index,litag in enumerate(litag):
            if(index == 0):
                templist.append(litag.find_all('a')[0].contents[0])
            else:
                try:
                    templist.append(litag.contents[0])
                except:
                    templist.append('')
        
        planetdata.append(templist)

    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('Scrapper.csv','w')as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetdata)

scrape()