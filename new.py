import streamlit as st
from bs4 import BeautifulSoup
import requests
headers = {'Accept': '*/*',
 'Accept-Encoding': 'identity, deflate, compress, gzip',
 'Authorization': u'Basic dXNlcjpwYXNz','User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

flipkart_url=''
amazon_url=''
def flipkart(name):
    try:
        global flipkart_url
        name1 = name.replace(" ","+")
        flipkart_url=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)


        st.write("\nSearching in flipkart....")
        soup = BeautifulSoup(res.text,'html.parser')
        
        if(soup.select('._4rR01T')):
            flipkart_name = soup.select('._4rR01T')[0].getText().strip().upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('._4rR01T')[0].getText().strip()
                st.write("Flipkart:")
                st.write(flipkart_name)
                st.write(flipkart_price)
                st.write("---------------------------------")
                
        elif(soup.select('.s1Q9rs')):
            flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
            flipkart_name = flipkart_name.upper()
            if name.upper() in flipkart_name:
                flipkart_price = soup.select('._30jeq3')[0].getText().strip()
                flipkart_name = soup.select('.s1Q9rs')[0].getText().strip()
                st.write("Flipkart:")
                st.write(flipkart_name)
                st.write(flipkart_price)
                st.write("---------------------------------")
        else:
            flipkart_price='0'
            
        return flipkart_price 
    except:
        st.write("Flipkart: No product found!")  
        st.write("---------------------------------")
        flipkart_price= '0'
    return flipkart_price

def amazon(name):
    try:
        global amazon_url
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon_url=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)
        st.write("\nSearching in amazon...")
        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()
                st.write("Amazon:")
                st.write(amazon_name)
                st.write("₹"+amazon_price)
                st.write("---------------------------------")
                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:
                    amazon_price = '0'
                    st.write("amazon : No product found!")
                    st.write("-----------------------------")
                    break
                    
        return amazon_price
    except:
       st.write("Amazon: No product found!")
       st.write("---------------------------------")
       amazon_price = '0'
    return amazon_price

def convert(a):
    b=a.replace(" ",'')
    c=b.replace("INR",'')
    d=c.replace(",",'')
    f=d.replace("₹",'')
    g=int(float(f))
    return g

st.title("Product Price Comparison")

name = st.text_input("Enter Product Name:")
if st.button("Search"):
    st.write("Searching...")
    flipkart_price = flipkart(name)
    amazon_price = amazon(name)
    min_price = min(flipkart_price, amazon_price)
    st.write("Minimum Price:", min_price)
    if min_price == flipkart_price:
        st.write("Minimum Price is on Flipkart")
    if min_price == amazon_price:
        st.write("Minimum Price is on Amazon")
            
