import pandas as pd 
import seaborn as sns 
import glob
import os
import matplotlib.pyplot as plt
import numpy as np


files = glob.glob('src/*csv')
registry_path = "files_registry.txt"  

if os.path.exists(registry_path):
    os.remove(registry_path)


def plotting_curve(data, y_axis, x_axis):
   
    ''' chart settings '''
    
    sns.lineplot(x= x_axis , y= y_axis, data=data)
    plt.title(f'Percent of {y_axis} by Temperature')
    plt.xlabel('Temperature in Celsius.')
    plt.ylabel(f'Percent of {y_axis}')
    plt.grid(True)

    plt.show() 

def plotting_all(datalist):

    ''' plotting all TG% and DTG% charts per file. '''

    for item in datalist:
        plotting_curve(item, 'TG%', 'Temp.')
        plotting_curve(item, 'DTG%', 'Temp.')  
        plotting_curve(item, 'Derivative_DTG%', 'Temp.')


def treating_data(file_path):

    ''' treating required data and remotion of texts applied by machines. '''

    global datas
    datas = [] 
    for file in file_path:
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

        with open("files_registry.txt", "a") as f:
            f.write(f"file :{file} \n")
            f.close()


try:
    treating_data(files)
    plotting_all(datas)

except Exception as error:
    print(error)




