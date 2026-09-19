def procesar_datos_elvis():
    """
    Función que almacena los datos académicos de Gracia Moreira Elvis Sebastián
    en un diccionario, calcula su promedio general y retorna el reporte.
    """

    # 1. Definimos los datos del estudiante usando un diccionario
    # Las materias y calificaciones se guardan en una lista de diccionarios
    estudiante = {
        "apellidos": "Gracia Moreira",
        "nombres": "Elvis Sebastián",
        "matricula": "2026-001",
        "calificaciones": [
            {"materia": "Fundamentos de Python", "nota": 9.5},
            {"materia": "Estadística Aplicada", "nota": 8.8},
            {"materia": "Bases de Datos", "nota": 9.2}
        ]
    }

    # 2. Extraemos las notas usando una comprensión de lista
    notas = [registro["nota"] for registro in estudiante["calificaciones"]]

    # 3. Calculamos el promedio
    # Protegemos contra división por cero por si la lista de notas estuviera vacía
    if len(notas) > 0:
        promedio = sum(notas) / len(notas)
    else:
        promedio = 0.0

    # 4. Agregamos el promedio calculado al diccionario del estudiante
    estudiante["promedio_general"] = round(promedio, 2)

    # 5. Generamos un reporte de salida
    print(f"--- Reporte Académico ---")
    print(f"Estudiante: {estudiante['apellidos']} {estudiante['nombres']}")
    print(f"Matrícula: {estudiante['matricula']}")
    print("Desglose de calificaciones:")

    for registro in estudiante["calificaciones"]:
        print(f" - {registro['materia']}: {registro['nota']}")

    print(f"-------------------------")
    print(f"PROMEDIO GENERAL: {estudiante['promedio_general']}")

    # Retornamos el diccionario completo por si se necesita en otro sistema
    return estudiante

# Llamamos a la función para probarla
datos_procesados = procesar_datos_elvis()