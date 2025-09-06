import csv

# Modulo de función para extraer los datos de .csv a un diccionario:

def extraer_datos():
    
    # Array vacio destinado a almacenar cada diccionario individual el cual representa un país
    datos = []

    #Pedido del archivo .csv al usuario
    archivo = input("Ingrese el archivo sobre paises del cual desea saber mas: ")
    
    #Apertura del archivo .csv
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        
        #Lectura del archivo .csv
        archivo = csv.reader(csvfile)

        #Iteración en las filas del archivo
        for fila in archivo:

            #Condicional para omitir la primer fila
            if fila[1].lower() == "poblacion" or fila[1].lower() == "pobalción" or fila[2].lower() == "superficie":
                continue 

            #Incersión de los diccionarios de datos en la matriz de datos:
            datos.append({'nombre': fila[0], 'poblacion': fila[1], 'superficie': fila[2], 'continente': fila[3]})


    return datos