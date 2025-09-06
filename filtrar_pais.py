#Funcion para filtrar paises:  
 
def filtrar_pais(paises):

    #Imprimimos por pantalla las opciones disponibles
    print("""1 para filtrar por continente
2 para filtrar por rango de población
3 para filtrar por rango de superficie""")

    #Almacenamos la respuesta del usuario para posteriormente usarla como condicional
    respuesta = int(input("Eliga su opción: "))

    #Inicializamos un array vacio para guardar los paises filtrados
    paises_filtrados = []

    #Evaluamos que opción eligio el usuario


    if respuesta == 1:

        #En filtro por continente pedimos el continente
        continente = input("Escriba el continente deseado: ")

        #Hacemos un bucle donde verificamos que pais coinciden con el contiente
        for pais in paises:
            if pais["continente"].lower() == continente.lower():
                paises_filtrados.append(pais)
        print(f"El resultado de los paises con el continente {continente} es:\n")
        

        #Imprimimos resultados tanto si los hubiese como si no.
        if not paises_filtrados:
            print("No hubo resultados para ese continente\n")
        else:
            for pais in paises_filtrados:
                print(f"""Pais: {pais["nombre"]}
Habitantes: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}            
                \n""")


    elif respuesta == 2:

        #En filtro por rango de población pedimos el minimo y maximo
        rango1 = int(input("Eliga el numero menor del rango: "))
        rango2 = int(input("Eliga el numero mayor del rango: "))

        #Utilizamos el mismo procedimiento de iterar los paises
        for pais in paises:

            #Evaluamos que paises estan dentro del rango
            if int(pais["poblacion"]) >= rango1 and int(pais["poblacion"]) <= rango2:
                paises_filtrados.append(pais)
        print("Los paises dentro del rango ingresado son: \n")

        #Imprimimos los resultados
        if not paises_filtrados:
            print("No hubo resultados para ese continente\n")
        else:
            for pais in paises_filtrados:
                print(f"""Pais: {pais["nombre"]}
Habitantes: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}            
                \n""")

    elif respuesta == 3:

        #En la opción de rango de superficie tambien pedimos rango minimo y maximo
        rango1 = int(input("Eliga el numero menor del rango: "))
        rango2 = int(input("Eliga el numero mayor del rango: "))

        #Utilizamos misma iteración
        for pais in paises:

            #Evaluamos que el pais este dentro del rango de superficie
            if int(pais["superficie"]) >= rango1 and int(pais["superficie"]) <= rango2:
                paises_filtrados.append(pais)

        #Imprimimos resultados
        print("Los paises dentro del rango ingresado son: \n")
        if not paises_filtrados:
            print("No hubo resultados para ese rango de superficie\n")
        else:
            for pais in paises_filtrados:
                print(f"""Pais: {pais["nombre"]}
Habitantes: {pais["poblacion"]}
Superficie: {pais["superficie"]}
Continente: {pais["continente"]}            
                \n""")

    #En caso de opción incorrecta manejamos el caso con uso de recursividad.
    else:
        print("Por favor eliga una opción correcta\n")
        filtrar_pais(paises)