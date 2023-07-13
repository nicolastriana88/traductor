from googletrans import Translator

def traducir_a_catalan(texto):
    traductor = Translator()
    deteccion_idioma = traductor.detect(texto)
    
    if deteccion_idioma.lang == 'it':
        traduccion = traductor.translate(texto, dest='ca')
        return traduccion.text
    elif deteccion_idioma.lang == 'en':
        return texto  # No se necesita traducción si está en inglés
    
    return "No se puede traducir."

# Ejemplo de uso
texto_ingles = "Hello, how are you?, ciao, come stai"
texto_italiano = "Ciao, come stai?"

print(traducir_a_catalan(texto_ingles))  # Salida: "Hello, how are you?"
print(traducir_a_catalan(texto_italiano))  # Salida: "Ciao, come stai?"
