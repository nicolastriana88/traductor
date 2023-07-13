import json
import unicodedata
from googletrans import Translator

def traducir_a_catalan(objeto_json):
    traductor = Translator()
    datos = objeto_json
    
    traducciones = {}
    for clave, valor in datos.items():
        deteccion_idioma = traductor.detect(valor)
        
        if deteccion_idioma.lang == 'it':
            traduccion = traductor.translate(valor, dest='ca')
            traduccion_texto = traduccion.text.encode('latin-1').decode('unicode-escape')
            traducciones[clave] = unicodedata.normalize('NFC', traduccion_texto)
        elif deteccion_idioma.lang == 'en':
            traducciones[clave] = valor  # No se necesita traducción si está en inglés
        else:
            traducciones[clave] = valor  # Mantener el valor original si no es italiano ni inglés
    
    resultado = json.dumps(traducciones)  # Convertir el diccionario traducido a JSON
    
    return resultado

# Ejemplo de uso
ruta_archivo = "1.json"
resultado_traduccion = ""

with open(ruta_archivo, "r") as archivo:
    while True:
        bloque = archivo.read(4096)  # Leer 4096 bytes (o el tamaño adecuado para tu caso)
        if not bloque:
            break  # Fin del archivo
        
        objeto_json = json.loads(bloque)
        resultado_traduccion += traducir_a_catalan(objeto_json)

# Guardar el resultado en un archivo de texto
with open("resultado_traduccion.txt", "w") as archivo:
    archivo.write(resultado_traduccion)

print("La traducción se ha guardado en el archivo resultado_traduccion.txt")
