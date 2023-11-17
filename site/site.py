import requests
from bs4 import BeautifulSoup
import re
import pprint


url = 'https://fcdlmg.org.br/posicionamento-da-fcdl-mg-sobre-portaria-que-altera-trabalho-no-comercio-aos-domingos-e-feriados/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html,'html.parser')

notice = parsed_html.select_one('#wrapper > main > div > div > div > div.col-lg-8 > div > h2')
article = notice.parent

for p in article.select('p'):
    print(re.sub(r'\s{1,}', ' ', p.text).strip())

