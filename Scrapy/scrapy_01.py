import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['heeps://blog.scrpainghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a :: text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)