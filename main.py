from lectura_csv import extraer_datos
from agregar_pais import agregar_pais
from modificar_pais import modificar_pais
from buscar_pais import buscar_pais
from filtrar_pais import filtrar_pais
from ordenar_paises import ordenar_paises
from mostrar_estadisticas import mostrar_estadisticas


# Importamos las funciones modularizadas

#Pedido del archivo .csv al usuario
archivo = input("Ingrese el archivo sobre paises del cual desea saber mas: ")
 
# Pedimos el archivo al usuario, lo leemos y extraemos los datos en un formato valido (una lista de diccionarios por cada pais) 
    
datos = extraer_datos(archivo)

# Iniciamos un bucle con nuestro porgrama

while datos != "error":
    
    # Mostramos por pantalla las opciones del usario    

    print("""Seleccion la opcion que desee.
            1 Agregar un pais
            2 Actualizar población y superficie de un pais
            3 Buscar un pais
            4 Filtrar paises
            5 Ordenar paises
            6 Mostrar estadisticas
            7 Salir del programa""")

    # Tomamos su respuesta

    respuesta = input("Eliga una opción: ")
    print("\n")

    # Realizamos una estructura condicional para cada opcion

    if respuesta == '1':
        # agregar un pais
        datos = agregar_pais(archivo, datos)

    elif respuesta == '2':
        #Modificar un pais
        datos = modificar_pais(archivo, datos)       
        
    elif respuesta == '3':
        # Busqueda de paises
        buscar_pais(datos)

    elif respuesta == '4':
        # Filtrado de paises
        filtrar_pais(datos)

    elif respuesta == '5':
        # Ordenamiento de paises
        ordenar_paises(datos)

    elif respuesta == '6':
        # EStadisticas generales
        mostrar_estadisticas(datos)

    elif respuesta == '7':
        #Salida del bucle y del programa
        break

    # En caso de elegir una opcion incorrecta, manejamos la situacion
    else:
        print("Opcion incorrecta \n")
        continue

