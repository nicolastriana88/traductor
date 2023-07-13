import json
from googletrans import Translator

# Cargar el archivo JSON
with open('frutas.json', 'r') as f:
    data = json.load(f)

# Crear un objeto de traducción
translator = Translator()

# Traducir cada fruta en la lista
for i, fruta in enumerate(data["frutas"]):
    translation = translator.translate(data["frutas"][fruta], dest='ca')
    data["frutas"][fruta] = translation.text

# Escribir los datos traducidos en un nuevo archivo JSON
with open('archivo_traducido.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)