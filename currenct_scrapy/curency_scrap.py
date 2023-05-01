
from bs4 import BeautifulSoup
import requests


url="https://www.ashesh.com.np/forex/widget2.php?api=63223444h04546637"
html_content = requests.get(url).text



soup = BeautifulSoup(html_content, 'lxml')

country_name = soup.find_all("div", {"class": "name"})
rate_selling = soup.find_all("div", {"class": "rate_selling"})
rate_buying = soup.find_all("div", {"class": "rate_buying"})
unit = soup.find_all("div", {"class": "unit"})

nepal_exchange_rates = {}
nepal_exchange_rates_list = []

for country,sell,buy,unit in zip(country_name,rate_selling,rate_buying,unit):
    nepal_exchange_rates['country'] = country.text.replace('\n', ' ').strip()
    nepal_exchange_rates['rate_selling'] = sell.text.replace('\n', ' ').strip()
    nepal_exchange_rates['rate_buying'] = buy.text.replace('\n', ' ').strip()
    nepal_exchange_rates['unit'] = unit.text.replace('\n', ' ').strip()
    nepal_exchange_rates_list.append(nepal_exchange_rates)
    

print(nepal_exchange_rates_list)
