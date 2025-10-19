# Proyecto Gestión de Países


## Descripción del proyecto
Este proyecto permite gestionar información de países almacenada en un archivo CSV.  
Entre sus funcionalidades se incluyen:

- Agregar un nuevo país al archivo CSV.  
- Modificar la población y superficie de un país existente.  
- Buscar países por nombre o coincidencia parcial.  
- Filtrar países por continente, rango de población o rango de superficie.  
- Ordenar países por nombre, población o superficie (ascendente o descendente).  
- Mostrar estadísticas: país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente.  

El proyecto está diseñado para ser interactivo y fácil de usar desde la terminal, asegurando validaciones de entrada y control de errores.

---

## Datos de la Universidad y la Cátedra
- Universidad: Universidad Tecnologica Nacional
- Carrera: Tecnicatura Universitaria 
- Cátedra: Programacion 1
- Año: 2025  

---

## Integrantes
- Ezequiel Gonzalez 
- Joaquin del Valle
---

## Datos de los Profesores
- Profesor titular: Cinthia Rigoni  
- Tutor: Oscar Londero  

---

## Estructura del Proyecto
/raíz_del_proyecto
├─ lectura_csv.py # Función extraer_datos
├─ agregar_pais.py # Función agregar_pais
├─ modificar_pais.py # Función modificar_pais
├─ buscar_pais.py # Función buscar_pais
├─ filtrar_pais.py # Función filtrar_pais
├─ ordenar_paises.py # Función ordenar_paises
├─ mostrar_estadisticas.py # Función mostrar_estadisticas
├─ datos.csv # Archivo CSV con información de países
└─ main.py # Archivo principal que ejecuta el programa

---

## Instrucciones de Ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/JoacoDv/Programacion1-TPI.git
cd Programacion1-TPI
```

2. Asegurarse de tener Python 3 instalado.

3. Ejecutar el programa:

```bash
python main.py
```

4. Seguir las instrucciones interactivas para agregar, modificar, buscar, filtrar, ordenar o mostrar estadísticas de países

---

## Uso de Librerías de Terceros

csv (módulo estándar de Python)

os (módulo estándar de Python)

No se requiere instalación adicional, ya que todas las librerías son estándar de Python.

---

## Links

Video demostrativo: [enlace al video]

Repositorio GitHub: https://github.com/JoacoDv/Programacion1-TPI#

---

## Ejemplos de Entrada y Salida

### Ejemplo 1: Agregar un país
**Entrada:**
```text
Nombre del país: España
Población: 47351567
Superficie: 505990
Continente: Europa
```

**Salida**
```text
País 'España' agregado correctamente.
```

### Ejemplo 2: Buscar país
**Entrada**
```text
Escriba el país del cual desea saber más: es
```

**Salida**
```text
Pais: España
Habitantes: 47351567
Superficie: 505990
Continente: Europa
```

### Ejemplo 3: Filtrar por población
**Entrada**
```text
Eliga el número menor del rango: 1000000
Eliga el número mayor del rango: 50000000
```

**Salida**
```text
Los países dentro del rango ingresado son: 
Pais: España
Habitantes: 47351567
Superficie: 505990
Continente: Europa
```

### Ejemplo 4: Mostrar estadísticas
**Entrada**
```text
Escriba su elección: 2
```

**Salida**
```text
El promedio de la población de todos los países ingresados es de 24500000 habitantes
```

