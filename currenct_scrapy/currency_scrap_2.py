
from bs4 import BeautifulSoup
import requests


url="https://www.nrb.org.np/forex"
html_content = requests.get(url).text



soup = BeautifulSoup(html_content, 'lxml')
curency_table = soup.find_all("table")


# currency_dict = {}
final_currency_exchange = []


for table in curency_table:
    price_table_data = table.tbody.find_all("tr")

    for table_data in price_table_data:
        currency_exchange = []
        currency_dict = {}
        for td in table_data.find_all("td"):
            data_extracted = td.text.replace('\n', ' ').strip()
            currency_exchange.append(data_extracted)


        currency_dict['country'] = currency_exchange[0]
        currency_dict['Unit'] = currency_exchange[1]
        currency_dict['Buy'] = currency_exchange[2]
        currency_dict['Sell'] = currency_exchange[3]

        final_currency_exchange.append(currency_dict)

print(final_currency_exchange)