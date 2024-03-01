import streamlit as st
import original as file_module

st.title("Product Price Comparison")

name = st.text_input("Enter Product Name:")
if st.button("Search"):
    st.write("Searching...")
    flipkart_price1 = file_module.flipkart(name)
    amazon_price1 = file_module.amazon(name)
    
    if flipkart_price1 == '0':
        st.write("Flipkart: No product found!")
    else:
        st.write(f"Flipkart Price: ₹{flipkart_price1}")

    if amazon_price1== '0':
        st.write("Amazon: No product found!")
    else:
        st.write(f"Amazon Price: ₹{amazon_price1}")
    min_price = min(flipkart_price1, amazon_price1)

    if min_price == flipkart_price1:
                st.write("Minimum Price is on Flipkart")
                st.write("Minimum Price: ₹", min_price)
              
    else:
                st.write("Minimum Price is on Amazon")
                st.write("Minimum Price: ₹", min_price)
               
