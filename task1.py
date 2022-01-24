#!/usr/bin/env python
# coding: utf-8


# Task1
#import required library
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import bs4
import time
from selenium.webdriver.chrome.options import Options

def export_csv(url,user,user_password):
    '''
    this function export the csv file from webpage
    
    '''
     # installing driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=Options())
    
    print('Please wait...')
    # request on webpage
    driver.get(url)

    #getting page data
    source_data = bs4.BeautifulSoup(driver.page_source,'html.parser')
    # getting address of inner iframe
    inner_frame = source_data.find('div',attrs={'class':'iframe-wrapper'}).iframe['src']

    #request on inner iframe
    driver.get(inner_frame)
    
    
    # click on "My screen"
    driver.find_element_by_xpath('//*[@id="my-screen-tab"]').click()
    time.sleep(5)
    
    #entering username 
    username = driver.find_element_by_xpath('/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/div[1]/input')
    username.send_keys(user)

    # entering password
    password = driver.find_element_by_xpath('/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/div[2]/input')
    password.send_keys(user_password)

    # click on sign in
    driver.find_element_by_xpath('/html/body/main/section/div/div[8]/section/div/div/div/section[1]/form/button').click()
    time.sleep(4)
    
    #click on Run
    driver.find_element_by_xpath('/html/body/main/section/div/div[6]/section/div/div/div/div/table/tbody/tr/td[3]/a[1]').click()
    time.sleep(5)
    
    # click on select all companies
    driver.find_element_by_xpath('/html/body/main/section/div/div[4]/div/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[1]/div/table/thead/tr/th[1]/input').click()
    time.sleep(2)
    
    #click export to cvs
    driver.find_elements_by_xpath('//*[@id="screener_table_wrapper"]/div[1]/a[1]')[0].click()

    print('Downloaded')


if __name__ == '__main__':
    url = r'https://www.zacks.com/screening/stock-screener?icid=screening-screening-nav_tracking-zcom-main_menu_wrapper-stock_screener'
    username = 'laboc57506@ampswipe.com'
    password = 'msJ$eb8EJu72@Bj'
    export_csv(url,username,password)

