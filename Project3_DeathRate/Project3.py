#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Project:Develop a Python Flask application for death mortality rates of world till 2017
#Program By:Ayush Pandey
#Email Id:1805290@kiit.ac.in
#DATE:19-Oct-2021
#Python Version:3.7
#CAVEATS:None
#LICENSE:None


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


#For reading the csv file
df=pd.read_csv('data_2.csv')


# In[4]:


df.head()


# In[5]:


df['Entity'].nunique()


# In[6]:


print(df.shape)


# In[7]:


df.dtypes


# In[8]:


print(df.isna().sum())


# In[9]:


sns.heatmap(df.isna())


# In[10]:


#As more than 70% data are Nan in High total cholesterol so droping it
df.drop('High total cholesterol',axis=1,inplace=True)


# In[11]:


df.shape


# In[12]:


#Checking for Nan values in Code
q=df[df['Code'].isna()]


# In[13]:


#Using entity we can infer code so droping code
df.drop('Code',axis=1,inplace=True)


# In[14]:


df.shape


# In[15]:


df.head(2)


# In[16]:


df.describe()


# In[17]:


#Grouping all the data with entity and taking sum of all the factors respectively to obtain some inference
df1=df.groupby('Entity',as_index=False).agg({'Unsafe water source':'sum','Unsafe sanitation':'sum','No access to handwashing facility':'sum','Household air pollution from solid fuels':'sum','Non-exclusive breastfeeding':'sum','Discontinued breastfeeding':'sum','Child wasting':'sum','Child stunting':'sum','Low birth weight for gestation':'sum','Secondhand smoke':'sum','Alcohol use':'sum','Drug use':'sum','Diet low in fruits':'sum','Diet low in vegetables':'sum','Unsafe sex':'sum','Low physical activity':'sum','High fasting plasma glucose':'sum','High body-mass index':'sum','High systolic blood pressure':'sum','Smoking':'sum','Iron deficiency':'sum','Vitamin A deficiency':'sum','Low bone mineral density':'sum','Air pollution':'sum','Outdoor air pollution':'sum','Diet high in sodium':'sum','Diet low in whole grains':'sum','Diet low in nuts and seeds':'sum'})


# In[18]:


df1


# In[19]:


#Sum of all the columns is greater than 10,00,00,000
def get(x):
    q=df1[df1['Entity']==x]
    a=q.sum(axis=1)
    s=a.values
    if(s[0]>100000000):
        Total[x]=s[0]
Total={}
ob=df['Entity'].apply(get)


# In[20]:


a=Total.keys()
s=Total.values()
df2=pd.DataFrame()
df2['Entity']=a
df2['Total']=s
df2.head()


# In[21]:


#Graph for the entity having death due to all reasons greater then 10,00,00,000
plt.figure(figsize=(1,1))
sns.catplot(x='Entity',y='Total',data=df2.sort_values('Total',ascending=False),kind='bar',height=3,aspect=3)
plt.xticks(rotation=90)
plt.title("Death Cases More Than 10000000")
plt.savefig('Death_more_than_100000000.png',format='png',bbox_inches='tight')
plt.show()


# In[22]:


#Sum of all the factors for an Entity is less than 50,000
def get(x):
    q=df1[df1['Entity']==x]
    a=q.sum(axis=1)
    s=a.values
    if(s[0]<50000):
        Total[x]=s[0]
Total={}
ob=df['Entity'].apply(get)


# In[23]:


a=Total.keys()
s=Total.values()
df2=pd.DataFrame()
df2['Entity']=a
df2['Total']=s
df2.head()


# In[24]:


#Graph for the entity having death due to all reasons less than 50,00,000
sns.catplot(x='Entity',y='Total',data=df2.sort_values('Total',ascending=False),kind='bar',height=3,aspect=3)
plt.xticks(rotation=90)
plt.title("Death Cases Less Than 50,000")
plt.savefig('Death_Less_than_50000.png',format='png',bbox_inches='tight')
plt.show()


# In[25]:


