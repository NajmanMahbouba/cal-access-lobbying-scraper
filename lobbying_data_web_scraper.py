#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

# Create the driver object
driver = webdriver.Chrome()
driver.implicitly_wait(10)

# Navigate to the main page containing the links/ update link for each letter and year 
driver.get("https://cal-access.sos.ca.gov/Lobbying/Employers/list.aspx?letter=A&session=2021")


# Define the link names based on letter to pick up the href attribute by name

link_names = [
    
"A BETTER WAY FORWARD TO HOUSE CALIFORNIA",
"A PLACE FOR MOM, INC.",
"A VOICE FOR CHOICE ADVOCACY, INC",
"A. O. SMITH CORPORATION",
"A. TEICHERT & SON, INC.",
"AA HOMECARE",
"AARP",
"AARP SERVICES, INC.",
"AB CARVAL INVESTORS LP",
"ABATE OF CALIFORNIA - MOTORCYCLISTS RIGHTS & SAFETY ORGANIZATION",
"ABBEY CAPITAL (US) LLC",
"ABBOTT LABORATORIES",
"ABBVIE",
"ABC CENTRAL CALIFORNIA",
"ABM INDUSTRIES INCORPORATED",
"ABRDN INC.",
"ABRY PARTNERS II, LLC",
"ABSOLUTE PHARMACY, LLC",
"ACADEMIC PARTNERSHIPS, LLC",
"ACADEMIC SENATE FOR CALIFORNIA COMMUNITY COLLEGES",
"ACADEMY OF CALIFORNIA ADOPTION-ART LAWYERS (ACAL)",
"ACADIA HEALTHCARE COMPANY INC.",
"ACADIAN ASSET MANAGEMENT LLC",
"ACCENTURE LLP"

]


# Iterate over the link_names list
for name in link_names:
    # Go back to the main page containing the links/ update link for each letter and year 
    driver.get("https://cal-access.sos.ca.gov/Lobbying/Employers/list.aspx?letter=A&session=2021")
    
    #pass each list name to find elements function and store in link_elements list 
    link_elements = driver.find_elements(By.LINK_TEXT, name)
    # click the link elements
    for link_element in link_elements:
        link_element.click()
        wait = WebDriverWait(driver, 15)
           
      
        # Add code to click the two specific buttons
       # Find the element directly by the href attribute using ID and view
    
    
        try: 
            financial_button = driver.find_element(By.XPATH, "//a[contains(@href, 'view=activity')]")
            financial_button.click()
            #print("current url", driver.current_url)
        
        
        #make an exception for when button is not found in case of an error page/ update link for each letter and year
        except NoSuchElementException: 
            driver.get("https://cal-access.sos.ca.gov/Lobbying/Employers/list.aspx?letter=A&session=2021")


        # Get the page source and create a BeautifulSoup object
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

       # print(soup)
    
    
        #convert html values to string form 
        html_str = str(soup)
        
        #search for number in strings

        if "1341" in html_str:
            print ("1341 was found: ", driver.current_url)
         
        
        # Go back to the main page containing the links
        driver.back()

# close the Selenium WebDriver
driver.quit()


# In[ ]:




