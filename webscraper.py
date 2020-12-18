import requests
from bs4 import BeautifulSoup

# Getting info from static monster.com page
URL = 'https://www.monster.com/jobs/search/?q=Software-Engineer&where=Oregon'
page = requests.get(URL)

# Parse the html with beautifulsoup
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

# Get all job postings from the page
jobs = results.find_all('section', class_='card-content')

# Extract the title, company, and location of each job and print
for job in jobs:
    title = job.find('h2', class_='title')
    company = job.find('div', class_='company')
    location = job.find('div', class_='location')
    # Print each element if they are not empty
    if title is not None:
        print(title.text.strip())
    if company is not None:
        print(company.text.strip())
    if location is not None:
        print(location.text.strip())

    # Include link to the post, if one exists
    link = job.find('a')
    if link is not None:
        link = job.find('a')['href']
        print(f"Apply here: {link}\n")
    print()