#Data containg all factors along with their total death count
a=df1.columns[1:]
see={}
for i in a:
    #print(df1[i].sum())
    see[i]=df1[i].sum()


# In[26]:


a=see.keys()
s=see.values()
df3=pd.DataFrame()
df3['Factor']=a
df3['Total']=s
df3.head()


# In[27]:


#Graph for the Different Factors of Death along with their count
sns.catplot(x='Factor',y='Total',data=df3.sort_values('Total',ascending=False),kind='bar',height=3,aspect=3)
plt.xticks(rotation=90)
plt.title("Different Factor And Their Count")
plt.savefig('Factors_count.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:





# In[28]:


#Major causes of death in India
q=df1[df1['Entity']=='India']
a=q.columns[1:]
see={}
for i in a:
    see[i]=q[i].sum()
a=see.keys()
s=see.values()
df4=pd.DataFrame()
df4['Factor']=a
df4['Total']=s
df4.head()

#Graph for all the causes of death in India along with their count
sns.catplot(x='Factor',y='Total',data=df4.sort_values('Total',ascending=False),kind='bar',height=3,aspect=3)
plt.xticks(rotation=90)
plt.title("Different Factor For Death and Their Count In India")
plt.savefig('Factors_India.png',format='png',bbox_inches='tight')
plt.show()


# In[29]:


#For comparing the country India and Pakistan
India=df[df['Entity']=='India']
Pakistan=df[df['Entity']=='Pakistan']


# In[30]:


#Death each year in India due to Smoking,Air Pollution,High Systolic blood pressure
plt.figure(figsize=(5,5))
plt.plot(India.Year,India['Smoking'],label='Smoking')
plt.plot(India.Year,India['Air pollution'],label='Air Pollution')
plt.plot(India.Year,India['High systolic blood pressure'],label='HS-blood pressure')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Deaths  (in. lakhs)')
plt.title('Death each Year in India')
plt.savefig('Death_Each_Year_India.png',format='png',bbox_inches='tight')
plt.show()


# In[31]:


#Major causes of death in Pakistan
q=df1[df1['Entity']=='Pakistan']
a=q.columns[1:]
see={}
for i in a:
    see[i]=q[i].sum()
a=see.keys()
s=see.values()
df5=pd.DataFrame()
df5['Factor']=a
df5['Total']=s

q=df5[df5['Factor']=='Air pollution']
print(q['Total'][23])
sns.catplot(x='Factor',y='Total',data=df5.sort_values('Total',ascending=False),kind='bar',height=3,aspect=3)
plt.xticks(rotation=90)
plt.title('Different Factors of Death And Their Count In Pakistan')
plt.savefig('Factors_Pakistan.png',format='png',bbox_inches='tight')
plt.show()


# In[32]:


#Death in pakistan due to Smoking,Air Pollution and High Systolic Blood Pressure for year year
plt.figure(figsize=(5,5))
plt.plot(Pakistan.Year,Pakistan['Smoking'],label='Smoking')
plt.plot(Pakistan.Year,Pakistan['Air pollution'],label='Air Pollution')
plt.plot(Pakistan.Year,Pakistan['High systolic blood pressure'],label='HS-blood pressure')
plt.legend()
plt.xlabel('Year')
plt.ylabel('Deaths  (in. lakhs)')
plt.title('Death each Year in Pakistan')
plt.savefig('Death_Each_Year_Pakistan.png',format='png',bbox_inches='tight')
plt.show()


# In[33]:


df.head(2)


# In[34]:


#Major cause of death for every 10 year
df7=df.groupby(df.Year.sub(1990)//10,as_index=False).agg({'Unsafe water source':'sum','Unsafe sanitation':'sum','No access to handwashing facility':'sum','Household air pollution from solid fuels':'sum','Non-exclusive breastfeeding':'sum','Discontinued breastfeeding':'sum','Child wasting':'sum','Child stunting':'sum','Low birth weight for gestation':'sum','Secondhand smoke':'sum','Alcohol use':'sum','Drug use':'sum','Diet low in fruits':'sum','Diet low in vegetables':'sum','Unsafe sex':'sum','Low physical activity':'sum','High fasting plasma glucose':'sum','High body-mass index':'sum','High systolic blood pressure':'sum','Smoking':'sum','Iron deficiency':'sum','Vitamin A deficiency':'sum','Low bone mineral density':'sum','Air pollution':'sum','Outdoor air pollution':'sum','Diet high in sodium':'sum','Diet low in whole grains':'sum','Diet low in nuts and seeds':'sum'})


# In[35]:


df7.head()


# In[36]:


#For the year 1990-2000,the major cause for death is High Systolic blood Pressure
df7.columns
see={}
for i in df7.columns:
    see[i]=df7[i][0]
a=see.keys()
s=see.values()
df8=pd.DataFrame()
df8['Factor']=a
df8['Total']=s
df8.head()
#plt.figure(figsize=(20,10)) 
sns.catplot(x='Factor',y='Total',data=df8.sort_values('Total',ascending=False),kind='bar',height=4,aspect=3)
plt.xticks(rotation=90)
plt.title('Different Factors Causing Death Between 1990-2000')
plt.savefig('Factors_1990_2000.png',format='png',bbox_inches='tight')
plt.show()


# In[37]:


#For the year 2000-2010,the major cause for death is High Systolic blood Pressure
df7.columns
see={}
for i in df7.columns:
    see[i]=df7[i][1]
a=see.keys()
s=see.values()
df9=pd.DataFrame()
df9['Factor']=a
df9['Total']=s
df9.head()
sns.catplot(x='Factor',y='Total',data=df9.sort_values('Total',ascending=False),kind='bar',height=4,aspect=3)
plt.xticks(rotation=90)
plt.title('Different Factors Causing Death Between 2000-2010')
plt.savefig('Factors_2000_2010.png',format='png',bbox_inches='tight')
plt.show()


# In[38]:


#For the year 2010-2019,the major cause for death is High Systolic blood Pressure
df7.columns
see={}
for i in df7.columns:
    see[i]=df7[i][2]
a=see.keys()
s=see.values()
df10=pd.DataFrame()
df10['Factor']=a
df10['Total']=s
df10.head()
sns.catplot(x='Factor',y='Total',data=df10.sort_values('Total',ascending=False),kind='bar',height=4,aspect=3)
plt.xticks(rotation=90)
plt.title('Different Factors Causing Death Between 2010-2017')
plt.savefig('Factors_2010_2017.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:





# In[39]:


from sklearn.linear_model import LinearRegression


# In[40]:


#Finding the no access to handwash using Unsafe water and sanitation columns
#For All countries
x=df[['Unsafe water source','Unsafe sanitation']]
y=df['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print(model.coef_)


# In[41]:


from sklearn.metrics import r2_score
r2_score(y,model.predict(x))


# In[42]:


#For India Doing Mutiple regression
#Independent
x=India[['Unsafe water source','Unsafe sanitation']]
#Dependent
y=India['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print(model.coef_)

#This shows that the Unsafe water souce is the main cause for no access to handwashing facility as the coefficient value is more than 50%.


# In[43]:


r2_score(y,model.predict(x))


# In[ ]:





# In[44]:


#For Pakistan Doing Mutiple regression
#Independent
x=Pakistan[['Unsafe water source','Unsafe sanitation']]
#Dependent
y=Pakistan['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print(model.coef_)

#This shows that the Unsafe sanitation souce is the main cause for no access to handwashing facility as the coefficient value is around 40%.


# In[45]:


r2_score(y,model.predict(x))


# In[46]:


df.head()


# In[47]:


#For all countries
q=df
q.drop('Entity',axis=1,inplace=True)
q.head(2)


# In[48]:


#For All country
plt.figure(figsize=(30,10))
df10 = q.melt('Year', var_name='cols',  value_name='vals')
g = sns.factorplot(x="Year", y="vals", hue='cols', data=df10)
plt.xticks(rotation=90)
plt.show()


# In[49]:


q=India


# In[50]:


q.drop('Entity',axis=1,inplace=True)


# In[51]:


#For India
df10 = q.melt('Year', var_name='cols',  value_name='vals')
g = sns.factorplot(x="Year", y="vals", hue='cols', data=df10)
plt.xticks(rotation=90)
plt.show()


# In[52]:


q=Pakistan
q.drop('Entity',axis=1,inplace=True)
#For Pakistan
plt.figure(figsize=(30,20))
df10 = q.melt('Year', var_name='cols',  value_name='vals')
g = sns.factorplot(x="Year", y="vals", hue='cols', data=df10)
plt.xticks(rotation=90)
plt.show()


# In[53]:


#In the world the major cause for death is High Systolic blood Pressure
#so checking the regression of it with other column

#x=df[['High fasting plasma glucose','Smoking','Alcohol use','Diet low in fruits','Diet low in vegetables','Low physical activity','Diet low in whole grains','Diet high in sodium','Diet low in nuts and seeds']]
#One of the assumptions of linear regression is that the independent variables need to be uncorrelated with each other.
x=df[['Smoking','High fasting plasma glucose']]
y=df['High systolic blood pressure']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)


# In[ ]:





# In[54]:


#In India,death due to High Systolic blood Pressure is increasing rapidly
#so checking the regression of it with other column
x=India[['Smoking','High fasting plasma glucose']]
y=India['High systolic blood pressure']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)

plt.title("High systolic blood pressure In India")
plt.plot(India['Smoking'],India['High systolic blood pressure'],label="Smoking")
plt.plot(India['High fasting plasma glucose'],India['High systolic blood pressure'],label="HF-Plasma Glucose")
plt.plot(x,model.predict(x),color="green",label="Predicted")
plt.legend()
plt.xlabel("High fasting plasma glucose,Smoking")
plt.ylabel('High systolic blood pressure')
plt.savefig('HS_BloodPressure_India.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:





# In[55]:


#In Pakistan,death due to High Systolic blood Pressure is very high
#so checking the regression of it with other column

x=Pakistan[['Smoking','High fasting plasma glucose']]
y=Pakistan['High systolic blood pressure']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)


plt.title("High systolic blood pressure In Pakistan")

plt.plot(Pakistan['Smoking'],Pakistan['High systolic blood pressure'],label="Smoking")
plt.plot(Pakistan['High fasting plasma glucose'],Pakistan['High systolic blood pressure'],label="HF-Plasma Glucose")
plt.plot(x,model.predict(x),color="green",label="Predicted")
plt.legend()
plt.xlabel("High fasting plasma glucose,Smoking")
plt.ylabel('High systolic blood pressure')
plt.savefig('HS_BloodPressure_Pakistan.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:





# In[56]:


#For All country Doing Mutiple regression
#Independent
x=df[['Unsafe water source','Unsafe sanitation']]
#Dependent
y=df['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)


# In[57]:


#For India Doing Mutiple regression
#Independent
x=India[['Unsafe water source','Unsafe sanitation']]
#Dependent
y=India['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)
#This shows that the Unsafe water souce is the main cause for no access to handwashing facility as the coefficient value is more than 50%.

plt.title("No access to handwashing facility in India")
plt.plot(India['Unsafe water source'],India['No access to handwashing facility'],label="Water")
plt.plot(India['Unsafe sanitation'],India['No access to handwashing facility'],label="Sanitation")
plt.plot(x,model.predict(x),color="green",label="Predicted")
plt.legend()
plt.xlabel("Unsafe water source,Unsafe sanitation")
plt.ylabel('No access to handwashing facility')
plt.savefig('Handwashing_India.png',format='png',bbox_inches='tight')
plt.show()


# In[58]:


#For Pakistan Doing Mutiple regression
#Independent
x=Pakistan[['Unsafe water source','Unsafe sanitation']]
#Dependent
y=Pakistan['No access to handwashing facility']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)
#This shows that the Unsafe sanitation souce is the main cause for no access to handwashing facility as the coefficient value is around 40%.

plt.title("No access to handwashing facility in Pakistan")
plt.plot(Pakistan['Unsafe water source'],Pakistan['No access to handwashing facility'],label="Water")
plt.plot(Pakistan['Unsafe sanitation'],Pakistan['No access to handwashing facility'],label="Sanitation")
plt.plot(x,model.predict(x),color="green",label="Predicted")
plt.legend()
plt.xlabel("Unsafe water source,Unsafe sanitation")
plt.ylabel('No access to handwashing facility')
plt.savefig('Handwashing_Pakistan.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:





# In[60]:


#For All country Doing Mutiple regression
#Independent
x=df[['Vitamin A deficiency','Child stunting','Low birth weight for gestation']]
#Dependent
y=df['Child wasting']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)

#Children who are thin for their height because of acute food shortages or disease.
#Deficiency of vitamin A is associated with significant morbidity and mortality from common childhood infections, and is the world’s leading preventable cause of childhood blindness.


# In[61]:


#For India Doing Mutiple regression
#Independent
x=India[['Vitamin A deficiency','Child stunting','Low birth weight for gestation']]
#Dependent
y=India['Child wasting']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)

plt.title("Child wasting in India")
plt.plot(India['Vitamin A deficiency'],India['Child wasting'],label="VitaminA")
plt.plot(India['Child stunting'],India['Child wasting'],label="Child Stunting")
plt.plot(India['Low birth weight for gestation'],India['Child wasting'],label="LowBirthWeight")
plt.plot(x,model.predict(x),color="pink",label="Predicted")
plt.legend()
plt.xlabel("'Vitamin A deficiency,Child stunting,Low birth weight for gestation")
plt.ylabel('Child wasting')
plt.savefig('ChildWasting_India.png',format='png',bbox_inches='tight')
plt.show()


# In[ ]:





# In[62]:


#For Pakistan Doing Mutiple regression
#Independent
x=Pakistan[['Vitamin A deficiency','Child stunting','Low birth weight for gestation']]
#Dependent
y=Pakistan['Child wasting']
model=LinearRegression()
model.fit(x,y)
print("R2 Score=>",r2_score(y,model.predict(x)))
print(model.coef_)

plt.title("Child wasting in Pakistan")
plt.plot(Pakistan['Vitamin A deficiency'],Pakistan['Child wasting'],label="VitaminA")
plt.plot(Pakistan['Child stunting'],Pakistan['Child wasting'],label="Child Stunting")
plt.plot(Pakistan['Low birth weight for gestation'],Pakistan['Child wasting'],label="LowBirthWeight")
plt.plot(x,model.predict(x),color="pink",label="Predicted")
plt.legend()
plt.xlabel("Vitamin A deficiency,Child stunting,Low birth weight for gestation")
plt.ylabel('Child wasting')
plt.savefig('ChildWasting_Pakistan.png',format='png',bbox_inches='tight')
plt.show()


# In[63]:


r2_score(y,model.predict(x))


# In[64]:


df.dropna(inplace=True)


# In[65]:


#Dependent->Air Pollution
#Independent->Household air pollution from solid fuels,Smoking,Outdoor air pollution
#For All country Doing Mutiple regression
x=df[['Household air pollution from solid fuels','Smoking','Outdoor air pollution']]
y=df['Air pollution']
model=LinearRegression()
model.fit(x,y)
print(model.coef_)
print("R2 Score=>",r2_score(y,model.predict(x)))


# In[ ]:





# In[66]:


#Dependent->Air Pollution
#Independent->Household air pollution from solid fuels,Smoking,Outdoor air pollution

#For India Doing Mutiple regression
x=India[['Household air pollution from solid fuels','Smoking','Outdoor air pollution']]
y=India['Air pollution']
model=LinearRegression()
model.fit(x,y)
print(model.coef_)

plt.title("Deaths Due To Air Pollution in India")
plt.plot(India['Household air pollution from solid fuels'],India['Air pollution'],label="Household AP")
plt.plot(India['Smoking'],India['Air pollution'],label="Smoking")
plt.plot(India['Outdoor air pollution'],India['Air pollution'],label="Outdoor AP")
plt.plot(x,model.predict(x),color="pink",label="Predicted")
plt.legend()
plt.xlabel("Outdoor air pollution,Household air pollution from solid fuels,Smoking")
plt.ylabel('Air pollution')
plt.savefig('Air Pollution_India.png',format='png',bbox_inches='tight')
plt.show()
print("R2 Score=>",r2_score(y,model.predict(x)))


# In[67]:


#Dependent->Air Pollution
#Independent->Household air pollution from solid fuels,Smoking,Outdoor air pollution

#For Pakistan Doing Mutiple regression
#Independent
x=Pakistan[['Household air pollution from solid fuels','Smoking','Outdoor air pollution']]
#Depenent
y=Pakistan['Air pollution']
model=LinearRegression()
model.fit(x,y)
print(model.coef_)

plt.title("Deaths Due To Air Pollution in Pakistan")
plt.plot(Pakistan['Household air pollution from solid fuels'],Pakistan['Air pollution'],label="Household AP")
plt.plot(Pakistan['Smoking'],Pakistan['Air pollution'],label="Smoking")
plt.plot(Pakistan['Outdoor air pollution'],Pakistan['Air pollution'],label="Outdoor AP")
plt.plot(x,model.predict(x),color="pink",label="Predicted")
plt.legend()
plt.xlabel("Outdoor air pollution,Household air pollution from solid fuels,Smoking")
plt.ylabel('Air pollution')
plt.savefig('Air Pollution_Pakistan.png',format='png',bbox_inches='tight')
plt.show()
print("R2 Score=>",r2_score(y,model.predict(x)))


# In[ ]:





# In[69]:


#For India doing Polynomial regression on columns Diet Low in whole grains and Alcohol Use
#Independent
x=India[['Diet low in whole grains']]
#Dependent
y=India['Alcohol use']
#Using Linear Regression and obtained a score of 95%
model=LinearRegression()
model.fit(x,y)
print(model.score(x,y)*100)
print(model.coef_)

from sklearn.preprocessing import PolynomialFeatures
model1=PolynomialFeatures(degree=4)
x=np.array(list(India['Diet low in whole grains']))
x=x.reshape(-1,1)
X=model1.fit_transform(x)
model.fit(X,India['Alcohol use'])

plt.title("Deaths Due To Alcohol Use in India")
plt.scatter(India['Diet low in whole grains'],India['Alcohol use'],label="Low Diet",color="red")
plt.plot(India['Diet low in whole grains'],model.predict(X),color="green",label="Predicted")
plt.legend()
plt.xlabel("Diet Low in Whole Grain")
plt.ylabel('Alcohol Use')
plt.savefig('Alcohol_India.png',format='png',bbox_inches='tight')
plt.show()
print(model.coef_)
print("R2 Score=>",r2_score(India['Alcohol use'],model.predict(X)))


# In[70]:


#For Pakistan doing Polynomial regression on columns Diet Low in whole grains and Alcohol Use
#Independent
x=Pakistan[['Diet low in whole grains']]
#Dependent
y=Pakistan['Alcohol use']
model=LinearRegression()
model.fit(x,y)
print(model.score(x,y)*100)
print(model.coef_)

model1=PolynomialFeatures(degree=4)
x=np.array(list(Pakistan['Diet low in whole grains']))
x=x.reshape(-1,1)
X=model1.fit_transform(x)
model.fit(X,Pakistan['Alcohol use'])

plt.title("Deaths Due Alcohol Use in Pakistan")
plt.scatter(Pakistan['Diet low in whole grains'],Pakistan['Alcohol use'],label="Low Diet",color="red")
plt.plot(Pakistan['Diet low in whole grains'],model.predict(X),color="green",label="Predicted")
plt.legend()
plt.xlabel("Diet Low in Whole Grain")
plt.ylabel('Alcohol Use')
plt.savefig('Alcohol_Pakistan.png',format='png',bbox_inches='tight')
plt.show()
print(model.coef_)
print("R2 Score=>",r2_score(Pakistan['Alcohol use'],model.predict(X)))


# In[ ]:




