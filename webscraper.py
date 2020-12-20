import requests
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

############### MONSTER.COM #####################
# Getting info from static monster.com page
# URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=Oregon'
# page = requests.get(URL)

# # Parse the html with beautifulsoup
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find(id='ResultsContainer')

# # Get all job postings from the page
# jobs = results.find_all('section', class_='card-content')

# # Extract the title, company, and location of each job and print
# for job in jobs:
#     title = job.find('h2', class_='title')
#     company = job.find('div', class_='company')
#     location = job.find('div', class_='location')
#     # Print each element if they are not empty
#     if title is not None:
#         print(title.text.strip())
#     if company is not None:
#         print(company.text.strip())
#     if location is not None:
#         print(location.text.strip())

#     # Include link to the post, if one exists
#     link = job.find('a')
#     if link is not None:
#         link = job.find('a')['href']
#         print(f"Apply here: {link}\n")
#     print()

# print('Enter email : ', end ='') 
# email = input().strip() 
# print('Enter password : ', end ='') 
# password = input().strip() 

############### ZIPPIA.COM ##################
# Get user login info
print('Enter email id : ', end ='') 
email = input().strip() 
print('Enter password : ', end ='') 
passwd = input().strip()

URL = 'https://www.zippia.com/matches/'
driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')
driver.get(URL)

# Save main page to switch back to later
main_page = driver.current_window_handle 

driver.implicitly_wait(5)
login_btn = driver.find_element_by_class_name("loginButton")
login_btn.click()

####### LOGIN WITH EMAIL AND PASSWD #########
# driver.find_element_by_xpath('//*[@id="__next"]/header/div[3]/div/div/div[2]/div/form/div/input[1]').send_keys(email)
# driver.find_element_by_xpath('//*[@id="__next"]/header/div[3]/div/div/div[2]/div/form/div/input[2]').send_keys(passwd)
# driver.find_element_by_xpath('//*[@id="__next"]/header/div[3]/div/div/div[2]/div/form/div/button').click()


######### LOGIN WITH GOOGLE ############
driver.implicitly_wait(5)
# Click Google login button
google_login = driver.find_element_by_class_name('login-btn-goog')
google_login.click()

# changing the handles to access login popup page 
for handle in driver.window_handles: 
    if handle != main_page: 
        login_page = handle 
          
# change the control to login page         
driver.switch_to.window(login_page)

driver.implicitly_wait(3)
# Enter user's email
input_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
input_email.send_keys(email)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

driver.implicitly_wait(3)
# Enter user's password and log in
input_passwd = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
input_passwd.send_keys(passwd)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

# Go back to main page
driver.switch_to.window(main_page)


driver.implicitly_wait(3)
# Go to the My Jobs tab
driver.find_element_by_xpath('//*[@id="__next"]/header/nav/div/div[2]/ul/li[1]/span').click()

driver.implicitly_wait(3)
jobSearch = driver.find_element_by_id('jobSearch')
jobSearch.send_keys('Software Engineer')
jobSearch.send_keys(Keys.ENTER)

locationDD = driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div[1]')
locationDD.click()
# Select work from home option
driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/span').click()
locationInput = driver.find_element_by_xpath('//*[@id="locationNameMultiFilter59f55046-b7b0-4dcd-9711-b38707f597bf"]')
locationInput.send_keys('Oregon')
locationInput.send_keys(Keys.ENTER)
# Apply location filters
driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[2]/span')

jobLevelDD = driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div/div[1]/div[2]/div/div[2]/div[4]/div/div[1]')
jobLevelDD.click()
# Select the entry level option
driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div[2]/div[2]/div/div[1]/div/span').click()
# Apply job level filter
driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div/div[1]/div[2]/div[2]/div[2]/div[4]/div/div[2]/div[2]/div[3]/div[2]/span').click()

datePostedDD = driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div/div[1]/div[2]/div/div[2]/div[6]/div/div[1]')
datePostedDD.click()
# Select past week option
driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div/div[1]/div[2]/div[2]/div[2]/div[6]/div/div[2]/div[2]/div[2]/div/div[3]').click()
# Apply data filter
driver.find_element_by_xpath('//*[@id="matchesSection"]/div/div/div[1]/div[2]/div/div[2]/div[6]/div/div[2]/div[2]/div[3]/div[2]/span').click()