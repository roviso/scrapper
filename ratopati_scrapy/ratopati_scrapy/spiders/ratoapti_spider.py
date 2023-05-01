import scrapy
from urllib import parse
from ratopati_scrapy.items import RatopatiScrapyItem
from sharedcountsdk import SharedCountApi
import datetime
import nepali_datetime
import csv
from tqdm import tqdm

def date_splitter(date):
    number_dictionary = {'०':0, '१':1, '२':2, '३':3, '४':4, '५':5, '६':6, '७':7, '८':8, '९':9}
    month_dictionary = {'वैशाख': 1, 'बैशाख':1,'ज्येष्ठ': 2 , 'जेठ':2,'आषाढ़': 3, 'असार': 3, 'श्रावण': 4 , 'साउन': 4,
            'भाद्रपद': 5, 'भदौ': 5, 'असोज': 6, 'आश्विन': 6,'कात्तिक':7, 'कार्तिक':7 , 'मंसिर':8, 'मार्गशीर्ष':8, 'पुष':9,'पुस':9, 'पौष':9,
            'माघ':10, 'फागुन':11, 'फाल्गुण':11, 'चैत':12 , 'चैत्र': 12}
    date_list = date.split(',')
    year = str(date_list[1]).strip()
    year = int(''.join(str(number_dictionary[x]) for x in year))
    month = int(str(month_dictionary[date_list[0].split()[0]]).strip())
    day = str(date_list[0].split()[1]).strip()
    day = int(''.join(str(number_dictionary[x]) for x in day))
    return nepali_datetime.date(year,month,day)

def date_getter(published_date):
    todays_date = nepali_datetime.date.today()
    day_passed = nepali_datetime.date.today() - published_date
    day_passed = day_passed.days
    return day_passed

class ratopati(scrapy.Spider):
    name = 'ratopatiChor'
    allowed_domains = ['ratopati.com']
    start_urls = ['https://ratopati.com/']
    

    # def start_requests(self):
    #     with open("/content/gdrive/MyDrive/workaholic/news_recommendation/news_scraper/ratopati_scapper/ratopati_scapper/ratopati_updated.csv", "rU") as f:
    #             reader=csv.DictReader(f)
    #             i = 0 
            
    #             for row in reader:

    #                 url=row['0']
    #                 # Change the offset value incrementally to navigate through the product list
    #                 # You can play with the range value according to maximum product quantity
    #                 link_urls = [url]
    #                 i += 1

    #                 for link_url in link_urls:

    #                   print('------------link_url___________________--------------------------',link_url)

    #                   request=scrapy.Request(link_url, callback=self.parse_article)
    #                   yield request

    def start_requests(self):
        traverse_urls = ['http://ratopati.com/story/' + str(page) for page in list(range(190530,212220))]
        # coookie_dict={'__asc': 'e2ac80d317db7259b5ec491eced', '__auc': 'da1df9a117b4dfe2b271b56c078',
        #             '__cf_bm': '9Q6TVbNCbifk..GtUnyu7SGtWrIRmHlVR02MMImEBJk-1639455235-0-AR3qHH3/M62wQV25PQ7mEAYZi6SSJIU+e32sp0NMjOWtBKX5YKNwIcYWBb22YTP1j1uuqL0L1Ew/ycxK3PKvQ0DZgEHSJ4a0fK+B/muGIu0GVi+q4D45ET1dfFUVk00LEw==',
        #             '_gat': '1', 
        #             '_ga': 'GA1.2.300954166.1629101122',
        #             '_gid': 'GA1.2.487732953.1639388202',
        #             'userid': '2134e04e24b5951982b9372c825efc86'}
        for i,link_url in tqdm(enumerate(traverse_urls)):
            print(f"{i}. {link_url}")
            request=scrapy.Request(link_url,callback=self.parse_article)
            yield request


    def parse_article(self,response):
        access_time = response.xpath("//div[contains(@class,'article-head-meta')]/span[contains(@class,'meta-item')]/descendant::text()").extract()
        publish_date = date_splitter(access_time[1])
        day_passed = date_getter(publish_date)
        # try:#dominator2rule :997ee09718596404b3e6edca59da47cf7d391f20
        #   sharedCountApiInstance = SharedCountApi('997ee09718596404b3e6edca59da47cf7d391f20')
        #   urlGetResponse = sharedCountApiInstance.get(response_url)
        #   fb_info = urlGetResponse['Facebook']
        #   shares = fb_info['total_count']
        #   comments = fb_info['comment_count']

        # except:
        #   try:#ravi.praj05: dbc159c8dcf39265dd0a5cde28cd603e0b62ced7
        #     sharedCountApiInstance = SharedCountApi('dbc159c8dcf39265dd0a5cde28cd603e0b62ced7')
        #     urlGetResponse = sharedCountApiInstance.get(response_url)
        #     fb_info = urlGetResponse['Facebook']
        #     shares = fb_info['total_count']
        #     comments = fb_info['comment_count']
        #   except:
        #     try:#ravi.praj07: 42c47e38ba96c8eb6f283a09a0ace27d44639466
        #       sharedCountApiInstance = SharedCountApi('42c47e38ba96c8eb6f283a09a0ace27d44639466')
        #       urlGetResponse = sharedCountApiInstance.get(response_url)
        #       fb_info = urlGetResponse['Facebook']
        #       shares = fb_info['total_count']
        #       comments = fb_info['comment_count']
        #     except:
        #       try:#ravi.praj08: 43238bc406280d3abc1351bf24257008924a2ca3
        #         sharedCountApiInstance = SharedCountApi('42c47e38ba96c8eb6f283a09a0ace27d44639466')
        #         urlGetResponse = sharedCountApiInstance.get(response_url)
        #         fb_info = urlGetResponse['Facebook']
        #         shares = fb_info['total_count']
        #         comments = fb_info['comment_count']
        #       except:
        #         try:#ravi@prixa.org: 92c43723aa3d1ecf90a507861fcf8b227b121c38
        #           sharedCountApiInstance = SharedCountApi('92c43723aa3d1ecf90a507861fcf8b227b121c38')
        #           urlGetResponse = sharedCountApiInstance.get(response_url)
        #           fb_info = urlGetResponse['Facebook']
        #           shares = fb_info['total_count']
        #           comments = fb_info['comment_count']
        #         except:
        #             shares = '_'
        #             comments = '_'
        shares = '_'
        comments = '_'



        response_url = response.request.url
        print(f"ursl is : {response_url} 11111111111111111111111111111111111111111111111111111111111111111111111")
        item = RatopatiScrapyItem()
        item['url'] = response_url
        item['heading'] =  response.xpath("//div[contains(@class,'article-head')]/h1/descendant::text()").extract()
        item['content'] = " ".join(response.xpath("//div[contains(@class, 'ratopati-table-border-layout')]//p/text()").extract()).strip()
        item['date'] = date_splitter(access_time[1])
        #item['comments'] = int(response.xpath("//div[contains(@class,'article-head-meta')]/a[contains(@class,'meta-item')]/text()").extract()[0])
        item['shares'] = shares
        item['comments'] = comments
        item['label'] = response.xpath("//div[4]/main/div/div/div[1]/nav/ol/li[2]/a/text()").extract()[0]
        yield item

# scrapy crawl ratopatiChor -O ratopati_2021_2.csv
# //div[4]/main/div/div[3]/div[1]/div/div[1]/div[1]/div[1]/div[1]/span[2]