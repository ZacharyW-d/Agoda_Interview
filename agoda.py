#!/usr/bin/env python
# coding: utf-8

# In[143]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
from datetime import timedelta


# In[62]:


data_raw = pd.read_excel('Case_Study_Urgency_Message_Data.xlsx')
data = data_raw.copy()


# In[63]:


data.describe()


# In[64]:


plt.boxplot(data.ADR_USD)
plt.title('ADR_USD boxplot')


# In[65]:


data.head()


# In[193]:


plt.hist(data.ADR_USD, 100, color='lightsteelblue')
plt.xlabel('ADR_USD ($)')
plt.ylabel('Count')
plt.title('ADR_USD distribution')

plt.savefig('demo.png', transparent=True)


# In[67]:


data.isnull().any()


# In[99]:


data_clean = data[data.ADR_USD <= 300]
print(len(data) - len(data_clean))
data_clean = data_clean[data_clean.ADR_USD >= 15]
print(len(data) - len(data_clean))
len(data_clean)
data_clean = data_clean[data_clean.checkin_date > data_clean.booking_date]


# In[195]:


plt.hist(data_clean.ADR_USD, 100, color='lightsteelblue')
plt.xlabel('ADR_USD ($)')
plt.ylabel('Count')
plt.title('ADR_USD distribution')
plt.savefig('1.png', transparent=True)


# In[101]:


data_clean['date_diff'] = data_clean.checkin_date - data_clean.booking_date
data_clean['date_diff'] = [x.days for x in data_clean.date_diff]


# In[102]:


data_clean.head()


# In[198]:


temp = data_clean.groupby('date_diff')['ADR_USD'].agg({'Low Value':'min','High Value':'max','Mean':'mean', 'Median':'median', 'Std':'std'})
temp.reset_index(drop = False, inplace=True)
temp['date_diff'] = temp['date_diff']

ax  = temp.plot(x='date_diff', y='Mean', c='black')
plt.title('average ADR_USD by date_diff')
plt.fill_between(x='date_diff',y1='Low Value',y2='High Value', data=temp)


# In[182]:


temp.plot(x='date_diff', y='Std', c='red')
plt.title('std of ADR_USD by date_diff')


# In[78]:


temp[temp.date_diff == 50]


# In[183]:


temp_count = data_clean.groupby('date_diff')['ADR_USD'].count().reset_index()
plt.plot(temp_count.ADR_USD)
plt.title('count of bookings by date_diff')


# In[149]:


data_clean['month'] = [x.month for x in data_clean.checkin_date]
data_clean['stay'] = data_clean['checkout_date'] - data_clean['checkin_date']
data_clean['stay'] = [x.days for x in data_clean.stay]


# In[197]:


temp = data_clean.groupby(['stay', 'date_diff'])['ADR_USD'].agg({'Low Value':'min','High Value':'max','Mean':'mean', 'Median':'median', 'Std':'std'})
temp.reset_index(drop = False, inplace=True)

fig, ax = plt.subplots()
temp[temp.stay==1].plot(x='date_diff', y='Mean', c='yellow', ax=ax)
temp[temp.stay==2].plot(x='date_diff', y='Mean', c='red', ax=ax)
temp[temp.stay==3].plot(x='date_diff', y='Mean', c='green', ax=ax)
ax.legend(['one night', 'two nights', 'three nights'])
plt.title('ADR by date_diff with different nights stayed')

# plt.fill_between(x='date_diff',y1='Low Value',y2='High Value', data=temp)


# In[199]:


temp = data_clean.groupby(['month', 'date_diff'])['ADR_USD'].agg({'Low Value':'min','High Value':'max','Mean':'mean', 'Median':'median', 'Std':'std'})
temp.reset_index(drop = False, inplace=True)

fig, ax = plt.subplots()
temp[temp.month==10].plot(x='date_diff', y='Mean', c='yellow', ax=ax)
temp[temp.month==11].plot(x='date_diff', y='Mean', c='red', ax=ax)
temp[temp.month==12].plot(x='date_diff', y='Mean', c='green', ax=ax)
ax.legend(['Oct', 'Nov', 'Dec'])
plt.title('ADR by date_diff of Months')

# plt.fill_between(x='date_diff',y1='Low Value',y2='High Value', data=temp)


# In[ ]:





# In[212]:


temp = data_clean[data_clean.hotel_id == 197996].groupby('date_diff')['ADR_USD'].mean().reset_index()
temp.plot(x='date_diff', y='ADR_USD')


# In[ ]:




