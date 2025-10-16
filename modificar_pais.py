import csv

def modificar_pais(archivo, paises):
    # Pedimos el nombre del país
    pais_a_modificar = input("Ingrese el nombre (o parte del nombre) del país a modificar: ").strip().lower()

    # Lista para almacenar coincidencias parciales o exactas
    coincidencias = []

    for pais in paises:
        if pais["nombre"].startswith(pais_a_modificar):
            coincidencias.append(pais)

    # Si no hay coincidencias
    if not coincidencias:
        print("No se encontró ningún país con ese nombre o iniciales.\n")
        return paises

    # Si hay varias coincidencias, mostrar opciones
    if len(coincidencias) > 1:
        print("Se encontraron varias coincidencias:")
        for i, pais in enumerate(coincidencias, start=1):
            print(f"{i}. {pais['nombre'].title()} (Población: {pais['poblacion']}, Superficie: {pais['superficie']})")

        while True:
            try:
                seleccion = int(input("Ingrese el número del país que desea modificar: "))
                if 1 <= seleccion <= len(coincidencias):
                    pais_seleccionado = coincidencias[seleccion - 1]
                    break
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Por favor ingrese un número válido.")
    else:
        pais_seleccionado = coincidencias[0]

    # Pedir nueva población y superficie con validaciones
    while True:
        nueva_poblacion = input("Ingrese la nueva población: ").strip()
        if not nueva_poblacion.replace(',', '').replace('.', '').isdigit():
            print("La población debe ser un número válido.")
            continue
        break

    while True:
        nueva_superficie = input("Ingrese la nueva superficie: ").strip()
        # Permite números con coma o punto decimal
        if not nueva_superficie.replace(',', '').replace('.', '', 1).isdigit():
            print("La superficie debe ser un número válido.")
            continue
        break

    # Modificamos la lista de diccionarios
    for pais in paises:
        if pais["nombre"] == pais_seleccionado["nombre"]:
            pais["poblacion"] = nueva_poblacion.replace(',', '').replace('.', '')
            pais["superficie"] = nueva_superficie.replace(',', '').replace('.', '')
            break

    # Sobrescribimos el archivo CSV
    try:
        with open(archivo, "w", newline="", encoding="utf-8") as csvfile:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            writer.writerows(paises)
        print(f"País '{pais_seleccionado['nombre'].title()}' modificado correctamente.\n")
    except Exception as e:
        print(f"Ocurrió un error al sobrescribir el archivo: {e}")

    return paises
