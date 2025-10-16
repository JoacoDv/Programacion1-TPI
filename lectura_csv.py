import csv

# Modulo de función para extraer los datos de .csv a un diccionario:

def extraer_datos(archivo):
    
    # Array vacio destinado a almacenar cada diccionario individual el cual representa un país
    datos = []

    
    #Apertura del archivo .csv
    try:
        with open(archivo, newline='', encoding='utf-8') as csvfile:
            
            #Lectura del archivo .csv
            lector = csv.reader(csvfile)
            #Separamos el encabezado (primera fila)
            encabezado = next(lector)

            #Validamos si el formato del .csv es como lo esperamos, sino evitamos la ejecucion del archivo principal
            if [x.strip().lower() for x in encabezado] != ["nombre", "poblacion", "superficie", "continente"]:
                print("El archivo debe incluir 'nombre, poblacion, superficie, continente' en ese orden")
                return "error"

            #Iteración en las filas del archivo
            for fila in lector:
                nombre, poblacion, superficie, continente = [x.strip().lower() for x in fila]
                #Incersión de los diccionarios de datos en la matriz de datos:
                datos.append({'nombre': nombre, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente})
    #Manejamos el error
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
        return "error"
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return "error"

    return datos