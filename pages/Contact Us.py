import streamlit as st 
from send_email import enviaCorreo

st.set_page_config(layout="wide")
st.header("Contacto")
st.subheader("Correo electronico")

with st.form(key="emailContacto"):
    emailUsuario =st.text_input("Ingrese su correo electronico")
    topic = st.selectbox(
        'Seleccione Tema por el que desea contactarnos', 
        ('Ofertas de trabajo', 'Propuestas de Negocios', "Reclamaciones"))
    rawMensaje = st.text_area("Escriba su comentario o sugerencia")
    mensaje = f"""\
Subject: Nuevo correo de {emailUsuario} 

From: {emailUsuario}
{rawMensaje}
"""
    boton = st.form_submit_button("Enviar")

if boton:
    enviaCorreo(mensaje)
    st.info("Su email fue enviado con éxito.")