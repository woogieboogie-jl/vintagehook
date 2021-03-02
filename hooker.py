import requests
from bs4 import BeautifulSoup as bs
import json

shop_json = open("vintageshop_list.json")
shops_data = json.load(shop_json)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print(url_dict)


def shopInput(shops_data):
    for key in shops_data:
        print(key)
    while True:
        shop = input("choose your wanted vintage site for crawling...")
        if shop in shops_data.keys():
            shop_data = shops_data[shop]\
            url = shop_data["url"]
            selector = shop_data["selector"]
            break()
        elif shop not in shops_data.keys():
            print("not in vintage shops list")
        else:
            print("unexpected error!...")
    return url selector

def initiate(url):
    r = requests.get(url)
    if r.status_code == 200:
        r_text = r.text
    else: 
        print("requested url not avaliable!...")
    return r_text


def SoupGet(r_text):
    soup = bs(r_text,'html.parser')
    soup_str = soup.prettify()
    return soup_str

def SoupCrawl(soup_str, selector)
    soup_str



def main():
    url, selector = shopInput(shops_data)
    r_text = initiate(url)
    soup_str = SoupGet(r_text)