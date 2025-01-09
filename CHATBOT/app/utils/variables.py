
import pandas as pd

#Count es para saber donde estas.
count=0
Lista_de_socios=[]
socios_dict = []
ErrorCounter=0

class socio:
    def __init__(self,nombre,documento):
        self.nombre = nombre
        self.documento = documento
        # Método para establecer el nombre
    def poner_nombre(self, nombre):
        self.nombre = nombre
        #print(f"Nombre establecido: {self.nombre}")
    # Método para establecer la edad
    def Poner_documento(self, documento):
        self.documento = documento
        #print(f"Edad establecida: {self.edad}")

def agregar_aLista(socio_cargado):
    Name=socio_cargado.nombre
    Document=socio_cargado.documento
    Usuario=[Name,Document]
    print(Usuario)
    Lista_de_socios.append(Usuario)
    print(Lista_de_socios)
    
nuevo_Socio=socio(None,None)


# Crear una lista de diccionarios con los atributos de los objetos

def data_socio():
     # Crear un DataFrame con los datos de los socios
    df_socios = pd.DataFrame(Lista_de_socios, columns=['Nombre', 'Documento'])

    # Exportar a Excel
    df_socios.to_excel("socios.xlsx", index=False)

def Decision_func(Count,message_body):    
    if count==0:
        nuevo_Socio.poner_nombre(None)
        nuevo_Socio.Poner_documento(None)
        Counter=1
        ToSend="1) hacerme socio\n2) reservar cancha"

    elif message_body=="1" and count==1:
        ToSend="Introduzca nombre y apellido"
        Counter=2
        
    elif count==2:
        nuevo_Socio.poner_nombre(message_body)
        ToSend="Introduzca Documento"
        Counter=3

    elif count==3:
        nuevo_Socio.Poner_documento(message_body)
        Counter=4
        ToSend="Estan sus datos correctos?"+"\nNombre y apellido : "+ str(nuevo_Socio.nombre) + "\nDocumento : " + str(nuevo_Socio.documento) + "\nResponda Si o No"
        
    elif count==4 and message_body=="Si":
        agregar_aLista(nuevo_Socio)
        data_socio()
        ToSend="Gracias , recuerde que no tenemos natacion"
        Counter=0
        
    elif count==4 and message_body=="No":
        nuevo_Socio.poner_nombre(None)
        nuevo_Socio.Poner_documento(None)
        ToSend="Por favor vuelva a introducir su nombre y apellido"
        Counter=4

    elif count==4 and (message_body!="No" and message_body!="Si"):
        if ErrorCounter==3:
            nuevo_Socio.poner_nombre(None)
            nuevo_Socio.Poner_documento(None)
            ToSend="Comenzaremos de nuevo"
        else:
            ToSend="Estan sus datos correctos?"+"\nNombre y apellido : "+ str(nuevo_Socio.nombre) + "\nDocumento : " + str(nuevo_Socio.documento) + "\nResponda Si o No"
            Counter=3
            

    elif message_body=="2":
        ToSend="Diga horario que desa reservar"
    
    else:
        nuevo_Socio.poner_nombre(None)
        nuevo_Socio.Poner_documento(None)
        ToSend="1) hacerme socio\n2) reservar cancha"
    
    return ToSend,Counter


