# wiki scraping

import requests
from lxml import html

# creating header
encabezados = {
    
    "user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",

}

# url + response
url = 'https://www.wikipedia.org/'
respuesta = requests.get(url, headers=encabezados)

# creating parser
parser = html.fromstring(respuesta.text)

# get element by ID
ingles = parser.get_element_by_id("js-link-box-en")
print(ingles.text_content())

# get element with xpath()
ingles2 = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print(ingles2)

# get element by class with xpath
idiomas = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)

# get element by class with find_class
idiomas = parser.find_class('central-featured-lang')
for i in idiomas:
    print(i.text_content())
    