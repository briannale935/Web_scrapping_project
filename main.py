import requests 
from bs4 import BeautifulSoup 

# initializing url1
url1= "https://www2.hm.com/en_ca/women/shop-by-product/view-all.html?offset=36&page-size=108"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

# initializing url2
url2="https://www.aritzia.com/en/clothing"

# initializing lists and dictionaries
items1= []
prices1= []
matches1=[]
store1 = {}

items2= []
prices2= []
products2=[]
all_prices2= []
matches2= []
store2= {}

# Scrapping Website 1
while True: 
    request= requests.get(url1, headers=headers)
    doc = BeautifulSoup(request.text, "html.parser")

    # creating a list of all products on site 1 and appending it to the list "items1"
    products = doc.find_all("a", class_="link")
    for product in products: 
        items1.append(product.text)

    #creating a list of prices on site 1 and appending it to the list "prices1"
    prices = doc.find_all ("span", class_= "price regular")
    for price in prices:  
        prices1.append(price.text)


    #scrapping the next page 
    next_page = doc.find("a", class_="pagination-links-next")
    if next_page:
        url1 = "https://www2.hm.com" + next_page.get("href")
    else:
        break

# Searching for keywords 
# Takes the words that users searches and finds all products with the same words and appends it to a list
user_item= input("Enter an item from store 1: ")
list_user_word= user_item.split(" ")

for word1 in list_user_word: 
    for word2 in items1: 
        if word1 in word2: 
            matches1.append(word2)

# stores the items its price in a dictionary 
for k in matches1: 
    index=items1.index(k)
    price=prices1[index]
    if k not in store1: 
        store1[k]=price

print (f" Store 1: {store1}")

# Scrapping Website 2
while True: 
    request2= requests.get(url2, headers=headers)
    doc2 = BeautifulSoup(request2.text, "html.parser")

# creating a list of all products on site 2 and appending it to the list "items2"
    product_tag = doc2.find_all("div", class_="f0 product-name ar-product-name js-product-plp-name pr4-ns")    
    for tag in product_tag: 
        product_name= tag.find("a")["title"]
        products2.append(product_name)
    for product2 in products2: 
        items2.append(product2)


#creating a list of prices on site 2 and appending it to the list "prices2"
    price_tag = doc2.find_all("div", class_= "f0 product-pricing")
    for tag_ in price_tag: 
        price2= tag_.find("span", class_="js-product__sales-price")
        price2_actual= price2.find("span")
        all_prices2.append(price2_actual.text)
    for price2 in all_prices2: 
        prices2.append(price2)
    
    
#scrapping the next page 
    next_page2 = doc2.find("a", class_="js-load-more__button mb3")
    if next_page2:
        url2 = "https://www.aritzia.com" + next_page2.get("href")
    else:
        break

# Searching for keywords 
# Takes the words that users searches and finds all products with the same words and appends it to a list
user_item2= input("Enter an item from store 2: ")
list_user_word2= user_item2.split(" ")

for word1_store2 in list_user_word2: 
    for word2_store2 in items2: 
        if word1_store2 in word2_store2: 
            matches2.append(word2_store2)

# stores the items its price in a dictionary 
for j in matches2: 
    index2=items2.index(j)
    price2=prices2[index2]
    if j not in store2: 
        store2[j]=price2

print (f" Store 2: {store2}")
