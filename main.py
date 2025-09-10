from lectura_csv import extraer_datos
from buscar_pais import buscar_pais
from filtrar_pais import filtrar_pais
from ordenar_paises import ordenar_paises
from mostrar_estadisticas import mostrar_estadisticas


# Importamos las funciones modularizadas
 
# Pedimos el archivo al usuario, lo leemos y extraemos los datos en un formato valido (una lista de diccionarios por cada pais) 
    
datos = extraer_datos()

# Iniciamos un bucle con nuestro porgrama

while True:
    
    # Mostramos por pantalla las opciones del usario    

    print("""Seleccion la opcion que desee.
            1 Buscar un pais
            2 Filtrar paises
            3 Ordenar paises
            4 Mostrar estadisticas
            5 Salir del programa""")

    # Tomamos su respuesta

    respuesta = int(input("Eliga una opción: "))

    # Realizamos una estructura condicional para cada opcion

        
    if respuesta == 1:
        # Busqueda de paises
        buscar_pais(datos)

    elif respuesta == 2:
        # Filtrado de paises
        filtrar_pais(datos)

    elif respuesta == 3:
        # Ordenamiento de paises
        ordenar_paises(datos)

    elif respuesta == 4:
        # EStadisticas generales
        mostrar_estadisticas(datos)

    elif respuesta == 5:
        #Salida del bucle y del programa
        break

    # En caso de elegir una opcion incorrecta, manejamos la situacion
    else:
        print("Opcion incorrecta \n")
        continue

