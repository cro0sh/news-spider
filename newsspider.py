from bs4 import BeautifulSoup
import scrapy
import datetime
from time import gmtime, strftime, localtime
import pandas as pd
import re
from textblob import TextBlob

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

        #a = response.css("div.mEaVNd")
        a = response.css("div.mEaVNd")
        #a.css('.ZulkBc').extract()
        c = a.css('.DY5T1d').extract()
        # c = a.css('.ZulkBc').extract()  

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
        self.headlines = spanz_new
        #for value in headlines.values():
        #    headlines[times] = self.clean_headline(value)
        parsed_headline = {'sentiment': []}
        lstt = []
        for value in self.headlines.values():
            
            lstt.append(value)

        for z in lstt:
            for z1 in z:
                s = ''.join(z1)
                parsed_headline['sentiment'].append(self.get_headline_sentiment(s))




        def sentiment(self):
            pass
            pheadlines = [headline for headline in headlines if headline['sentiment'] == 'positive'] 
# percentage of positive headlines 
            print("Positive headlines percentage: {} %".format(100*len(pheadlines)/len(headlines))) 
# picking negative headlines from headlines 
            nheadlines = [headline for headline in headlines if headline['sentiment'] == 'negative'] 
# percentage of negative headlines 
            print("Negative headlines percentage: {} %".format(100*len(nheadlines)/len(headlines))) 
# percentage of neutral headlines 
            print("Neutral headlines percentage: {} % \ ".format(100*len(headlines - nheadlines - pheadlines)/len(headlines))) 

# printing first 5 positive headlines 
            print("\n\nPositive headlines:") 
            for headline in pheadlines[:10]: 
                print(headlines['text']) 

# printing first 5 negative headlines 
            print("\n\nNegative headlines:") 
            for headline in nheadlines[:10]: 
                print(headlines['text']) 



        df = pd.DataFrame({'Headline': spanz_new[times], 'sentiment': parsed_headline['sentiment'], 'Link': new_linkz[times]})
        #df['Headline'] = df['Headline'].str[0]
        #df['sentiment'] = df['sentiment'].str[0]
        #df['Link'] = df['Link'].str[0]
        filename = times + ' news' + '.csv'
        df.to_csv(filename, sep='\t', encoding='utf-8')

    def clean_headline(self, headline): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', headline).split())


    def get_headline_sentiment(self, headline): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        #import TextBlob

        analysis = TextBlob(self.clean_headline(headline)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

      


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


