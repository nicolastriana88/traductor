from googletrans import Translator

def traducir_a_italiano(texto):
    traductor = Translator()
    deteccion_idioma = traductor.detect(texto)
    
    if deteccion_idioma.lang == 'en':
        traduccion = traductor.translate(texto, dest='it')
    elif deteccion_idioma.lang == 'it':
        traduccion = texto  # No se necesita traducción si ya está en italiano
    else:
        traduccion = None  # Si el idioma no es inglés ni italiano, no se puede traducir
    
    return traduccion if traduccion else "No se puede traducir."

# Ejemplo de uso
texto_ingles = "Hello, how are you?"
texto_italiano = "Ciao, come stai?"

print(traducir_a_italiano(texto_ingles))  # Salida: "Ciao, come stai?"
print(traducir_a_italiano(texto_italiano))  # Salida: "Ciao, come stai?"
