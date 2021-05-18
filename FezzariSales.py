#!/usr/bin/env python
# coding: utf-8

# In[59]:


#importing dataset
import pandas as pd
df = pd.read_csv('Fezzari Sales.csv')
df


# In[18]:


#overview of tha dataset
df.head()


# In[19]:


#number of columns and rows in the dataset
df.shape


# In[14]:


df.info()


# In[20]:


#checking total missing values in the dataset
df.isna().sum()


# In[21]:


#Finding total missing values in the dataset
new_df = df[df.isna().any(axis=1)]
new_df


# In[22]:


#Cleaning missing values
df=df.dropna(axis=0,how='any')
df


# In[23]:


#checking missing values after cleaning
df.isna().sum()


# In[24]:


#checking datatype in dataset
df.dtypes


# In[25]:


#Correcting datatype of CustomerAge, Year and Quantity column
df['Customer Age']=df['Customer Age'].astype('int')
df['Year']=df['Year'].astype('int')
df['Quantity']=df['Quantity'].astype('int')
df


# In[26]:


#checking datatype after modification
df.dtypes


# In[27]:


#Total count of datatypes
df.dtypes.value_counts()


# In[28]:


#description of the dataset
df.describe()


# In[29]:


#Augmenting data with additional columns
df['Month'] = pd.to_datetime(df['Date']).dt.month
df.head()


# In[30]:


#calculating sales cost
df['Sales Cost'] = df['Quantity']* df['Unit Cost']
df


# In[38]:


#Grouping month by sales cost
df_temp = df.groupby('Month').sum()['Sales Cost'].reset_index()
df_temp


# In[32]:


#plotting sales by month
import matplotlib.pyplot as plt

months = range(1,13)
print(months)

plt.bar(months,df.groupby(['Month']).sum()['Sales Cost'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()


# In[33]:


#grouping revenue by country
new_df=df.groupby(['Country']).sum()
new_df.loc[:,'Revenue']


# In[34]:


#Plotting revenue by country
keys = [Country for Country, df in df.groupby(['Country'])]
plt.bar(keys,df.groupby(['Country']).sum()['Revenue'])

plt.ylabel('Sales in USD ($)')
plt.xlabel('Country')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()


# In[35]:


#Sorting Product Category and Subcategory based on revenue
cat_subcat = pd.DataFrame(df.groupby(['Product Category', 'Sub Category']).sum()['Revenue'])
cat_subcat.sort_values(['Product Category','Revenue'], ascending=False)


# In[36]:


#sorting out top 10 sells cost
product_sales = pd.DataFrame(df.groupby('Sub Category').sum()['Sales Cost'])
product_sales.sort_values(by=['Sales Cost'], inplace=True, ascending=False)
product_sales.head(10)


# In[39]:


#Plotting top 10 Products by Sales Cost
keys = [SubCategory for SubCategory, df in df.groupby(['Sub Category'])]
plt.bar(keys,df.groupby(['Sub Category']).sum()['Sales Cost'])

plt.ylabel('Sales in USD ($)')
plt.xlabel('Sub Category')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()


# In[40]:


#Grouping and Sorting products based on Quantity
most_selling_products = pd.DataFrame(df.groupby('Sub Category').sum()['Quantity'])
most_selling_products.sort_values(by=['Quantity'], inplace=True, ascending=False)
most_selling_products[:10]


# In[42]:


#Plotting most sold products based on Quantity
product_group = df.groupby('Sub Category')
quantity = product_group.sum()['Quantity']

keys = [pair for pair, df in product_group]
plt.bar(keys, quantity)
plt.xticks(keys, rotation='vertical', size=8)
plt.ylabel('Quantity')
plt.xlabel('Sub Category')
plt.show()


# In[43]:


#Plotting in pie-chart
category_chart=df['Sub Category'].value_counts()
category_chart.plot(kind = 'pie', autopct='%1.1f%%', figsize=(15, 15)).legend()


# In[44]:


#Counting Payment modes
df['Payment'].value_counts()


# In[45]:


#plotting payment modes
import seaborn as sns
sns.countplot(x='Payment', data=df)
plt.show()


# In[46]:


#time at which we should display advertisements to maximize likelihood of customer's buying product
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
df


# In[47]:


df['Hour'].value_counts()


# In[48]:


keys = [slot for slot, df in df.groupby(['Hour'])]
plt.plot(keys, df.groupby(['Hour']).count())
plt.xticks(keys)
plt.grid()
plt.ylabel('Count')
plt.xlabel('Hour')
plt.show()


# In[49]:


#Which hour of the day is the busiest
sns.lineplot(x="Hour",  y = 'Quantity',data =df).set_title("Product Sales per Hour")


# In[50]:


#Finding Mean for Customer Rating to see Customer Satisfaction
import numpy as np
sns.distplot(df['Rating'])
plt.axvline(x=np.mean(df['Rating']), c='red', ls='--', label='mean')
plt.legend()


# In[51]:


#Counting the products bought by age
Age=df.groupby('Customer Age').sum()['Quantity']
Age=Age[Age == Age.max()]
Age


# In[52]:


#Plotting products bought by age
import seaborn as sns
plt.figure(figsize=(20, 10))
sns.countplot(x='Customer Age', data=df)
plt.show()


# In[58]:


#States to be chosen for expansion
keys = [Country for Country, df in df.groupby(['State'])]
plt.bar(keys,df.groupby(['State']).sum()['Revenue'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('State')
plt.xticks(keys, rotation='vertical', size=10)
plt.show()


# 
