from googletrans import Translator

def traducir_a_catalan(texto):
    traductor = Translator()
    deteccion_idioma = traductor.detect(texto)
    
    if deteccion_idioma.lang == 'it':
        traduccion = traductor.translate(texto, dest='ca')
    elif deteccion_idioma.lang == 'en':
        traduccion = texto  # No se necesita traducción si esta en ingles
    else:
        return "No se puede traducir."

# Ejemplo de uso
texto_ingles = "Hello how are you?"
texto_italiano = "Ciao, come stai?"

print(traducir_a_catalan(texto_ingles))  # Salida: "Ciao, come stai?"
print(traducir_a_catalan(texto_italiano))  # Salida: "Ciao, come stai?"
