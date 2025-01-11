
import pandas as pd

#Count es para saber donde estas.
count=0
Lista_de_socios=[]
socios_dict = []
ErrorCounter=0

class socio:
    def __init__(self,apellido,nombre,DNI,fechaNac,edad,sexo,direccion,pisodpto,localidad,provincia,codPost,Nacionalidad,telfijo,celular,mail,ocupacion):
        self.apellido = apellido
        self.nombre = nombre
        self.DNI = DNI
        self.fechaNac = fechaNac
        self.edad = edad
        self.sexo = sexo
        self.direccion = direccion
        self.pisodpto = pisodpto
        self.localidad = localidad
        self.provincia = provincia
        self.codPost = codPost
        self.Nacionalidad = Nacionalidad
        self.telfijo = telfijo
        self.celular = celular
        self.mail = mail
        self.ocupacion=ocupacion
    # Método para establecer el nombre
    # Método para establecer el apellido

    def poner_apellido(self, apellido):
        self.apellido = apellido

    # Método para establecer el nombre
    def poner_nombre(self, nombre):
        self.nombre = nombre

    # Método para establecer el DNI
    def poner_DNI(self, DNI):
        self.DNI = DNI

    # Método para establecer la fecha de nacimiento
    def poner_fechaNac(self, fechaNac):
        self.fechaNac = fechaNac

    # Método para establecer la edad
    def poner_edad(self, edad):
        self.edad = edad

    # Método para establecer el sexo
    def poner_sexo(self, sexo):
        self.sexo = sexo

    # Método para establecer la dirección
    def poner_direccion(self, direccion):
        self.direccion = direccion

    # Método para establecer el piso/departamento
    def poner_pisodpto(self, pisodpto):
        self.pisodpto = pisodpto

    # Método para establecer la localidad
    def poner_localidad(self, localidad):
        self.localidad = localidad

    # Método para establecer la provincia
    def poner_provincia(self, provincia):
        self.provincia = provincia

    # Método para establecer el código postal
    def poner_codPost(self, codPost):
        self.codPost = codPost

    # Método para establecer la nacionalidad
    def poner_Nacionalidad(self, Nacionalidad):
        self.Nacionalidad = Nacionalidad

    # Método para establecer el teléfono fijo
    def poner_telfijo(self, telfijo):
        self.telfijo = telfijo

    # Método para establecer el celular
    def poner_celular(self, celular):
        self.celular = celular

    # Método para establecer el correo electrónico
    def poner_mail(self, mail):
        self.mail = mail

    # Método para establecer la ocupación
    def poner_ocupacion(self, ocupacion):
        self.ocupacion = ocupacion

def agregar_aLista(socio_cargado):
    Napellido = socio_cargado.apellido
    Nnombre = socio_cargado.nombre
    NDNI = socio_cargado.DNI
    NfechaNac = socio_cargado.fechaNac
    Nedad = socio_cargado.edad
    Nsexo = socio_cargado.sexo
    Ndireccion = socio_cargado.direccion
    Npisodpto = socio_cargado.pisodpto
    Nlocalidad = socio_cargado.localidad
    Nprovincia = socio_cargado.provincia
    NcodPost = socio_cargado.codPost
    NNacionalidad = socio_cargado.Nacionalidad
    Ntelfijo = socio_cargado.telfijo
    Ncelular = socio_cargado.celular
    Nmail = socio_cargado.mail
    Nocupacion= socio_cargado.ocupacion
    Usuario=[Napellido,Nnombre,NDNI,NfechaNac,Nedad,Nsexo,Ndireccion,Npisodpto,Nlocalidad,Nprovincia,NcodPost,NNacionalidad,Ntelfijo,Ncelular,Nmail,Nocupacion]
    print(Usuario)
    Lista_de_socios.append(Usuario)
    print(Lista_de_socios)
    
nuevo_Socio = socio(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)


# Crear una lista de diccionarios con los atributos de los objetos

def data_socio():
     # Crear un DataFrame con los datos de los socios
     #AGREGAR FECHA 
    df_socios = pd.DataFrame(Lista_de_socios, columns=["apellido","nombre","DNI","fechaNac","edad","sexo","direccion","pisodpto","localidad","provincia","codPost","Nacionalidad","telfijo","celular","mail","ocupacion"])

    # Exportar a Excel
    df_socios.to_excel("socios.xlsx", index=False)

