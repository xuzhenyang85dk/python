import webget
import pandas as pd
import matplotlib.pyplot as plt
import os
import statistics
from collections import Counter

URL = 'https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv'
webget.download(URL)
df = pd.read_csv('ks-projects-201801.csv')
main_category_lst = []

def question1():
    for _, row in df.iterrows():
        if row['state'] == 'successful':
            main_category_lst.append(row['main_category'])
    res_category = max(set(main_category_lst),key=main_category_lst.count)
    print('1. What main-category of project has the highest success rate?')
    print('The highest success rate of project is: {} '.format(res_category))
    # here counter how many Music projects
    def counter_category(lst,cat):
        counter = 0
        for idx in lst:
            if idx == cat:
                counter +=1
        return counter
    cat_amount = counter_category(main_category_lst,'Music')
    print('The amount are: {}'.format(cat_amount))
    x = list(set(main_category_lst))
    # list of succes project amount
    y = [6534,12300,2338,24197,5593,6085,5842,3305,11510,10550,2115,23623,1012,6434,12518]
    plt.figure(figsize=(18,10))
    plt.bar(x,y, align='center',color = 'lightblue',label='Main Categories')
    plt.title('The highest success rate',fontsize = 14)
    plt.xlabel('Main Categories',fontsize= 12)
    plt.legend()
    plt.show()
    plt.savefig(os.path.join('highest_succes_rate.png'), dpi=300, format='png', bbox_inches='tight')

def question2():
    main_category_series = df['main_category'].value_counts()
    print('2. For the main-category of project with highest success rate (question above), what is the main-category with the highest number of project proposals?')
    print('The highest number of project proposals is: {} '.format(main_category_series.index[0]))
    main_category_series.plot.bar(color='lightblue',figsize = (8,6),label='words',align='center')
    plt.title('The highest number of project proposals',fontsize = 14)
    plt.xlabel('Main Categories',fontsize= 12)
    plt.show()
    plt.savefig(os.path.join('highest_number_of_project_proposals.png'), dpi=300, format='png', bbox_inches='tight')

def question3():
    pledged_amout_lst = []
    for _, row in df.iterrows():
        if row['state'] == 'successful':
            pledged_amout_lst.append(row['usd_pledged_real'])
    median_pledged_amount = statistics.median(pledged_amout_lst)
    print('3. What is the median pledged amount (usd_pledged_real) of successfully funded projects?')
    print('The median pledged amount (usd_pledged_real) of successfully funded projects is: {}'.format(median_pledged_amount))

def question4():
    categories = []
    for _, row in df.iterrows():
        if row['state'] == 'successful':
            if row['usd_pledged_real'] >= 5000:
                categories.append(row['main_category'])
    counter_categories =Counter(categories)
    res = list(counter_categories.most_common(1))
    print('4. What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per main-category?')
    print('The number of successfully funded projects with more than 5.000$ pledged is: {} '.format(res[0]))
    lables,values =  zip(*Counter(categories).items())
    plt.figure(figsize=(18,10))
    plt.bar(lables,values,align='center',color = 'lightblue',label='Main Categories')
    plt.show()
    plt.savefig(os.path.join('number_of_success_project_more_than_5000.png'), dpi=300, format='png', bbox_inches='tight')


def question5():
    fst_lst,sec_lst, trd_lst, fourth_lst, fifth_lst,six_lst = [], [], [], [], [], []
    for _, row in df.iterrows():
        if row['usd_goal_real'] <= 10000:
            fst_lst.append(row['main_category'])
        if row['usd_goal_real'] > 10000 and row['usd_goal_real'] <= 20000:
            sec_lst.append(row['main_category'])
        if row['usd_goal_real'] > 20000 and row['usd_goal_real'] <= 30000:
            trd_lst.append(row['main_category'])
        if row['usd_goal_real'] > 30000 and row['usd_goal_real'] <= 40000:
            fourth_lst.append(row['main_category'])
        if row['usd_goal_real'] > 40000 and row['usd_goal_real'] <= 50000:
            fifth_lst.append(row['main_category'])
        if row['usd_goal_real'] > 50000 :
            six_lst.append(row['main_category'])
    print('5.For the main-category with the most successfully funded projects (quantity, not rate of success), what is the goal-amount range (usd_goal_real), e.g. range 0-10k$ , 5-15k$, 100k$-110k$, that contains the most successfully funded projects (in quantity, not rate of success)?')
    print('Range 0 - 10k$ are: {}'.format(list(Counter(fst_lst).most_common())))
    print('Range 10k - 20k are: {}'.format(list(Counter(sec_lst).most_common())))
    print('Range 20k - 30k are: {}'.format(list(Counter(trd_lst).most_common())))
    print('Range 30k - 40k are: {}'.format(list(Counter(fourth_lst).most_common())))
    print('Range 40k - 50k are: {}'.format(list(Counter(fifth_lst).most_common())))
    print('Range 60k and more are: {}'.format(list(Counter(six_lst).most_common())))
    lables, values = zip(*Counter(fst_lst).items())
    plt.figure(figsize=(18,10))
    plt.bar(lables,values,align='center',color = 'lightblue',label='Main Categories')
    plt.title('The most successfully funded projects range 0-10k$ ',fontsize = 14)
    plt.xlabel('Main Category',fontsize= 12)
    plt.show()
    plt.savefig(os.path.join('10k.png'), dpi=300, format='png', bbox_inches='tight')

question1()  
question2()
question3()
question4()
question5()
