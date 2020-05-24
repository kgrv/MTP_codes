#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import nltk
import time
import re
import numpy as np

from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn import neighbors, datasets
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[9]:


def clean_fields(input_data):
    desc_str =""
    for j in range(len(input_data)):
        PD = input_data[j].lower() # change everything to lowercase
        PD = re.sub('[^A-Za-z0-9\s]+', ' ', PD) #remove special characters
        PD = re.sub("\d+\.?\d*", "", PD) # remove numbers
        PD = re.sub(r'[^\x00-\x7F]+',' ', PD) # remove ascii
        ptext = nltk.Text(PD.split())
        ptextclean2 = [w for w in ptext if not w in nltk.corpus.stopwords.words('english')]
        desc_str +=  (" ".join(ptextclean2)+"\n" )
    return(desc_str.strip("\n"))


# In[7]:


test_data=pd.read_excel('data/trainingFolder/master/testfile.xlsx')
train_data=pd.read_excel('data/trainingFolder/master/master_data.xlsx')


# In[10]:


desc_test=clean_fields(test_data['article'])
desc_train = clean_fields(train_data['article'])
train_buffer = desc_train.split("\n")
test_buffer=desc_test.split("\n")


# In[11]:


test_lbl=test_data['upintraday']
train_lbl=train_data['upintraday']


# In[13]:


vectorizer = TfidfVectorizer(max_df=1.0, max_features=10000,min_df=0, stop_words='english')


# In[14]:


vectorizer.fit( train_buffer+ test_buffer)

X_train = vectorizer.transform(train_buffer)
X_test = vectorizer.transform(test_buffer)


# In[15]:


clf=LogisticRegression()


# In[17]:


clf.fit(X_train, train_lbl)
XP_train =  clf.predict(X_train)
XProb_train = clf.predict_proba(X_train)
print('Accuracy L2  : {:.3f}'.format(accuracy_score(train_lbl, XP_train)))
XP = clf.predict(X_test)
XProb = clf.predict_proba(X_test)


# In[28]:


confusion_matrix(test_lbl, XP, labels=None, sample_weight=None).ravel()


# In[29]:


sum(confusion_matrix(test_lbl, XP, labels=None, sample_weight=None).ravel())


# In[30]:


40/61


# In[21]:


test_data['upintraday'].values

