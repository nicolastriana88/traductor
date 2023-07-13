from googletrans import Translator

def traducir_a_catalan(texto):
    traductor = Translator()
    oraciones = texto.split(",")  # Separar el texto en oraciones
    
    traducciones = []
    for oracion in oraciones:
        deteccion_idioma = traductor.detect(oracion)
        
        if deteccion_idioma.lang == 'it':
            traduccion = traductor.translate(oracion, dest='ca')
            traducciones.append(traduccion.text)
        elif deteccion_idioma.lang == 'en':
            traducciones.append(oracion)  # No se necesita traducción si está en inglés
        else:
            traducciones.append(oracion)  # Mantener la oración original si no es italiano ni inglés
    
    resultado = ", ".join(traducciones)  # Unir las oraciones traducidas
    
    return resultado

# Ejemplo de uso
texto_ingles_italiano = "empty-text , Nessun dato"

print(traducir_a_catalan(texto_ingles_italiano))  
# traducion ingles sin modificar / traudccion italiano catalan
