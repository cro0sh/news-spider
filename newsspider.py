from bs4 import BeautifulSoup
import scrapy
import datetime
from time import gmtime, strftime, localtime
import pandas as pd
import re

class a_time():
    def __init__(a):
        #super().__init__(zero)
        #a.zero = zero
        a.time = strftime("%Y-%m-%d %H-%M-%S", localtime())

    def get(a):
        a.time = strftime("%Y-%m-%d %H-%M-%S", localtime())
        return a.time



class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://news.google.com/?hl=en-CA&gl=CA&ceid=CA:en']
    #start_urls = ['http://www.washingtonpost.com/']

    def parse(self, response):

        a = response.css("div.mEaVNd")
        #a.css('.ZulkBc').extract()

        c = a.css('.ZulkBc').extract()  

        c = str(c)
        soup = BeautifulSoup(c, features="html.parser")

        times = a_time()
        times = times.get()
        #from time import gmtime, strftime, localtime

##        time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        
        spanz = {times:[]}
        linkz = {times:[]}

        for span in soup.find_all('span', text=False):
    #if 'Land area' in dt.text:
            yield({times: span.contents})
            spanz[times].append(span.contents)
        spanz_new = {times:[]}
        lst_2 = []
        # for comma in spanz.values():
        for lst in spanz.values():
            for something in lst:
                for string in something:
##            print(string)
                    if ',' in string:
                        string = string.replace(',', '') 
                        new_lst = []
                        new_lst.append(string)
                        spanz_new[times].append(new_lst)
                        #lst_2.append(string)
                        #spanz_new[times].append(lst)
                        #spanz_new[times].append(string)
                    else:
                        new_lst = []
                        new_lst.append(string)
                        spanz_new[times].append(new_lst)
                        #lst_2.append(string)
                        
                        #spanz_new[times].append(lst)
                        #spanz_new[times].append(string)    
        #for item in lst_2:
        #    spanz_new[times].append(item)
        new_linkz = {times:[]}
        for link in soup.findAll('a', attrs={'href': re.compile("^./articles/")}):
            #linkz = { times: (link.get('href')) }
            yield({ times: (link.get('href')) })
            linkz[times].append(link.get('href'))

        for z in linkz.values():
            for z1 in z:
                if '.' in z1:
                    z1 = z1.replace('.', 'https://news.google.com')
                    new_linkzz = []
                    new_linkzz.append(z1)
                    new_linkz[times].append(new_linkzz)
        #import pandas

        df = pd.DataFrame({'Headline': spanz_new[times], 'Link': new_linkz[times]})
        filename = times + ' news' + '.csv'
        df.to_csv(filename, sep='\t', encoding='utf-8')

class filter_news():
    def __init__(a):
        pass
        #super().__init__(zero)
        #a.zero = zero
        #a.time = strftime("%Y-%m-%d %H:%M:%S", localtime())

    def filter(a):

        import csv

        interest = ['celery', 'implant']

        with open("goognews.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                for something in row:
                    for z in interest:
                        if z in something:
                            print(something)
        #a.time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        #return a.time