def Decision_func(count,message_body,ErrorCounter):

    ErrorCounterstatus=ErrorCounter
    if count==0:
        nuevo_Socio.poner_apellido(None)
        nuevo_Socio.poner_nombre(None)
        nuevo_Socio.poner_DNI(None)
        nuevo_Socio.poner_fechaNac(None)
        nuevo_Socio.poner_edad(None)
        nuevo_Socio.poner_sexo(None)
        nuevo_Socio.poner_direccion(None)
        nuevo_Socio.poner_pisodpto(None)
        nuevo_Socio.poner_localidad(None)
        nuevo_Socio.poner_provincia(None)
        nuevo_Socio.poner_codPost(None)
        nuevo_Socio.poner_Nacionalidad(None)
        nuevo_Socio.poner_telfijo(None)
        nuevo_Socio.poner_celular(None)
        nuevo_Socio.poner_mail(None)
        nuevo_Socio.poner_ocupacion(None)
        Counter=count+1
        ToSend="1) hacerme socio\n2) reservar cancha"

    elif message_body=="1" and count==1:
        ToSend=("Si en algun momento del proceso cargo algun dato erroneo , escriba VOLVER A EMPEZAR"  + "\n"
        + "\n"
        + "Introduzca Apellido"
        )
        Counter=count+1

    elif count==2:
        nuevo_Socio.poner_apellido(message_body)
        ToSend="Introduzca nombres"
        Counter=count+1
       
    elif count==3:
        nuevo_Socio.poner_nombre(message_body)
        ToSend="Introduzca Numero de Documento"
        Counter=count+1      
    
    elif count==4:
        nuevo_Socio.poner_DNI(message_body)
        ToSend="Introduzca fecha de nacimiento (DIA/MES/AÑO)"
        Counter=count+1
    
    elif count==5:
        nuevo_Socio.poner_fechaNac(message_body)
        ToSend="Introduzca edad"
        Counter=count+1

    elif count==6:
        nuevo_Socio.poner_edad(message_body)
        ToSend="Introduzca sexo (M/F/X)"
        Counter=count+1

    elif count == 7:
        nuevo_Socio.poner_sexo(message_body)
        ToSend = "Introduzca dirección"
        Counter = count + 1

    elif count == 8:
        nuevo_Socio.poner_direccion(message_body)
        ToSend = "Introduzca piso/departamento"
        Counter = count + 1

    elif count == 9:
        nuevo_Socio.poner_pisodpto(message_body)
        ToSend = "Introduzca localidad"
        Counter = count + 1

    elif count == 10:
        nuevo_Socio.poner_localidad(message_body)
        ToSend = "Introduzca provincia"
        Counter = count + 1

    elif count == 11:
        nuevo_Socio.poner_provincia(message_body)
        ToSend = "Introduzca código postal"
        Counter = count + 1

    elif count == 12:
        nuevo_Socio.poner_codPost(message_body)
        ToSend = "Introduzca nacionalidad"
        Counter = count + 1

    elif count == 13:
        nuevo_Socio.poner_Nacionalidad(message_body)
        ToSend = "Introduzca teléfono fijo"
        Counter = count + 1

    elif count == 14:
        nuevo_Socio.poner_telfijo(message_body)
        ToSend = "Introduzca celular"
        Counter = count + 1

    elif count == 15:
        nuevo_Socio.poner_celular(message_body)
        ToSend = "Introduzca correo electrónico"
        Counter = count + 1

    elif count == 16:
        nuevo_Socio.poner_mail(message_body)
        ToSend = "Introduzca ocupación"
        Counter = count + 1

    elif count == 17:
        nuevo_Socio.poner_ocupacion(message_body)
        Counter = count + 1
        ToSend = (
            "Estan sus datos correctos?\n"
            + "Apellido: " + str(nuevo_Socio.apellido) + "\n"
            + "Nombre: " + str(nuevo_Socio.nombre) + "\n"
            + "Numero de documento: " + str(nuevo_Socio.DNI) + "\n"
            + "Fecha de nacimiento: " + str(nuevo_Socio.fechaNac) + "\n"
            + "Edad: " + str(nuevo_Socio.edad) + "\n"
            + "Sexo: " + str(nuevo_Socio.sexo) + "\n"
            + "Dirección: " + str(nuevo_Socio.direccion) + "\n"
            + "Piso/Departamento: " + str(nuevo_Socio.pisodpto) + "\n"
            + "Localidad: " + str(nuevo_Socio.localidad) + "\n"
            + "Provincia: " + str(nuevo_Socio.provincia) + "\n"
            + "Código postal: " + str(nuevo_Socio.codPost) + "\n"
            + "Nacionalidad: " + str(nuevo_Socio.Nacionalidad) + "\n"
            + "Numero Teléfono fijo: " + str(nuevo_Socio.telfijo) + "\n"
            + "Numero Celular: " + str(nuevo_Socio.celular) + "\n"
            + "Correo electrónico: " + str(nuevo_Socio.mail) + "\n"
            + "Ocupación: " + str(nuevo_Socio.ocupacion) + "\n"
            + "Responda Si o No"
        )
    
    elif count==18 and message_body=="Si":
        agregar_aLista(nuevo_Socio)
        data_socio()
        ToSend="Gracias , recuerde que no tenemos natacion"
        Counter=0
        
    elif count==18 and message_body=="No":
        nuevo_Socio.poner_apellido(None)
        nuevo_Socio.poner_nombre(None)
        nuevo_Socio.poner_DNI(None)
        nuevo_Socio.poner_fechaNac(None)
        nuevo_Socio.poner_edad(None)
        nuevo_Socio.poner_sexo(None)
        nuevo_Socio.poner_direccion(None)
        nuevo_Socio.poner_pisodpto(None)
        nuevo_Socio.poner_localidad(None)
        nuevo_Socio.poner_provincia(None)
        nuevo_Socio.poner_codPost(None)
        nuevo_Socio.poner_Nacionalidad(None)
        nuevo_Socio.poner_telfijo(None)
        nuevo_Socio.poner_celular(None)
        nuevo_Socio.poner_mail(None)
        nuevo_Socio.poner_ocupacion(None)
        ToSend="Por favor vuelva a introducir Apellido"
        Counter=2

    elif count==18 and (message_body!="No" and message_body!="Si"):
        if ErrorCounter==3:
            nuevo_Socio.poner_nombre(None)
            nuevo_Socio.Poner_documento(None)
            ToSend="Comenzaremos de nuevo\n1) hacerme socio\n2) reservar cancha"
            Counter=0
            ErrorCounterstatus=0
        else:
            ToSend = (
            "Estan sus datos correctos?\n"
            + "Apellido: " + str(nuevo_Socio.apellido) + "\n"
            + "Nombre: " + str(nuevo_Socio.nombre) + "\n"
            + "Documento (DNI): " + str(nuevo_Socio.DNI) + "\n"
            + "Fecha de nacimiento: " + str(nuevo_Socio.fechaNac) + "\n"
            + "Edad: " + str(nuevo_Socio.edad) + "\n"
            + "Sexo: " + str(nuevo_Socio.sexo) + "\n"
            + "Dirección: " + str(nuevo_Socio.direccion) + "\n"
            + "Piso/Departamento: " + str(nuevo_Socio.pisodpto) + "\n"
            + "Localidad: " + str(nuevo_Socio.localidad) + "\n"
            + "Provincia: " + str(nuevo_Socio.provincia) + "\n"
            + "Código postal: " + str(nuevo_Socio.codPost) + "\n"
            + "Nacionalidad: " + str(nuevo_Socio.Nacionalidad) + "\n"
            + "Teléfono fijo: " + str(nuevo_Socio.telfijo) + "\n"
            + "Celular: " + str(nuevo_Socio.celular) + "\n"
            + "Correo electrónico: " + str(nuevo_Socio.mail) + "\n"
            + "Ocupación: " + str(nuevo_Socio.ocupacion) + "\n"
            +"\n"
            + "Responda Si o No"
        )
            Counter=count
            ErrorCounterstatus= ErrorCounter+1
            #print(ErrorCounterstatus)
            
    elif message_body=="2" and count==1:
        ToSend="Esto no esta disponbile hasta tener natacion"

    else:
        ToSend="Ocurrio un error en el sistema , volveremos a empezar"
        Counter=0
        ErrorCounterstatus=0
    return ToSend,Counter,ErrorCounterstatus

