# Funcion para mostrar estadisticas

def mostrar_estadisticas(paises):

    #Damos las opciones al usuario para que eliga

    print("""Selecciona la opcion para ver tus estadisticas:
1 Mostrar pais con menor y mayor poblacion
2 Promedio de poblacion
3 Promedio de superficie
4 Cantidad de paises por continente""")

    #Creamos funcion auxiliar para promediar y para contar paises por continentes, ambas por bucles for

    def promedio(paises, parametro):
        promedio = 0
        for pais in paises:
            promedio += int(pais[parametro])
        return promedio // len(paises)

    def paises_por_continente(paises, parametro):
        contador = 0
        for pais in paises:
            if pais["continente"].lower() == parametro.lower():
                contador += 1
        return contador

    # Creamos estructura condicional con la respuesta del usuario

    respuesta = input("Escriba su eleccion: ")

    #Sacamos y mostramos paises con minima y maxima poblacion

    if respuesta == "1":
        minimo = min(paises, key = lambda pais: int(pais["poblacion"]))
        maximo = max(paises, key = lambda pais: int(pais["poblacion"]))

        print(f"""
Pais con pobalcion minima:
Pais: {minimo["nombre"]}
Poblacion: {minimo["poblacion"]}
Superficie: {minimo["superficie"]}
Continente: {minimo["continente"]}

Pais con pobalcion maxima:
Pais: {maximo["nombre"]}
Poblacion: {maximo["poblacion"]}
Superficie: {maximo["superficie"]}
Continente: {maximo["continente"]}

""")

    #Imprimimos el promdio de paises

    elif respuesta == "2":
        print("\nEl promedio de la poblacion de todos los paises ingresados es de ", promedio(paises, "poblacion"), "habitantes\n")

    #Imprimimos el promedio de superficie
    elif respuesta == "3":
        print("\nEl promedio de la superficie de todos los paises ingresados es de ", promedio(paises, "superficie"), "km al cuadrado\n")

    #Imprimimos la cantidad de paises totales por continente
    elif respuesta == "4":
        continentes = ["america", "europa", "africa", "asia", "oceania"]

        for continente in continentes:
            print(f"\nEl numero de paises en {continente} es de {paises_por_continente(paises, continente)}\n")

    #Manejamos la excepcion de que el usuario alla elegido otra opcion
    else:
        print("\nLa opcion elegida es incorrecta\n")
        mostrar_estadisticas(paises)
