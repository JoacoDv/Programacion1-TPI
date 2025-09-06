#Funcion de busqueda de pais por concidencia parcial o exacta:

def buscar_pais(paises):

    #Pedimos al usuario que ingrese el pais que quiere buscar
    pais_a_buscar = input("Escriba el pais del cual desea saber mas: ")

    #Inicializamos un array vacio donde iran los paises que contengan las mismas letrar que lo que ingreso el usuario
    paises_similares = []

    #Hacemos un bucle para iterar por el array de diccionarios con los paises
    for pais in paises:

        #Evaluamos si el sclicing del pais iterado es igual al pais ingresado por el usuario
        if pais["nombre"][0: len(pais_a_buscar)].lower() == pais_a_buscar.lower() :

            #Añadimos el pais que coincide a la lista de paises similares
            paises_similares.append(pais)

        # si evalua a false saltamos de iteracion
        else:
            continue

    #Evaluamos si hay paises similares
    if not paises_similares:

        #Avisamos al usario que no hubo ccoincidencia
        print("No se encontro ningun pais con esas iniciales.")
    
    #Al haber coincidencia mostramos los paises por pantalla con un bucle
    else:
        for pais in paises_similares:
            print(f""" Pais: {pais["nombre"]}
Habitantes: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}            
            """)