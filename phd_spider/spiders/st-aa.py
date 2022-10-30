import scrapy


class STAASpider(scrapy.Spider):
    name = "st-aa"
    start_urls = ['https://aa.stanford.edu/people/faculty']

    def parse(self, response):
        links = response.css('li.su-padding-bottom-3 a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_profile)
    
    def parse_profile(self, response):
        title = 'professor'
        field = ''
        name = ''
        mm = response.xpath('//head/meta')
        for m in mm:
            if m.xpath('@property').get() == 'og:title':
                name = m.xpath('@content').get()
            if m.xpath('@name').get() == 'description':
                t = m.xpath('@content').get()
                if ('Associate professor' in t) or ('associate professor' in t) or ('Associate Professor' in t) or ('associate Professor' in t):
                    title = 'associate professor'
                if ('Assistant professor' in t) or ('assistant professor' in t) or ('Assistant Professor' in t) or ('assistant Professor' in t):
                    title = 'assistant professor'
                if ('robot' in t) or ('Robot' in t):
                    field = ' robot'
                if ('learning' in t) or ('Learning' in t):
                    field = f'{field} learning'
                if ('control' in t) or ('Control' in t):
                    field = f'{field} control'
        yield {
            'name': name,
            'field': field,
            'title': title,
        }
        # name = response.url.split('-')[-1]
        # filename = f'{name}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}'import scrapy


class QuotesSpider(scrapy.Spider):
    name = "st-aa"
    start_urls = ['https://aa.stanford.edu/people/faculty']

    def parse(self, response):
        links = response.css('li.su-padding-bottom-3 a::attr(href)').getall()
        for link in links:
            yield response.follow(link, callback=self.parse_profile)
    
    def parse_profile(self, response):
        title = 'professor'
        field = ''
        name = ''
        mm = response.xpath('//head/meta')
        for m in mm:
            if m.xpath('@property').get() == 'og:title':
                name = m.xpath('@content').get()
            if m.xpath('@name').get() == 'description':
                t = m.xpath('@content').get()
                if ('Associate professor' in t) or ('associate professor' in t) or ('Associate Professor' in t) or ('associate Professor' in t):
                    title = 'associate professor'
                if ('Assistant professor' in t) or ('assistant professor' in t) or ('Assistant Professor' in t) or ('assistant Professor' in t):
                    title = 'assistant professor'
                if ('robot' in t) or ('Robot' in t):
                    field = ' robot'
                if ('learning' in t) or ('Learning' in t):
                    field = f'{field} learning'
                if ('control' in t) or ('Control' in t):
                    field = f'{field} control'
        yield {
            'name': name,
            'field': field,
            'title': title,
        }
        # name = response.url.split('-')[-1]
        # filename = f'{name}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}'))