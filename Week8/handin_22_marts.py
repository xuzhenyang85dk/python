import pandas as pd
import webget
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
import os

URL = 'https://raw.githubusercontent.com/KasperOnFire/ImpossibleTechnology/master/Datasets/songdata.csv'
webget.download(URL)
df = pd.read_csv('./songdata.csv')
words = df['text'].str.split(expand=True).stack().value_counts()
cleaned_data = df['text'].str.replace('\n','').str.replace('(','').str.replace('?','').str.replace(')','').str.replace(',','').str.lower()
data_list = cleaned_data.str.split()

def question1():
    top1 = words[:1]
    print('Question 1 - What is the most used words in the songs?')
    print('The most used words in the songs is: \n{}'.format(top1.index[0]))
    print('and the amount is: \n{}'.format(int(top1.values)))
    top10 = words[:10]
    top10.plot.bar(color='rgbym',figsize = (8,6),label='words')
    plt.title('Top 10 of the most used words',fontsize = 14)
    plt.xlabel('The most used words',fontsize= 12)
    plt.ylabel('Amount',fontsize = 12)
    plt.legend()
    plt.show()
    plt.savefig(os.path.join('top5.png'), dpi=300, format='png', bbox_inches='tight')
question1()

"""
Solution
Question 1 - What is the most used words in the songs?
The most used words in the songs is: 
the
and the amount is: 
446872
"""

def question2(song_id):
    
    # removed '\n', '(', ')', ','
    cleaned_data = df['text'].str.replace('\n','').str.replace('(','').str.replace(')','').str.replace('?','').str.lower()
    # splited the choiced song up to words
    data_list = cleaned_data.str.split()
    # countered and sorted each words of the choiced song
    splited_words = list(Counter(data_list[song_id]).most_common())

    print('Question 2 - How many times are each word repeated in a song? (Or perhaps - what song repeats the top 4 repeated words the most? - finds the most repetitive song)')
    print('Each word repeated in a song are: \n{}'.format(splited_words))

    words,amount = zip(*splited_words[:10])
    plt.figure(figsize=(10,5))
    plt.bar(words,amount, align='center',color = 'slategrey',label='Repeated words in a song')
    plt.legend()
    plt.show()
    plt.savefig(os.path.join('repeated_words.png'), dpi=300, format='png', bbox_inches='tight')
question2(0)

"""
Solution
Question 2 - How many times are each word repeated in a song? (Or perhaps - what song repeats the top 4 repeated words the most? - finds the most repetitive song)
Each word repeated in a song are: 
[('she', 9), ('could', 8), ('and', 7), ('me', 7), ('my', 5), ('that', 4), 
("she's", 4), ('just', 4), ('kind', 4), ('of', 4), ('girl', 4), ('ever', 4), 
('what', 4), ('i', 4), ('do', 4), ('her', 3), ('the', 3), ('be', 3), ('look', 2), 
('at', 2), ('face', 2), ('a', 2), ('when', 2), ('makes', 2), ('feel', 2), ('fine', 2), 
('who', 2), ('believe', 2), ('mine', 2), ('without', 2), ("i'm", 2), ('blue', 2), 
('if', 2), ('leaves', 2), ('we', 2), ('go', 2), ('for', 2), ("it's", 1), 
('wonderful', 1), ('it', 1), ('means', 1), ('something', 1), ('special', 1), 
('to', 1), ('way', 1), ('smiles', 1), ('sees', 1), ('how', 1), ('lucky', 1), 
('can', 1), ('one', 1), ('fellow', 1), ('walk', 1), ('in', 1), ('park', 1), 
('holds', 1), ('squeezes', 1), ('hand', 1), ("we'll", 1), ('on', 1), ('walking', 1), 
('hours', 1), ('talking', 1), ('about', 1), ('all', 1), ('things', 1), ('plan', 1)]
"""

