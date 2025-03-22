# Estudiantes Aprobados

Este programa en Python solicita al usuario los nombres y notas de tres estudiantes, almacena esta información en un diccionario y luego genera un archivo Excel (`ejercicio2.xlsx`) que contiene una lista de los estudiantes aprobados (aquellos con una nota de 60 o superior).

## Requisitos

* Python 3.x
* Librería `openpyxl` (puedes instalarla con `pip install openpyxl`)

## Cómo ejecutar el programa

1.  Asegúrate de tener Python 3.x instalado en tu sistema.
2.  Instala la librería `openpyxl` si aún no la tienes:

    ```bash
    pip install openpyxl
    ```

3.  Guarda el código Python en un archivo llamado `main.py`.
4.  Abre una terminal o línea de comandos y navega al directorio donde guardaste el archivo.
5.  Ejecuta el programa con el siguiente comando:

    ```bash
    python main.py
    ```

6.  El programa te pedirá que ingreses el nombre y la nota de cada estudiante (tres veces).
7.  Una vez que ingreses los datos, se generará un archivo Excel llamado `ejercicio2.xlsx` en el mismo directorio.
8.  Abre el archivo `ejercicio2.xlsx` para ver la lista de estudiantes aprobados en la columna A.

## Estructura del archivo Excel

El archivo Excel generado (`ejercicio2.xlsx`) tiene la siguiente estructura:

* **Columna A:** Contiene los nombres de los estudiantes aprobados (aquellos con una nota de 60 o superior).
* **Fila 1:** Contiene el encabezado "Aprobados (>=60)".
* **Filas 2 en adelante:** Contienen los nombres de los estudiantes aprobados.

## Posibles mejoras

* Permitir al usuario ingresar la cantidad de estudiantes.
* Permitir al usuario especificar la nota mínima para aprobar.
* Agregar más información al archivo Excel (por ejemplo, la nota de cada estudiante).
* Agregar formato al archivo Excel (por ejemplo, cambiar el tipo de letra, el color de fondo, etc.).
* Agregar una columna con todos los estudiantes y otra columna con el resultado de aprobado o reprobado.

## Autor

Marvin Garcia
