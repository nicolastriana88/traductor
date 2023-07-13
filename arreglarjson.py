import json

def corregir_json(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as f:
        contenido = f.read()
        
    try:
        json_corregido = json.loads(contenido)
    except json.JSONDecodeError as e:
        error = str(e)
        inicio_error = error.rfind('line ') + 5
        fin_error = error.rfind(' column')
        linea_error = int(error[inicio_error:fin_error])
        
        lineas = contenido.split('\n')
        lineas[linea_error-1] = lineas[linea_error-1].replace(':', ',')
        contenido_corregido = '\n'.join(lineas)
        
        try:
            json_corregido = json.loads(contenido_corregido)
        except json.JSONDecodeError as e:
            print("No se pudo corregir el archivo JSON.")
            return
    
    with open(archivo_salida, 'w') as f:
        json.dump(json_corregido, f, indent=4)
    
    print("El archivo JSON se ha corregido exitosamente.")

# Ejemplo de uso
archivo_entrada = 'archivo_danado.json'
archivo_salida = 'archivo_corregido.json'
corregir_json(archivo_entrada, archivo_salida)
