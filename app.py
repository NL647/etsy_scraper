import os
import requests
from bs4 import BeautifulSoup
from termcolor import colored
from prettytable import PrettyTable

# Set headers
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

# Get search term and construct URL
sCleaned = input("Search Etsy: ")
url = "https://www.etsy.com/search?q={}&explicit=1&order=highest_reviews".format(sCleaned)

#clean old txt file
os.remove("text.txt")

# Make request to URL
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

# Python code to find frequency of each word in the title of products for SEO
def freq(str):
    # convert the string to lowercase
    str = str.lower()

    # break the string into list of words
    str = str.split()

    # words to exclude from the count
    str3 = ["is", "-", "/", "et", "avec","de", "a", "•", ".", "|", "la", "le", "the", "pour", "and", "of", "&", ",", ".", "en", ":", "des", "d'", "à", "d’", "les", "aux", "a", "|"]

    # loop till string values present in list str
    str2 = []
    for i in str:
        # checking for the duplicate
        if i not in str2 and i not in str3:
            # insert value in str2
            str2.append(i)

    # create a dictionary to store the frequency of each word
    freq_dict = {}
    for word in str2:
        freq_dict[word] = str.count(word)

    # sort the dictionary by value (frequency) in descending order
    sorted_freq_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # print the result
    for word, freq in sorted_freq_dict:
        if freq > 2:
            print('Frequency of [ ', word, ' ] is :', freq)


items = []
for item in soup.select('.v2-listing-card__info'):
    try:
        titre = item.select('h3')[0].get_text().strip()
        prix = item.select('.currency-value')[0].get_text().strip()
        stars = item.select('input[name="initial-rating"]')[0]['value']   
        extra = item.select('.wt-text-caption')[1].get_text().strip()

        # Append data to list
        items.append({
            "titre": titre,
            "prix": prix,
            "stars": stars,
            "extra": extra
        })

    except Exception as e:
        raise e

# Sort items by stars from higher value to lower
sorted_items = sorted(items, key=lambda x: float(x['stars']), reverse=True)

# Create table to display data
table = PrettyTable(['Title', 'Price EUR', 'Stars', 'Num Reviews'])
for item in sorted_items:
    titre = item["titre"]
    prix = item["prix"]
    stars = item["stars"]
    extra = item["extra"]

    # Add row to table
    table.add_row([titre, prix, stars, extra])
    file_object = open('text.txt', 'a')
    file_object.write(titre)
        # Close the file
    file_object.close()

# Display table in console
print(table)

with open('text.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
print("\n== WORDS FREQUENCY ==\n")    
freq(data)
print("\n====\n") 


