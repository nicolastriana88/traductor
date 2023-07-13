from googletrans import Translator

def traducir_texto(texto, origen, destino):
    traductor = Translator()
    traduccion_intermedia = traductor.translate(texto, src=origen, dest='it')
    traduccion_final = traductor.translate(traduccion_intermedia.text, src='it', dest=destino)
    return traduccion_final.text

# Texto de ejemplo
texto_ingles = "Hello, how are you?"

# Traducción de inglés a italiano
texto_italiano = traducir_texto(texto_ingles, 'en', 'it')
print("Texto en italiano:", texto_italiano)

# Traducción de italiano a catalán
texto_catalan = traducir_texto(texto_italiano, 'it', 'ca')
print("Texto en catalán:", texto_catalan)
