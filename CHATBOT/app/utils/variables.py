
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

    
