# Variables y tipos de datos
nombre = "Camila"
ciudad = "Santiago"
print(nombre)
print(ciudad)
print(type(nombre))

"""
crea tres variables con el nombre de una pelicula,
un videojuego y una asignatura. Muéstralas 
con print() y aplica type() a una de ellas
"""
# Texto: str (cadena de caracteres)
nombre_película = input("Ingresa nombre pelicula: ")
videojuego = input("Ingresa nombre videojuego: ")
asignatura = input("Ingresa nombre asignatura: ")
print(f"""
Pelicula: {nombre_película}
Videojuego: {videojuego}
Asignatura: {asignatura}
Tipo de datos:
{type(nombre_película)},
{type(videojuego)},
{type(asignatura)}
""")

# Número ingresado por teclado
numero = int(input("Ingresar un número: ")) #texto a número
numeroDecimal = float("Ingresar número decimal (Ej: 6.9):")

# Enteros: int
edad = 16
cantidad = 25
print(edad)
print(cantidad)
print(type(edad))

# AHORA TE TOCA · EJERCICIO 4 — Practica el tipo int
# Crea variables numéricas para tu edad, cantidad de hermanos y año actual. Muestra las tres con print() y verifica el
# tipo de una con type().
# Comprueba: Si escribes "16" entre comillas, Python lo reconoce como texto, no como número entero.
edad1 = int(input("Ingresar edad: "))
hermanos = int(input("Ingresar cantidad de hermanos: "))
anio = int(input("Ingresar año: "))
print(f"""
Edad: {edad1}
Cantidad de hermanos: {hermanos}
Tipo de dato: {type(edad1)}
""")

# Decimales: float
precio = 1599.90
altura = 1.65
print(precio)
print(altura)
print(type(altura))

# AHORA TE TOCA · EJERCICIO 5 — Practica el tipo float
# Declara variables para el precio de un producto, la temperatura y un promedio de notas. Imprime los tres valores y
# utiliza type() en dos de ellos.
# Comprueba: Todos deben contener valores numéricos escritos con punto decimal.
precio_producto = float("Ingresar precio del producto: ")
temperatura = float("Ingresar temperatura: ")
promedio_notas = float("Ingresar promedio de notas: ")
print(f"""
Precio del producto: {precio_producto}
Temperatura: {temperatura}
Promedio de notas: {promedio_notas}

Tipos de datos:
{type(precio_producto)}
{type(promedio_notas)}
""")

# Booleanos: bool
tiene_computador = True
esta_lloviendo = False
print(tiene_computador)
print(esta_lloviendo)
print(type(tiene_computador))

# AHORA TE TOCA · EJERCICIO 6 — Practica el tipo bool
# Crea tres variables booleanas para indicar si tienes Internet, si terminaste la tarea y si tienes clases mañana.
# Imprime sus valores y verifica el tipo de una.
# Comprueba: True y False no llevan comillas.
internet = True
tarea = True
clases = False
print(f"""
¿Tiene Internet?: {internet}
¿Terminó la tarea?: {tarea}
¿Tienes clases mañana?: {clases}

Tipo de dato (Internet):
{type(internet)}
""")

# Integración: ficha de producto


# AHORA TE TOCA · EJERCICIO 7 — Cuatro tipos en una ficha
# Inventa un producto de una tienda, crea cuatro variables con los tipos correspondientes e imprime los valores y el
# tipo de cada variable.
# Comprueba: Antes de continuar, asegúrate de haber utilizado str, int, float y bool dentro del mismo archivo.

