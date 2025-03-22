import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
estudiantes = {}
for i in range(3):
    nombre = input(f"Nombre del estudiante {i + 1}: ")
    nota = float(input(f"Nota de {nombre}: "))
    estudiantes[nombre] = nota

# PARTE 2: Crear archivo Excel
libro = openpyxl.Workbook()
hoja = libro.active

# PARTE 3: Escribir encabezado
hoja['A1'] = "Aprobados (>=60)"

# PARTE 4: Escribir aprobados con ciclo y condicional
fila = 2
for nombre, nota in estudiantes.items():
    if nota >= 60:
        hoja[f'A{fila}'] = nombre
        fila += 1

# PARTE 5: Guardar archivo
libro.save("ejercicio2.xlsx")
print("¡Ejercicio 2 guardado en ejercicio2.xlsx!")