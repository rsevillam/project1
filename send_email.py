import smtplib, ssl 

def enviaCorreo(mensaje):
    host = "smtp.gmail.com"
    port = 465 

    userName = "robertosevillaprog@gmail.com"
    password = "nehjtzxysxbrwdgv"

    reciever = "robertosevillaprog@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        """context = context es porque "context" es el nombre de un argumento 
    por defento de este metodo. En caso de no hacerlo se asigna el valor de context
    al atributo siguiente en la declaracion del metodo  """
        server.login(userName, password)
        server.sendmail(userName, reciever, mensaje)

