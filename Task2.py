#!/usr/bin/env python
# coding: utf-8


#Task 2

#import required library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import bs4
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options

def scrap(url):
     # installing driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=Options())

    # creating dicitonary for storing data
    details = {
        'Security Name' : [],
        'Symbol':[],
        'Shares':[],
        'Weight(%)':[],
        '52 Wk Change(%)':[]
    } 
    print('Please wait....')
    # request on webpage
    driver.get(url)
    time.sleep(7)
    
    #total no. of pages
    soup = bs4.BeautifulSoup(driver.page_source,'html.parser')
    all_pages =  int(soup.find_all('a',attrs={'class':'paginate_button'})[-2].text)
    
    #getting data from each page
    for page in range(all_pages):
        #getting source code of page
        source_code = bs4.BeautifulSoup(driver.page_source,'html.parser')
        
        #Accessing table data
        data =source_code.find('section',id="etf_holding_details").find('div',attrs={'class':'DTFC_ScrollWrapper'})
        table = data.find_all('table',attrs={'aria-describedby':"etf_holding_table_info"})[0].tbody

        # all rows of table
        rows = table.find_all('tr')

        #getting data from each row
        for row in rows:
            colums = row.find_all('td')
            # getting data from each column and store it
            for col,key in zip(colums,details):
                details[key].append(col.text.strip('.'))

        #click on next page
        try:
            if page < all_pages-1:
                driver.find_element_by_xpath('//*[@id="etf_holding_table_next"]').click()
        except:
            driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/section[2]/div/div/div[3]/div[3]/a[2]')
            
        print('Page no. ',page+1,'scrap')
    
    #convert in csv file    
    details = pd.DataFrame(details)
    details.to_csv('veu.csv',index=False)   
    
if __name__ == '__main__':
    url = 'https://www.zacks.com/funds/etf/veu/holding'
    scrap(url)
    print('Finished...')

