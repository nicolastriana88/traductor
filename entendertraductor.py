from googletrans import Translator

# Crea una instancia del traductor
translator = Translator()

# Traduce un texto de inglés a español
translation = translator.translate("Hello, how are you?", src="en", dest="es")

# Imprime el resultado
print(translation.text)  