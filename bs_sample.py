from bs4 import BeautifulSoup
import requests

# this is used to analyze the data we collected from html

content = requests.get("http://books.toscrape.com/").text
soup = BeautifulSoup(content, "html.parser")
# there are a lot of things that BeautifulSoup can do, so we have to identify a parser.
# it will be analyzed into a tree-like structure.
# print(soup.p) will print the first text-paragraph element in the html.
# print(soup.img) will print the first image element in the html.
# e.g. in this website, all the price info are classified as "price_color")
# therefore, if we want all the price, we can do
# all_prices = soup.findAll("p", attrs = {"class": "price_color"})
# the key and value in attrs will be the price we want.
all_prices = soup.findAll("p", attrs={"class": "price_color"})
for price in all_prices:
    print(price.string[2:])  # to get rid of useless information

# how to find all the book names
all_titles = soup.findAll("h3")  # we don't need attrs here
# because we don't need to filter the data according to the class
for title in all_titles:
    all_links = title.findAll("a")
    for link in all_links:
        print(link.string)
