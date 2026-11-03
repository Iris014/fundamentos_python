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
