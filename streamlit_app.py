
import streamlit 
streamlit.title("Demo App")
streamlit.text("sample 1")
streamlit.text("sample 2")
streamlit.text("sample 3")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 
my_fruit = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit = my_fruit.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick Some fruits:" , list(my_fruit.index))
fruits_to_show = my_fruit.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
