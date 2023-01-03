import streamlit as st 
import PIL
import pandas


st.set_page_config(layout="wide")

st.header("The Best Company!!!")
visionTetra = """La vision de la compañia es vender bueno, bonito y barato. Pagar bien y chao pescao"""

st.subheader(visionTetra)
st.header("Our Team")


df = pandas.read_csv('data.csv', sep=",")
#El parametro sep "," se podria omitir ya que viene es el valor por defecto de este parametro
col1, col2, col3 = st.columns(3)
with col1: 
    for indice, fila in df[:4].iterrows(): 
        st.header(f'{fila["first name"].title()} {fila["last name"].capitalize()}')
        st.text(fila["role"])
        st.image("images/" + fila["image"])


with col2: 
    for indice, fila in df[4:8].iterrows(): 
        st.header(fila["first name"].capitalize() +" "+ fila["last name"].capitalize())
        st.text(fila["role"])
        st.image("images/" + fila["image"])


with col3: 
    for indice, fila in df[8:].iterrows(): 
        st.header(fila["first name"].capitalize() +" "+ fila["last name"].capitalize())
        st.text(fila["role"])
        st.image("images/" + fila["image"])
