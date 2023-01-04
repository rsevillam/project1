import streamlit as st 

st.set_page_config(layout="wide")
st.header("Contacto")
st.subheader("Correo electronico")
with st.form(key="emailContacto"):
    emailUsuario =st.text_input("Ingrese su correo electronico")
    info = st.text_area("Escriba su comentario o sugerencia")
    boton = st.form_submit_button("Enviar")

if boton:
    print("hola") 