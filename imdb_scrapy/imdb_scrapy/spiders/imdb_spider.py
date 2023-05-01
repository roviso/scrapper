import scrapy

from imdb_scrapy.items import ImdbScrapyItem


class ImdbSpider(scrapy.Spider):
    name = "imdbChor"

    def start_requests(self):
        urls = [
            'https://www.imdb.com/title/tt9288030/?ref_=nv_sr_srsg_0',
            'https://www.imdb.com/title/tt11192306/?ref_=nv_sr_srsg_0',
            'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=9NEN4V13TK60MK8C5MVR&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        item = ImdbScrapyItem()

        item['title'] = response.xpath("//div[contains(@class, 'TitleBlock__Container-sc-1nlhx7j-0') and contains(@class, 'hglRHk')]//h1//text()").getall()[0]
        item['url'] =  response.request.url



        item['info'] = response.xpath("//div[contains(@class, 'TitleBlock__Container-sc-1nlhx7j-0') and contains(@class, 'hglRHk')]//div[contains(@class, 'TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2') and contains(@class, 'hWHMKr')]//li//text()").getall() 
        item['imdb_rating'] = response.xpath("//div[contains(@class, 'RatingBar__ButtonContainer-sc-85l9wd-1')]//span[contains(@class, 'AggregateRatingButton__RatingScore-sc-1ll29m0-1')]/text()").getall()[0]
        item['cover'] = 'https://www.imdb.com/' + response.xpath("//div[contains(@class, 'Media__PosterContainer-sc-1x98dcb-1')]//a[contains(@class, 'ipc-lockup-overlay')]/@href").getall()[0]
        item['genres'] = response.xpath("//div[contains(@class, 'GenresAndPlot__ContentParent-sc-cum89p-8')]//a//span//text()").getall()
        item['plot'] = response.xpath("//div[contains(@class, 'GenresAndPlot__ContentParent-sc-cum89p-8')]//p//text()").getall()[0]
        item['creator'] = response.xpath("//div[contains(@class, 'PrincipalCredits__PrincipalCreditsPanelWideScreen-sc-hdn81t-0')]//div[contains(@class, 'ipc-metadata-list-item__content-container')]")[0].css("::text").getall()
        item['stars'] = response.xpath("//div[contains(@class, 'PrincipalCredits__PrincipalCreditsPanelWideScreen-sc-hdn81t-0')]//div[contains(@class, 'ipc-metadata-list-item__content-container')]")[1].css("::text").getall()


        yield item