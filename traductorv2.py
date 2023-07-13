#Importacion de librerias necesarias
import json
from googletrans import Translator

# Proceso crear casos de uso.

#Puedo crear una clase que si es ingles ignore y no traduzca y si es italino traduzca
#crear if para no traducir ingles y si italiano
#convertirlo en una clase


#cargar archivo json
with open('prueba.json', 'r') as j:
 traduccion =json.load (j)

#Traductor

translator = Translator()