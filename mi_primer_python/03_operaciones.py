# Operaciones


# Suma (+)
numero1 = 12
numero2 = 8
print(numero1 + numero2)

# AHORA TE TOCA · EJERCICIO 8 — Suma tus valores
# Crea lapices = 7 y cuadernos = 4. Muestra con print() el total de artículos.
# Comprueba: El resultado debe ser 11.
lapices = int(input("Ingresa número de lapices: "))
cuadernos = int(input("Ingresa número de cuadernos: "))
print(f"""
Lápices: {lapices}
Cuadernos: {cuadernos}
Total de artículos: {lapices + cuadernos}
""")


# Resta (-)
dinero = 5000
gasto = 1800
print(dinero - gasto)

# AHORA TE TOCA · EJERCICIO 9 — Dinero que queda
# Declara variables para presupuesto = 10000 y compra = 3750. Muestra cuánto dinero queda.
# Comprueba: El resultado debe ser 6250.
presupuesto = int(input("Ingresa dinero de presupuesto: "))
compra = int(input("Ingresa dinero de compra: "))
print(f"""
Presupuesto: {presupuesto}
Compra: {compra}
Dinero que queda: {presupuesto - compra}
""")


# Multiplicación (*)
precio = 2500
cantidad = 3
print(precio * cantidad)

# AHORA TE TOCA · EJERCICIO 10 — Costo total
# Si cada entrada cuesta 4000 y compras 5, calcula el precio total con variables y print().
# Comprueba: El resultado debe ser 20000.
precio_entrada = int(input("Ingresa precio de entrada: "))
entradas = int(input("Ingresa número de entrada"))
print(f"""
Precio de entrada: {precio_entrada}
Entradas: {entradas}
Costo total: {precio_entrada * entradas}
""")


# División (/)
total = 20
personas = 4
print(total / personas)

# AHORA TE TOCA · EJERCICIO 11 — Reparto exacto
# Reparte 48 objetos entre 6 personas usando /.
# Comprueba: El resultado debe ser 8.0.
objetos = int(input("Ingresa total de objetos:"))
personas = int(input("Ingresa total de personas:"))
print(f"""
Objetos: {objetos}
Personas: {personas}
Reparto por persona: {objetos / personas}
""")


# División entera (//)
lapices = 17
paquetes = 5
print(lapices // paquetes)

# AHORA TE TOCA · EJERCICIO 12 — Grupos completos
# Si tienes 23 estudiantes y cada equipo debe tener 4, calcula cuántos equipos completos puedes formar con //.
# Comprueba: El resultado debe ser 5.
estudiantes = int(input("Ingresa total de estudiantes: "))
por_equipo = int(input("Ingresa estudiantes por equipo: "))
print(f"""
Total de estudiantes: {estudiantes}
Estudiantes por equipo: {por_equipo}
Equipos completos que se pueden formar: {estudiantes // por_equipo}
""")


# Módulo (%)
lapices = 17
paquetes = 5
print(lapices % paquetes)

# AHORA TE TOCA · EJERCICIO 13 — Elementos sobrantes
# Con 23 estudiantes en equipos de 4, utiliza % para saber cuántos estudiantes quedan fuera de equipos completos.
# Comprueba: El resultado debe ser 3.
# Reutilizando los valores del ejercicio anterior conceptualmente
estudiantes_total = int(input("Ingresa total de estudiantes : "))
equipo = int(input("Ingresa estudiantes por equipo: "))
print(f"""
Total de estudiantes: {estudiantes_total}
Integrantes por equipo: {equipo}
Estudiantes sin equipo: {estudiantes_total % equipo}
""")


# Potencia (**)
base = 3
exponente = 2
print(base ** exponente)

# AHORA TE TOCA · EJERCICIO 14 — Cálculo de potencia
# Crea dos variables para calcular 2 elevado a 5 utilizando **.
# Comprueba: El resultado debe ser 32.
base = int(input("Ingresa número base: "))
exponente = int(input("Ingresa número exponente: "))
print(f"""
Base: {base}
Exponente: {exponente}
Resultado de {base} elevado a {exponente}: {base ** exponente}
""")


# Guardar resultados en variables
precio = 2500
cantidad = 3
total = precio * cantidad
print("Total de la compra:")
print(total)

# AHORA TE TOCA · EJERCICIO 15 — Promedio de notas
# Crea las variables nota1 = 6.0, nota2 = 5.0 y nota3 = 7.0. Calcula el promedio guardándolo en una variable y
# muéstralo con print().
# Comprueba: Debe mostrarse 6.0. Recuerda utilizar paréntesis para sumar antes de dividir.
nota1 = float("Ingresa primera nota: ")
nota2 = float("Ingresa segunda nota: ")
nota3 = float("Ingresa tercera nota: ")
# Los paréntesis son vitales aquí para sumar primero y dividir después
promedio = (nota1 + nota2 + nota3) / 3
print(f"""
Notas: {nota1}, {nota2}, {nota3}
Promedio: {promedio}
""")
# COMPROBACIÓN DE OPERADORES
# En tu archivo deben aparecer los siete operadores: +, -, *, /, //, %, **, además de un resultado almacenado en una
# variable.
