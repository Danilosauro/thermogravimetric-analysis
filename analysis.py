import pandas as pd 
import seaborn as sns 
import glob
import matplotlib.pyplot as plt
import numpy as np


files = glob.glob('src/*csv')

def plotting_curve(data, y_axis, x_axis):
    
    sns.lineplot(x= x_axis , y= y_axis, data=data)
    plt.title(f'Percent of {y_axis} by Temperature')
    plt.xlabel('Temperature in Celsius.')
    plt.ylabel(f'Percent of {y_axis}')
    plt.grid(True)

    plt.show() 

def plotting_all(datalist):
    for item in datalist: 
        plotting_curve(item, 'TG%', 'Temp.')

    for item in datalist:
        plotting_curve(item, 'DTG%', 'Temp.') 
    
    for item in datalist: 
        plotting_curve(item, 'Derivative_DTG%', 'Temp.')

datas = [] 

for file in files: 
    data = pd.read_csv(file) 
    data = data.drop(0) 
    data['Temp.'] = data['Temp.'].str.replace(',','.').astype('float')
    data['TG'] = data['TG'].str.replace(',','.').astype('float')
    data['TG%'] = (data['TG'] * 100 / data['TG'].iloc[0]) 
    data['DTG'] = data['DTG'].str.replace(',','.').astype('float')
    data['DTG%'] = (data['DTG'] * 100 / 8.320312) 
    data['Derivative_DTG%'] = np.gradient(data['DTG%']) 
    data['Derivative_Temp.'] = np.gradient(data['Temp.'])
    datas.append(data) 

plotting_all(datas)



