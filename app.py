
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os
from prettytable import PrettyTable
from termcolor import colored
os.system('color')


search = input('What product do you search for\n')
sCleaned = search.replace(" ", "+")
# print(sCleaned)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = "https://www.etsy.com/fr/search?q={}&explicit=1&order=highest_reviews".format(sCleaned)
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

# Python code to find frequency of each word
def freq(str):
 
    # break the string into list of words
    str = str.split()        
    str2 = []
    str3 = ["is", "-", "/", "et","de", "a", "•", '|', "la", "le", "the", "pour", "and", "of", "&", ",", ".", ":" ]
 
    # loop till string values present in list str
    for i in str:            
 
        # checking for the duplicacy
        if i not in str2 and i not in str3:
 
            # insert value in str2
            str2.append(i)
             
    for i in range(0, len(str2)):
 
        # count the frequency of each word(present
        # in str2) in str and print
        if str.count(str2[i]) > 5:
            
            
        	print('Frequency of', str2[i], 'is :', str.count(str2[i]))
         	my_table = PrettyTable()
			my_table.field_names = ["No.", "Keyword"]
			my_table.add_row([str.count(str2[i]), str2[i]])
         
        
        
for item in soup.select('.v2-listing-card__info'):
	try:
		file_object = open('text.txt', 'a')
  
		titre = item.select('h3')[0].get_text().strip()
		prix = item.select('.currency-value')[0].get_text().strip()
		stars = item.select('.wt-screen-reader-only')[0].get_text().strip()
		extra = item.select('.wt-text-caption')[1].get_text().strip()
		print('----------------------------------------')

		print(colored(f"TITRE: {titre}" , 'white', attrs=['bold', 'blink']))
		print(colored(f"Prix: {prix}", 'green', attrs=['reverse', 'blink']))
		print(colored(f"Stars: {stars}" , 'yellow', attrs=['reverse', 'blink']))
		print(colored(f"Extra Infos: {extra}" , 'blue', attrs=['bold', 'blink']))
  
		print('----------------------------------------')
		# Append at the end of file
		file_object.write(titre)
		# Close the file
		file_object.close()
		# print(item)
		# print(item.select('h3')[0].get_text().strip())
		# print(item.select('.currency-value')[0].get_text().strip())
		# print(item.select('.wt-screen-reader-only')[0].get_text().strip())
		# print(item.select('.wt-text-caption')[1].get_text().strip())
		# print(item.select('.wt-text-caption')[0]['src'])

	except Exception as e:
		raise e

		
with open('text.txt', 'r') as file:
    data = file.read().replace('\n', '')  
str = data
freq(str)
