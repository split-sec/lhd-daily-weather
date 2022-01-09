import sys
from termcolor import colored
import requests
import colorama
from bs4 import BeautifulSoup

#Storing the command line argument to a string variable
city = sys.argv[1]

#Sending a request
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

#Scraping data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs = {'class': 'BNeawe tAd8D AP7Wnd'}).text

data = str.split('\n')
time = data[0]
sky = data[1]

listdiv = soup.findAll('div', attrs = {'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[2].text

pos = strd.find('Wind')
other_data = strd[pos:]

#Color picking based on variable values
temp_i = int(temp[:2])
clr=""
if temp_i>40:
    clr = "red"
elif temp_i>30:
    clr = "yellow"
elif temp_i>10:
    clr = "blue"

#Displaying output
colorama.init()
print("Temperature is", end=" ")
txt = colored(temp, clr)
print(txt)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)

