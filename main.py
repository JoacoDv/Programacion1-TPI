from lectura_csv import extraer_datos
from buscar_pais import buscar_pais

# 1ro Hay que pedir al usuario el nombre del archivo con el cual vamos a trabajar

# 2do leer ese archivo

# 3ro guardar los datos en nuestro programa

# 4to vamos a imprimir por pantalla las opciones de 1) Filtrar  paises, 2) ordenar paises, 3) Mostrar estadisticas, 4) Buscar un pais. 5) Salir del programa.

# 5to volver a mostrar hasta que decida salir


    
#Asignacion del resultado de la extracción de datos en la variable datos

datos = extraer_datos()


print("""Seleccion la opcion que desee.
         1 Buscar un pais
         2 Filtrar paises
         3 Ordenar paises
         4 Mostrar estadisticas
         5 Salir del programa
""")

respuesta = int(input())
    
if respuesta == 1:
    buscar_pais(datos)
    

