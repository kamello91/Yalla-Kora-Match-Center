#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import csv


# In[2]:


Date = input('please enter the date ? (MM/DD/YYYY)')
url = requests.get(f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={Date}#days')


# In[4]:


def main(url):
    src = url.content
    soup = BeautifulSoup(src,'lxml')
    matches_list = []
    championships = soup.find_all('div',{'class' : 'matchCard'})
    def info(championships):
        
        #championship_title
        championship_title = championships.contents[1].find('h2').text.strip()
        
        #matches_info
        matches = championships.contents[3].find_all('li')
        num_matches = len(matches)
        
        #Get_teams
        for i in range (num_matches):
            
            teamA = matches[i].find('div',{'class' : 'teamA'}).text.strip()
            teamB = matches[i].find('div',{'class' : 'teamB'}).text.strip()
            
            #Get_score 
            result = matches[i].find('div',{'class' : 'MResult'}).find_all('span', {'class' : 'score'})
            score = f'{result[0].text.strip()} : {result[1].text.strip()}'
            
            #Get_time
            time = matches[i].find('div',{'class' : 'MResult'}).find('span', {'class' : 'time'}).text.strip()
            
            #Get_week
            week = matches[i].find('div',{'class' : 'date'}).text.strip()
            
            #List_append            
            matches_list.append({'اسم البطولة' : championship_title,
                                'الفريق الاول' : teamA,
                                'الفريق الثاني' : teamB,
                                 'النتيجة' :score,
                                'الوقت'     : time,
                                'الاسبوع' : week,})

    for i in range(len(championships)) :
        info(championships[i])
    
    
    keys = matches_list[0].keys()
    
    with open('yalla-kora.csv','w',encoding="utf-8") as file :
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_list)
        print('file created')
main(url)


# In[ ]:




