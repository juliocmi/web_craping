# Title Project: Web Scraping to Haker News
# Created by   : Julio Martínez
# Position     : Data Scientist
# Date         : 03/07/24
#------------------------------------------


# Importing libraries
import requests
from bs4 import BeautifulSoup

# Creating header
# URL definition
header = {
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/126.0.6478.114 Safari/17.4.1",
}
url = 'https://news.ycombinator.com/'

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'lxml')

news_list = soup.find_all("tr", class_="athing")

for news in news_list:

    title = news.find('span', class_='titleline').text
    url   = news.find('span', class_='titleline').find('a').get('href')
    metadata = news.find_next_sibling()

    score = 0
    comments = 0
    
    # try - except block to the files with no comments
    try:
        score_tmp = metadata.find('span', class_='score').text
        score_tmp = score_tmp.replace('points', '').strip()
        score = int(score_tmp)
    except:
        print('no hay score')
    print(score)

    try:
        comments_tmp = metadata.find('span', attrs={'class':'subline'}).text
        comments_tmp = comments_tmp.split('|')[-1]
        comments = comments_tmp.replace('comments', '').strip()
    except:
        print('no hay titulos')

    print(title)
    print(url)
    print(score)
    print(comments)

    print()