#ERROR=0
#cONTADOR=0
#
#nuevo_Socio_Test = socio(
#    apellido="Pérez",
#    nombre="Juan",
#    DNI="12345678",
#    fechaNac="01/01/1990",
#    edad=33,
#    sexo="Masculino",
#    direccion="Calle Falsa 123",
#    pisodpto="1B",
#    localidad="Buenos Aires",
#    provincia="Buenos Aires",
#    codPost="1000",
#    Nacionalidad="Argentina",
#    telfijo="011-12345678",
#    celular="11-987654321",
#    mail="juan.perez@example.com",
#    ocupacion="Ingeniero"
#)
#
#
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,1,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,"1",ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.apellido,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.nombre,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.DNI,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.fechaNac,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.edad,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.sexo,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.direccion,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.pisodpto,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.localidad,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.provincia,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.codPost,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.Nacionalidad,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.telfijo,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.celular,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.mail,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,nuevo_Socio_Test.ocupacion,ERROR)
#SEND,cONTADOR,ERROR=Decision_func(cONTADOR,"Si",ERROR)
#
#
#
#print(f"Apellido: {nuevo_Socio.apellido}")
#print(f"Nombre: {nuevo_Socio.nombre}")
#print(f"DNI: {nuevo_Socio.DNI}")
#print(f"Fecha de Nacimiento: {nuevo_Socio.fechaNac}")
#print(f"Edad: {nuevo_Socio.edad}")
#print(f"Sexo: {nuevo_Socio.sexo}")
#print(f"Dirección: {nuevo_Socio.direccion}")
#print(f"Piso/Departamento: {nuevo_Socio.pisodpto}")
#print(f"Localidad: {nuevo_Socio.localidad}")
#print(f"Provincia: {nuevo_Socio.provincia}")
#print(f"Código Postal: {nuevo_Socio.codPost}")
#print(f"Nacionalidad: {nuevo_Socio.Nacionalidad}")
#print(f"Teléfono Fijo: {nuevo_Socio.telfijo}")
#print(f"Celular: {nuevo_Socio.celular}")
#print(f"Correo Electrónico: {nuevo_Socio.mail}")
#print(f"Ocupación: {nuevo_Socio.ocupacion}")
#