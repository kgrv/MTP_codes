#!/usr/bin/env python
# coding: utf-8

# In[1]:


from newsapi import NewsApiClient
import pandas as pd
import time
newsapi = NewsApiClient(api_key='9691f05cd1bf40b9affb85d8bf0a98db')
#keys=f8c75c18656149309e660ee3682ae166,9691f05cd1bf40b9affb85d8bf0a98db,7dacecf955174607b1ffb79fcad52619


# In[2]:


company_list1=['Exxon Mobil','British petroleum BP','PetroChina','Schlumberger','Chevron Corporation']
company_list2=['Johnson & Johnson Company','Pfizer','Unitedhealth Group UNH','Merck and co pharmaceutical company','Abbott Laboratories']
company_list3=['Ford Motor','General Motors','Honda Motor','Toyota Motor Corp','Tesla Inc']
company_list4=['JPMorgan Chase','CitiBank Citi Group','UBS Group','HSBC','Barclays']
company_list5=['Microsoft','Sony Corp','Amazon','Netflix','Tencent']
company_list=['Exxon Mobil','British petroleum BP','PetroChina','Schlumberger','Chevron Corporation','Johnson & Johnson Company','Pfizer','Unitedhealth Group UNH','Merck and co pharmaceutical company','Abbott Laboratories','Ford Motor','General Motors','Honda Motor','Toyota Motor Corp','Tesla Inc','JPMorgan Chase','CitiBank Citi Group','UBS Group','HSBC','Barclays','Microsoft','Sony Corp','Amazon','Netflix','Tencent']


# In[ ]:


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


# In[17]:





# In[40]:


top_headlines = newsapi.get_everything(q='Coronavirus covid19 india',
                                      from_param='2020-04-01',
                                      to='2020-04-11',
                                      language='en',
                                      sort_by='relevancy')
top_headlines


# In[31]:


'''
all_articles = newsapi.get_everything(q='Google',
                                      from_param='2020-02-01',
                                      to='2020-02-01',
                                      language='en',
                                      sort_by='relevancy')
                                      
all_articles = newsapi.get_everything(q='Google',
                                      from_param='2020-02-11',
                                      to='2020-02-11',
                                      sources='google-news',
                                      language='en',
                                      sort_by='relevancy')
top_headlines = newsapi.get_top_headlines(q='Google',
                                          sources='google-news',
                                          language='en')

/v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='exxon mobil',
                                          language='en',
                                          country='us')
print(top_headlines)
sources = newsapi.get_sources()'''


# In[ ]:




