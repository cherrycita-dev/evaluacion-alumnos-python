def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

def esta_aprobado(promedio):
    if promedio >= 6.0:
        return "Aprobado" 
    else:
        return "Reprobado"

estudiantes = []
total_aprobados = 0
total_reprobados = 0

while True:
    try:
        numero_estudiantes = int(input("\nIngrese el número de estudiantes: "))
        if numero_estudiantes > 0:
            break
        print("\nEl número de estudiantes debe ser mayor a 0")
    except ValueError:
        print("\nEntrada no válida. Por favor, ingresa un número entero.")

for i in range(numero_estudiantes):
    print(f"\nEstudiante {i + 1}")
    estudiante = {}

    estudiante['nombre'] = input("Nombre: ").strip()
    calificaciones = []

    for j in range(3):
        while True:
            try:
                cal = float(input(f"Calificación {j + 1}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Ingresa un número decimal entre 0 y 10.")

    estudiante['calificaciones'] = calificaciones
    promedio = calcular_promedio(calificaciones)
    estudiante['promedio'] = promedio

    estado = esta_aprobado(promedio)
    estudiante['estado'] = estado

    if estado == "Aprobado":
        total_aprobados += 1
    else:
        total_reprobados += 1

    estudiantes.append(estudiante)

print("\n--- RESULTADOS ---")
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} - Promedio: {estudiante['promedio']:.1f} - {estudiante['estado']}")

print(f"\nTotal de estudiantes aprobados: {total_aprobados}")
print(f"Total de estudiantes reprobados: {total_reprobados}")