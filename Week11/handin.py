import webget
import pandas as pd
import matplotlib.pyplot as plt
import os

URL = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv'

webget.download(URL)
df = pd.read_csv('./airline-safety.csv')

print('-------------- Assignment 9 - Dataset Charming P* --------------')
def question1():
    print('How many incidents happened between 1985-1999?')
    incidents_series = df['incidents_85_99']
    incidents_lst = incidents_series.values
    incidents_85_99 = sum(incidents_lst)
    print('Between 1985 - 1999 has been {} incidents'.format(incidents_85_99))
    # Anwser: Between 1985 - 1999 has been 402 incidents
    print('------------------------------------------------------')

def question2():
    print('How many death-incidents happened between 1985-1999?')
    death_incidents_series = df['fatal_accidents_85_99']
    death_incidents_lst = death_incidents_series.values
    res = sum(death_incidents_lst)
    print('Between 1985 - 1999 has been {} death-incidents'.format(res))
    # Anwser: Between 1985 - 1999 has been 122 death-incidents
    print('------------------------------------------------------')

def question3():
    print('How many incidents happened between 2000-2014?')
    incidents_00_14_series = df['incidents_00_14']
    incidents_00_14_lst = incidents_00_14_series.values
    incidents_00_14 = sum(incidents_00_14_lst)
    print('Between 2000 - 2014 has been {} incidents'.format(incidents_00_14))
    # Anwswer: Between 2000 - 2014 has been 231 incidents
    print('------------------------------------------------------')

def question4():
    print('How many death-incidents happened between 2000-2014?')
    fatal_accidents_00_14_series = df['fatal_accidents_00_14']
    fatal_accidents_00_14_lst = fatal_accidents_00_14_series.values
    res = sum(fatal_accidents_00_14_lst)
    print('Between 2000 - 2014 has been {} death-incidents'.format(res))
    # Answer: Between 2000 - 2014 has been 37 death-incidents
    print('------------------------------------------------------')

def question5():
    print('Has the amount of incidents increased, comparing the later statistics to the earlier ones?')
    plt.figure(figsize=(5,5))
    plt.title('Comparing incidents amount of 1985 - 1999 and 2000 - 2014')
    plt.xlabel('The years between 1985 - 1999 and 2000 - 2014',fontsize = 14)
    plt.ylabel('Incidents amount',fontsize = 14)
    x = ['1985 - 1999','2000 - 2014']
    y = [402,231]
    plt.bar(x,y,align='center',color = 'lightblue',label='incidents')
    plt.show()
    #plt.savefig(os.path.join('incidents.png'), dpi=300, format='png', bbox_inches='tight')
    print('The incidents amount has been decreased since 1985 to 2014')
    # Anwser: The incidents amount has been decreased since 1985 to 2014
    print('------------------------------------------------------')

question1()
question2()
question3()
question4()
question5()