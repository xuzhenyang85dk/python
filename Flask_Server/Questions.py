import pandas as pan
import Pygal_generator

dFrame = pan.read_csv("./data/NZ_DataSet.csv.tsv", sep='\t')

def getQuestions():
    questions = {1:["How many products have been tested?", "http://www.iconarchive.com/download/i87059/graphicloads/colorful-long-shadow/Chart-pie.ico"],
                2:["How many times have each product been tested?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                3:["When was 'Tuna - canned' cheapest?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                4:["When was 'Tuna - canned' most expensive?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                5:["Show the most cheapest product.", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                6:["Show the most expensive product.", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                7:["Show the top 10 cheapest food products", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                8:["Show the top 10 most expensive food products.", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                9:["What was the average price for 1 kg bananas in 2012?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                10:["What was the average price for 1 kg bananas in 2013?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                11:["What was the price for 1 kg carrots in marts 2012?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                12:["What was the price for 1 kg carrots in marts 2013?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                13:["In which period was 1 kg kiwi cheapestand what was the price (Show top 10)?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"],
                14:["In which period was 1 kg kiwi most expensive and what was the price (Show top 10)?", "http://placehold.it/460x250/e67e22/ffffff&text=HTML5"]
                }
    return questions

def execQ1():

    out = dFrame.columns(['Series_title_1'])

    '''testvar = {"heyData":25,"whyData":25,"dudeData":50}

    total_amount = Pygal_generator.createPie(testvar, title="test8")'''
    return out

def exec02():
    pass
    return
