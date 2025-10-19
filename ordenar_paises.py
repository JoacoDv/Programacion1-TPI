

# Funcion para ordenar paises por distintos parametros:

def ordenar_paises(paises):

    #Brindamos las opciones para ordenar
    print("""Seleccione como quiere ordenar sus paises:
1 Por nombre
2 Por poblacion
3 Por superficie
""")

    # Tomamos la eleccion del usuario
    respuesta = input("Escriba su elección: ")

    #Creamos funcion auxiliar para mostrar paises por consola
    def mostrar_paises(paises):
        for pais in paises:
            print(f"""Nombre: {pais["nombre"]}
Poblacion: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}
""")

    # Armamos una estructura condicional en base a la eleccion del usuario

    # opcion 1 ordena por el nombre en orden alfabetico
    if respuesta == "1":
        #En todas las opciones usamos una funcion lambda para acceder al valor requerido del diccionario
        paises_ordenados = sorted(paises, key=lambda pais: pais["nombre"])
        print("\nLos paises ordenados alfabeticamente son:\n")
        mostrar_paises(paises_ordenados)


    # opcion 2 ordena por la poblacion de menor a mayor
    elif respuesta == "2":
        paises_ordenados = sorted(paises, key=lambda pais: int(pais["poblacion"]))
        print("\nLos paises ordenados De menor poblacion a mayor son: ")
        mostrar_paises(paises_ordenados)


    # opcion 3 ordena por superficie dando la posibilidad de que sea de manera ascendente o descendente utilizando un condicional anidado
    elif respuesta == "3":
        print("""
Selecciona la opcion que desea: 
1 Para ordenar de manera ascendente
2 Para ordenar de manera descendente
""")
        respuesta_superficie = input("Escriba su eleccion:")
        if respuesta_superficie == "1" :
            paises_ordenados = sorted(paises, key=lambda pais: int(pais["superficie"]))
            print("\nLos paises ordenados por superficie de manera ascendente son:")
            mostrar_paises(paises_ordenados)

        elif respuesta_superficie == "2":
            paises_ordenados = sorted(paises, key=lambda pais: int(pais["superficie"]), reverse = True)
            print("\nLos paises ordenados por superficie de manera descendente son:")
            mostrar_paises(paises_ordenados)


        else:
            print("\nLa opcion elegida no es correcta \n")

    #Manejamos la posibilidad de que el usuario elija una opcion no sugerida y llama la misma funcion de manera recursiva
    else:
            print("\nLa opcion elegida no es correcta\n")
            ordenar_paises(paises)