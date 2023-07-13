import json
import unicodedata
from googletrans import Translator

def traducir_a_catalan(texto):
    traductor = Translator()
    datos = json.loads(texto)  # Analizar el objeto JSON
    
    traducciones = {}
    for clave, valor in datos.items():
        deteccion_idioma = traductor.detect(valor)
        
        if deteccion_idioma.lang == 'it':
            traduccion = traductor.translate(valor, dest='ca')
            traducciones[clave] = unicodedata.normalize('NFC', traduccion.text)
        elif deteccion_idioma.lang == 'en':
            traducciones[clave] = valor  # No se necesita traducción si está en inglés
        else:
            traducciones[clave] = valor  # Mantener el valor original si no es italiano ni inglés
    
    resultado = json.dumps(traducciones)  # Convertir el diccionario traducido a JSON
    
    return resultado

# Ejemplo de uso
texto_ingles_italiano = '{"name": "John Doe", "message": "Ciao, come stai?"}'

print(traducir_a_catalan(texto_ingles_italiano))
# Salida: '{"name": "John Doe", "message": "Ell com estàs?"}'
