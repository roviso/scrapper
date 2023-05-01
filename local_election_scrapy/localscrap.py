
from bs4 import BeautifulSoup
import requests


url="https://sthaniya.gov.np/gis/website/webdataquery.php?province=0"
html_content = requests.get(url).text



soup = BeautifulSoup(html_content, 'lxml')

local_table = soup.find_all("table")

final_local_election = []


for table in local_table:
    local_election_data = table.tbody.find_all("tr")
    for table_data in local_election_data:
        local_election = []
        election_dict = {}
        for td in table_data.find_all("td"):
            data_extracted = td.text.replace('\n', ' ').strip()
            local_election.append(data_extracted)
        print(local_election)

        election_dict['S.N'] = local_election[0]
        election_dict['local_election_name'] = local_election[1]
        election_dict['district'] = local_election[2]
        election_dict['election_type'] = local_election[3]
        election_dict['pradesh'] = local_election[4]
        election_dict['bewosachit'] = local_election[5]
        election_dict['kaifiyat'] = local_election[6]

        final_local_election.append(election_dict)

print(final_local_election)