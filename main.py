import requests
from bs4 import BeautifulSoup
import csv
from html import unescape, escape


URL = "https://www.geeksforgeeks.org/top-10-programming-languages-to-learn-in-2022/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
data_list = soup.findAll(name="h3")
link_text = []
for link in data_list:
    link_text.append(link.text)
    print(link.text)

with open('programming.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    title_text = "Top 10 programming languages in 2022"
    writer.writerow([unescape(title_text)])

    for link in data_list:
        writer.writerow([link.text.strip()])