def question3(word):
    res = 0
    index = 0
    song_name = df['song']
    for i, song in enumerate(cleaned_data):
        word_counter = 0
        for row in data_list[i]:
            if row == word:
                word_counter += 1
        if res < word_counter:
            index = i
            res = word_counter
    print('What song uses the word "X" the most time? (X meaning a specific word, choose your own!)')
    print('You choiced word: {}'.format(word))
    print('The song: {}'.format(song_name[index]))
    print('Amount: {}'.format(res))
# Hint: choice one word with lower characters
question3('the')

"""
Solution
What song uses the word "X" the most time? (X meaning a specific word, choose your own!)
You choiced word: the
The song: Bando
Amount: 127
"""

def question4():
    print('Question 4 - What is the average number of words in each song?')
    for i, song in enumerate(cleaned_data):
        # countered and sorted each words of the choiced song
        splited_words = Counter(data_list[i]).most_common()
        sum = 0
        length = len(splited_words)
        for word, num in splited_words:
            sum += num
        res = sum/length
        print('The average number of words is: {}'.format(res))
question4()
"""
Solution
Question 4 - What is the average number of words in each song?
The average number of words is: 2.283582089552239
The average number of words is: 3.7681159420289854
The average number of words is: 2.8363636363636364
...
"""

def question5():
    print('Question 5 - Show the distribution of number of words in the songs. (Example: how many songs have 5-10 words, 10-20 words)')
    lst = []
    hundred_lst = []
    two_hundred_lst = []
    three_hundred_lst = []
    four_hundred_lst = []
    five_hundred_lst = []
    six_hundred_lst = []
    seven_hundred_lst = []
    eight_hundred_lst = []
    # counted words in each songs and saved to a list
    for i,idx in enumerate(data_list):
        lst.append(len(data_list[i]))
    lst.sort()
    # splited the list into 8 diffrent lists
    for i,words in enumerate(lst):
        if words < 101:
            hundred_lst.append(words)
        if words > 100 and words < 201:
            two_hundred_lst.append(words)
        if words > 200 and words < 301:
            three_hundred_lst.append(words)
        if words > 300 and words < 401:
            four_hundred_lst.append(words)
        if words > 400 and words < 501:
            five_hundred_lst.append(words)
        if words > 500 and words < 601:
            six_hundred_lst.append(words)
        if words > 600 and words < 701:
            seven_hundred_lst.append(words)
        if words > 700 and words < 850:
            eight_hundred_lst.append(words)
    # saved distribution number into one list
    total_lst = len(hundred_lst)+len(two_hundred_lst)+len(three_hundred_lst)+len(four_hundred_lst)+len(five_hundred_lst)+len(six_hundred_lst)+len(seven_hundred_lst)+len(eight_hundred_lst)
    print('Total amount of words: {}'.format(total_lst))
    print('Songs have 0-100 words: {}'.format(len(hundred_lst)))
    print('Songs have 100-200 words: {}'.format(len(two_hundred_lst)))
    print('Songs have 200-300 words: {}'.format(len(three_hundred_lst)))
    print('Songs have 300-400 words: {}'.format(len(four_hundred_lst)))
    print('Songs have 400-500 words: {}'.format(len(five_hundred_lst)))
    print('Songs have 500-600 words: {}'.format(len(six_hundred_lst)))
    print('Songs have 600-700 words: {}'.format(len(seven_hundred_lst)))
    print('Songs have 700-800 words: {}'.format(len(eight_hundred_lst)))
question5()

"""
Solution
Question 5 - Show the distribution of number of words in the songs. (Example: how many songs have 5-10 words, 10-20 words)
Total amount of words: 57650
Songs have 0-100 words: 3715
Songs have 100-200 words: 26429
Songs have 200-300 words: 17785
Songs have 300-400 words: 6008
Songs have 400-500 words: 1923
Songs have 500-600 words: 1020
Songs have 600-700 words: 603
Songs have 700-800 words: 167
"""