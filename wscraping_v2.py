# Web Scraping para Stack Overflow

import requests
from bs4 import BeautifulSoup

# create header
header = {
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

# url seed
url = 'https://stackoverflow.com/questions'
response = requests.get(url, headers=header)

# parser tree
soup = BeautifulSoup(response.text)

# OBJECTIVE: EXTRACT THE TITLES AND DESCRIPTIONS TO EVERY QUESTION IN THE PRINCIPAL PAGE OF STACK OVERFLOW
quest_container = soup.find(id="questions")
questions_list  = quest_container.find_all('div', class_="s-post-summary")

# finding all titles and descriptions
for question in questions_list:
    question_text  = question.find("h3").text
    quest_descript = question.find(class_="s-post-summary--content-excerpt")
    if quest_descript:
        quest_descript = quest_descript.text
    else:
        quest_descript = "description not found"
    quest_descript = quest_descript.replace('\n','').replace('\r','').strip()
    print(question_text)
    print(quest_descript)

    print()