
from bs4 import BeautifulSoup
import requests


url="http://noc.org.np/retailprice"
html_content = requests.get(url).text



soup = BeautifulSoup(html_content, 'lxml')

price_table = soup.find("table")

price_table_data = price_table.tbody.find_all("tr")

current_price_data = []
price_dict = {}

for td in price_table_data[0].find_all("td"):
    current_price_data.append(td.text.replace('\n', ' ').strip())

for data in current_price_data:
    price_dict['date'] = current_price_data[0]
    price_dict['petrol'] = current_price_data[1]
    price_dict['diesel'] = current_price_data[2]
    price_dict['kerosene'] = current_price_data[3]
    price_dict['LPG'] = current_price_data[4]
    price_dict['ATF (DP)'] = current_price_data[5]
    price_dict['ATF (DF)'] = current_price_data[6]

print(price_dict)