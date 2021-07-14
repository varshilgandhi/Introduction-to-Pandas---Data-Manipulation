# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:13:28 2021

@author: abc
"""

#DELETING COLUMNS

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df1 = df.drop('Manual2',axis=1)     #Manual2 is delete from dataset
print(df1.head())


############################################################################

#Delete Multiple Columns

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df2 = df.drop(['Manual2','Auto_th_2'],axis=1)      #Manual2 and Auto_th_2 delete from dataset 
print(df.head())
print(df2.head())


##############################################################################

#Insert Columns 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df['Date'] = '2019-06-24'        #Date Columns insertv in dataset

print(df.head())

################################################################################

#Change datatypes 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')
df['Date'] = '2019-06-24'
print(df.head())
print(df.dtypes)


df['Date'] = pd.to_datetime('2019-06-24')
print(df.head())
print(df.dtypes)


#############################################################################


#Create a new csv file or rename and update exist csv file

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df.to_csv('manual_vs_auto_updated.csv')


#####################################################################

#Delete Rows 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df1 = df.drop(df.index[1])     #it's delete first index row from dataset
print(df.head())
print(df1.head())


#####################################################################

#Delete Multiple rows 

import pandas as pd

df = pd.read_csv('manual_vs_auto.csv')

df1 = df.iloc[10:,]       #it's delete first 10 index rows from dataset
print(df.head())
print(df1.head())


#######################################################################

#Delete particular one set

import pandas as pd
df =pd.read_csv('manual_vs_auto.csv')

df1 = df[df['Unnamed: 0'] != 'Set1']          #here set1 is deleted from dataset

print(df.head())
print(df1.head())

print(df1.tail())



#########################################################################

                        #THANK YOU
                        #GARR PEE RAHE SURKSIT RAHE 









