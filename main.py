
import csv

# 1ro Hay que pedir al usuario el nombre del archivo con el cual vamos a trabajar

# 2do leer ese archivo

# 3ro guardar los datos en nuestro programa

# 4to vamos a imprimir por pantalla las opciones de 1) Filtrar  paises, 2) ordenar paises, 3) Mostrar estadisticas, 4) Buscar un pais. 5) Salir del programa.

# 5to volver a mostrar hasta que decida salir

def main():
    data = []
    archivo = input("Ingrese el archivo sobre paises del cual desea saber mas: ")
    with open(archivo, newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile)
        contador = 0
        for fila in spamreader:
            # print(fila)
            data.append({'nombre': fila[0], 'poblacion': int(fila[1]), 'superficie': int(fila[2]), 'continente': fila[3]})
            contador += 1

    data.pop(0)
    print(data)


    print("""Seleccion la opcion que desee.
            1 Buscar un pais
            2 Filtrar paises
            3 Ordenar paises
            4 Mostrar estadisticas
            5 Salir del programa
    """)

    respuesta = int(input())
    

    

main()