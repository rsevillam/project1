import streamlit as st 
from send_email import enviaCorreo
import pandas 

st.set_page_config(layout="wide")
st.header("Contacto")
st.subheader("Correo electronico")

dataframe = pandas.read_csv('topics.csv')

with st.form(key="emailContacto"):
    emailUsuario =st.text_input("Ingrese su correo electronico")
    topic = st.selectbox(
        'Seleccione Tema por el que desea contactarnos', options=dataframe)
    rawMensaje = st.text_area("Escriba su comentario o sugerencia")
    mensaje = f"""\
Subject: Nuevo correo de {emailUsuario} 

From: {emailUsuario}
Topico Seleccionado: {topic}
{rawMensaje}
"""
    boton = st.form_submit_button("Enviar")

if boton:
    enviaCorreo(mensaje)
    st.info("Su email fue enviado con éxito.")





    """Solucion de Arpit
    with st.form(key="emailContacto"):
    emailUsuario =st.text_input("Ingrese su correo electronico")
    topic = st.selectbox(
        'Seleccione Tema por el que desea contactarnos', dataframe["topic"])
    Mi solucion no seria correcta si el archivo .csv tuviera mas de 1 columna"""