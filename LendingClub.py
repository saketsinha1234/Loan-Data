# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:46:06 2022

@author: anami
"""

import pandas as pd
import numpy as np
#file_name = pd.read_csv('file.csv') <----format of read_csv


loandata = pd.read_csv('loan_data.csv', sep=',')

loandata.info()

loandata['purpose'].unique()

loandata.describe()

loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

loandata.info()
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income


length = len(loandata)
ficocat = []

for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
            
    except:
        cat = 'Error - Unknown'
    ficocat.append(cat)

ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat
loandata.info()

loandata.loc[loandata['int.rate'] > 0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12,'int.rate.type'] = 'Low'

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green',width=0.1)
plt.show

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'red',width=0.2)
plt.show

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color='#4caf50')
plt.show


loandata.to_csv('loan_cleaned.csv', index = True)
