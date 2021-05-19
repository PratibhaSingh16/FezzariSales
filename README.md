<h1 align="center">
FezzariSales
  
  
Bike Accessories Sales Analysis 


![1](https://user-images.githubusercontent.com/77543839/118738658-86c7d800-b815-11eb-83e1-02cf2ea5e778.jpeg) 
</h1>


I used dataset [Bike_accessories_sales_dataset](https://raw.githubusercontent.com/PratibhaSingh16/FezzariSales/main/Fezzari%20Sales.csv) to perform this analysis using Python


Importing dataset:


```bash
import pandas as pd
df = pd.read_csv('Fezzari Sales.csv')
df
```

For knowing the shape of dataset:
```bash
df.shape
```

(34867, 14)

Checking total missing values in the dataset:
```
df.isna().sum()
```
Column Name | Total Missing Values
------------ | -------------
Date            |    1
Time             |   1
Year             |   1
Customer Age     |   3
Customer Gender  |   3
Country           |  1
State              | 3
Product Category   | 4
Sub Category        3
Quantity           | 1
Unit Cost         |  3
Revenue            | 1
Payment          |   0
Rating            |  1


Displaying all the missing values in the dataset:
```
new_df = df[df.isna().any(axis=1)]
new_df
```

Cleaning missing values: 
```
df=df.dropna(axis=0,how='any')
df
```

Checking missing values after cleaning:
```
df.isna().sum()
```
Column Name | Total Missing Values
------------ | -------------
Date          |      0
Time           |     0
Year            |    0
Customer Age     |   0
Customer Gender   |  0
Country            | 0
State               |0
Product Category|    0
Sub Category     |   0
Quantity          |  0
Unit Cost          | 0
Revenue          |   0
Payment           |  0
Rating             | 0


Checking datatype in dataset:
```
df.dtypes
```
Column Name | Data Type
------------ | -------------
Date           |      object
Time            |     object
Year             |   float64
Customer Age      |  float64
Customer Gender    |  object
Country             | object
State                |object
Product Category |    object
Sub Category      |   object
Quantity           | float64
Unit Cost    |       float64
Revenue       |      float64
Payment        |      object
Rating      |        float64


Correcting datatype of CustomerAge, Year and Quantity column:
``` 
df['Customer Age']=df['Customer Age'].astype('int')
df['Year']=df['Year'].astype('int')
df['Quantity']=df['Quantity'].astype('int')
df
```


Checking datatype after modification:
```
df.dtypes
```

Total count of datatypes:
```
df.dtypes.value_counts()
```


Data Type | Total
------------ | -------------
object  |   8
float64  |  3
int64     | 3

Description of the dataset:
```
df.describe()
```

Augmenting data with additional columns:
```
df['Month'] = pd.to_datetime(df['Date']).dt.month
df.head()
```


Calculating sales cost:
```
df['Sales Cost'] = df['Quantity']* df['Unit Cost']
df
```


Grouping month by sales cost:
```
df_temp = df.groupby('Month').sum()['Sales Cost'].reset_index()
df_temp
```

Month| Sales Cost
------------ | -------------		
1	| 1734134.19
2 |	1612798.61
3|	1735518.24
4	| 1779628.02
5|	2014706.84
6	|2130992.54
7	|1431118.20
8	|1430123.61
9|	1409997.43
10|	1385913.93
11|	1525403.64
12	|1883753.77


Plotting sales by month:
```
import matplotlib.pyplot as plt

months = range(1,13)
print(months)

plt.bar(months,df.groupby(['Month']).sum()['Sales Cost'])
plt.xticks(months)
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.show()
```

![output_16_1](https://user-images.githubusercontent.com/77543839/118738633-7f083380-b815-11eb-913d-7600c02f1495.png)


Result:

*Here we can see that Month 6 has high Sales. So June is the best month for sales with $2130992.54*


Grouping revenue by country:
```
new_df=df.groupby(['Country']).sum()
new_df.loc[:,'Revenue']
```

Country | Revenue
------------ | -------------
France        |     3444133.0
Germany        |    4244510.0
United Kingdom  |   4276220.0
United States  |   10371147.0


Plotting revenue by country:
```
keys = [Country for Country, df in df.groupby(['Country'])]
plt.bar(keys,df.groupby(['Country']).sum()['Revenue'])

plt.ylabel('Sales in USD ($)')
plt.xlabel('Country')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()
```

![output_18_0](https://user-images.githubusercontent.com/77543839/118738634-7f083380-b815-11eb-8afe-0dd240ccf671.png)


Result:

*Here we can see that United States has sold most products with $10371147.0 revenue*


Sorting Product Category and Subcategory based on revenue:
```
cat_subcat = pd.DataFrame(df.groupby(['Product Category', 'Sub Category']).sum()['Revenue'])
cat_subcat.sort_values(['Product Category','Revenue'], ascending=False)
```

Result:

Here we can see
1. In Clothing,jerseys are more profitable
2. In Bikes,Mountain Bikes are more profitable
3. In Accessories Tires and Tubes are more profitable


Sorting out top 10 sells cost:
```
product_sales = pd.DataFrame(df.groupby('Sub Category').sum()['Sales Cost'])
product_sales.sort_values(by=['Sales Cost'], inplace=True, ascending=False)
product_sales.head(10)
```
	
Sub Category	| Sales Cost
-------------|----------
Mountain Bikes|	5027183.58
Road Bikes|	3823818.35
Tires and Tubes	|2353428.93
Touring Bikes	|2293103.10
Helmets	|2219595.58
Jerseys	|1531295.87
Shorts	|602139.99
Bottles and Cages|	579840.55
Hydration Packs	|330935.06
Vests	|310337.04


Plotting top 10 Products by Sales Cost:
```
keys = [SubCategory for SubCategory, df in df.groupby(['Sub Category'])]
plt.bar(keys,df.groupby(['Sub Category']).sum()['Sales Cost'])

plt.ylabel('Sales in USD ($)')
plt.xlabel('Sub Category')
plt.xticks(keys, rotation='vertical', size=8)
```

![output_21_0](https://user-images.githubusercontent.com/77543839/118738635-7f083380-b815-11eb-9621-4a4c876eac56.png)

Result

*Here we can see top 10 products by sales. And Mountain Bikes holds first in sales with $5029503.58 sales cost.*



Grouping and Sorting products based on Quantity:
```
most_selling_products = pd.DataFrame(df.groupby('Sub Category').sum()['Quantity'])
most_selling_products.sort_values(by=['Quantity'], inplace=True, ascending=False)
most_selling_products[:10]
```

	
Sub Category | Quantity
-----------|----------
Tires and Tubes	|22201
Bottles and Cages|	10558
Helmets|	8384
Road Bikes	|6119
Mountain Bikes	|5494
Jerseys	|4030
Caps	|3020
Touring Bikes	|2673
Fenders|	1494
Shorts	|1129


Plotting most sold products based on Quantity:
```
product_group = df.groupby('Sub Category')
quantity = product_group.sum()['Quantity']

keys = [pair for pair, df in product_group]
plt.bar(keys, quantity)
plt.xticks(keys, rotation='vertical', size=8)
plt.ylabel('Quantity')
plt.xlabel('Sub Category')
plt.show()
```

![output_23_0](https://user-images.githubusercontent.com/77543839/118738637-7f083380-b815-11eb-942d-931ab7facde0.png)

Plotting in pie-chart:
```
category_chart=df['Sub Category'].value_counts()
category_chart.plot(kind = 'pie', autopct='%1.1f%%', figsize=(15, 15)).legend()
```

![output_24_1](https://user-images.githubusercontent.com/77543839/118738638-7f083380-b815-11eb-88ce-606fee6ecda2.png)

Result

*Here we can see Tires and Tubes have sold more with 22201 sales quantity.*


Counting Payment modes:
```
df['Payment'].value_counts()
```
Payment Mode| Total
----------|--------
Cash   |        16702
Credit Card |   11697
Ewallet      |   6468

Plotting payment modes:
```
import seaborn as sns
sns.countplot(x='Payment', data=df)
plt.show()
```

![output_26_0](https://user-images.githubusercontent.com/77543839/118738639-7fa0ca00-b815-11eb-8db6-eae26bda59b9.png)

Result

*The most preferred payment mode is in-fact cash and not credit cards and Ewallet as this dataset was of year 2015,2016.*


Time at which we should display advertisements to maximize likelihood of customer's buying product:
```
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
df
df['Hour'].value_counts()
```
Hour | Total Count
-------|-------
19.0  |  3943
13.0   | 3593
15.0    |3554
10.0 |   3521
18.0  |  3244
11.0   | 3137
12.0 |   3100
14.0  |  2893
16.0   | 2690
20.0 |   2613
17.0  |  2578

Graphical representation of Hour wise Total Count:
```
keys = [slot for slot, df in df.groupby(['Hour'])]
plt.plot(keys, df.groupby(['Hour']).count())
plt.xticks(keys)
plt.grid()
plt.ylabel('Count')
plt.xlabel('Hour')
plt.show()
```

![output_29_0](https://user-images.githubusercontent.com/77543839/118738640-7fa0ca00-b815-11eb-9f77-0f080f2a17ae.png)

Result

*Most of the customers are buying products at 7pm so we can display advertisement at that time and maximize likelihood of buying products*


Which hour of the day is the busiest:
```
sns.lineplot(x="Hour",  y = 'Quantity',data =df).set_title("Product Sales per Hour")
```
![output_30_1](https://user-images.githubusercontent.com/77543839/118738642-7fa0ca00-b815-11eb-9b14-ef49ead28d08.png)

Result

*Peak is observed in the 12th and 17th hour that is 12pm and 5pm .Hence sales is high in afternoons.*


Finding Mean for Customer Rating to see Customer Satisfaction:
```
import numpy as np
sns.distplot(df['Rating'])
plt.axvline(x=np.mean(df['Rating']), c='red', ls='--', label='mean')
plt.legend()
```

![output_31_1](https://user-images.githubusercontent.com/77543839/118738643-7fa0ca00-b815-11eb-87af-3567973cfb0c.png)

Result

*The red line here indicates that 7.491 is the mean value of customer rating*


Counting the Max products bought by age:
```
Age=df.groupby('Customer Age').sum()['Quantity']
Age=Age[Age == Age.max()]
Age
```

Customer|Age
------|-----
31.0  |  2630.0

Plotting products bought by age:
```
import seaborn as sns
plt.figure(figsize=(20, 10))
sns.countplot(x='Customer Age', data=df)
plt.show()
```

![output_33_0](https://user-images.githubusercontent.com/77543839/118738644-80396080-b815-11eb-8d4f-bcdd900e920b.png)

Result

*We can see that people of Age 31 have bought most products = 2630*


States to be chosen for expansion:
```
keys = [Country for Country, df in df.groupby(['State'])]
plt.bar(keys,df.groupby(['State']).sum()['Revenue'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('State')
plt.xticks(keys, rotation='vertical', size=10)
plt.show()
```

![](https://user-images.githubusercontent.com/77543839/118738645-80396080-b815-11eb-802c-37c43ecb9d51.png)


Result

*California is the most profitable state which comes under united states.So we can focus on California to expand*

# This was all the Analysis made by me on the dataset











