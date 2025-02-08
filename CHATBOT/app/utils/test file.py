from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def validar_dni_argentino(image_path):
    count=0
    # Extraer texto de la imagen
    texto = pytesseract.image_to_string(Image.open(image_path), lang='spa')
    print(texto)
    
    # Palabras clave para validar
    palabras_clave = ["REPUBLICA ARGENTINA", "MERCOSUR", "REGISTRO NACIONAL", "MINISTERIO DEL INTERIOR","EJEMPLAR","40731267","ARGENTINA"]
    
    # Verificar si las palabras clave están en el texto
    for palabra in palabras_clave:
        if palabra in texto:
            count+=1
            print(count)
            print(palabra)
        else:
            print()
    
    if count>2:
        return "La foto subida es un DNI argentino válido."
    else:
        return "La foto subida no es un DNI argentino válido."
texAAt=validar_dni_argentino("imagen2.jpg")
print(texAAt)