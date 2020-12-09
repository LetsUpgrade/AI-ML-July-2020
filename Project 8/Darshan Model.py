#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.simplefilter('ignore')


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle 
# pickle is used to save the model created by us


# In[3]:


df = pd.read_csv("hiring.csv")
df.head()


# In[4]:


df.isna().sum()


# In[5]:


# experience

df['experience'].fillna(0, inplace=True)


# In[6]:


df.isna().sum()


# In[7]:


df['test_score'].mean()


# In[8]:


df['test_score'].fillna(df['test_score'].mean(), inplace=True)


# In[9]:


df.isna().sum()


# __Dataset is Clean now.__

# In[10]:


df.head()


# In[11]:


X = df.iloc[:,:-1]


# In[12]:


X.head()


# In[13]:


X.shape


# In[14]:


X.experience


# In[19]:


# Convert text in the cols to integer values

def conv(x):
    dict = {'two':2, 'three':3, 'five':5, 'seven':7, 'ten':10, 0:0, 'eleven':11 }
    return dict[x]


# In[20]:


X['experience'] = X['experience'].apply(lambda x: conv(x))


# In[21]:


X.head()


# In[22]:


X.info()


# __X is ready.__

# In[23]:


y = df.iloc[:,-1]
y


# I am not going to do traintestsplit as the dataset itself is very small.
# 
# However, you all are encouraged to do it later as a part of practice and submit it as an assignment.
# 
# __Q. You can select any of the projects covered till now  by any of the trainers and deploy the same.__

# In[24]:


# Modeling

from sklearn.linear_model import LinearRegression
lr = LinearRegression()


# In[25]:


# Fit the model
lr.fit(X, y)


# In[27]:


# Prediction Phase
y_pred=lr.predict(X)
y_pred


# In[28]:


y


# In[29]:


from sklearn.metrics import r2_score
r2_score(y_pred, y)


# In[32]:


X


# In[33]:


lr.predict([[3,9,7]])


# In[34]:


lr.predict([[10,10,10]])


# In[35]:


lr.predict([[10,2,3]])


# # Model Deployment

# In[36]:


# Here, we will save the 'lr' model to disk as 'model.py'

import pickle

pickle.dump(lr,open('model.py','wb'))
# Dump this model by the name "model.py" in the systems HDD and while doing this
# write this file using "write bytes" mode.


# In[37]:


# Lets now try to load the same model by reading it from the system
# and using it for prediction

model2 = pickle.load(open("model.py","rb"))


# In[38]:


model2.predict([[3,9,7]])


# In[39]:


model2.predict([[10,10,10]])


# In[40]:


model2.predict([[10,2,3]])


# # Happy Learning
