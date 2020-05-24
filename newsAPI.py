
from newsapi import NewsApiClient
import pandas as pd
import time
newsapi = NewsApiClient(api_key='969XXXXXXXXXXXXXXXXXXXXXXXdb')

company_list=['Exxon Mobil','British petroleum BP','PetroChina','Schlumberger','Chevron Corporation','Johnson & Johnson Company','Pfizer','Unitedhealth Group UNH','Merck and co pharmaceutical company','Abbott Laboratories','Ford Motor','General Motors','Honda Motor','Toyota Motor Corp','Tesla Inc','JPMorgan Chase','CitiBank Citi Group','UBS Group','HSBC','Barclays','Microsoft','Sony Corp','Amazon','Netflix','Tencent']


n=9
for i in range(n):
    DATE="2020-05-"+str(int(15+(i+1)))
    print(DATE)
    for company in company_list:
        print(company)
        date=[]
        title=[]
        source=[]
        author=[]
        description=[]
        full_news=[]
        articles=newsapi.get_everything(q=company, from_param=DATE, to=DATE, language='en',sort_by='relevancy')
        if(len(articles['articles'])!=0):
            print('Total Number of news available:', len(articles['articles']))
            for i in range(len(articles['articles'])):
                date.append(articles['articles'][i].get('publishedAt'))
                #date.append(from_date)
                title.append(articles['articles'][i].get('title'))
                source.append(articles['articles'][i].get('source')['name'])
                author.append(articles['articles'][i].get('author'))
                description.append(articles['articles'][i].get('description'))
                full_news.append(articles['articles'][i].get('content'))
            print(title)
            df=pd.DataFrame()
            df['PublishedAt']=date
            df['Headline']=title
            df['Source']=source
            df['Author']=author
            df['Description']=description
            df['FullNews']=full_news
            df.to_excel('data/trainingFolder/{0}_news_{1}.xlsx'.format(company,DATE))
        print("*************************************************************")
