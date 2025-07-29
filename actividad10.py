#Ejercicio #1
colores = ["rojo", "azul", "amarillo"]
try:
    ver_color = int(input("Ingrese el numero del color que desea ver: "))
    n = ver_color-1
    colores[n]
except IndexError:
    print("el valor no existe en la lista mencioanada")
else:
    print(colores[n])
finally:
    print("gracias por usar el programa")

#Ejercicio #2
try:
    numero = int(input("ingrese un numero entero: "))
except ValueError:
    print("Tiene que ingresar un numero entero para seguir: ")
else:
    print(numero*3)

#ejercicio 3

frutas = ["manzana", "pera", "banano"]
try: 
    eliminar_fruta = int(input("ingrese el numero de fruta que desea eliminar: "))
    n = eliminar_fruta - 1
    fruta_eliminada = frutas.pop(n)
except IndexError:
    print("El valor no existe en la lista mencionada")
else:
    print(f"Fruta eliminada: {fruta_eliminada}")
finally:
    print(f"Lista actualizada: {frutas}")

#ejercicio 4 

peliculas = {
    "matrix": 1999,
    "spiderman 2" : 2004,
    "interestelar": 2014
}
try:
    nombre_pelicula = input("ingrese el nombre de la pelicula que desea buscar ") 
    print(f"{nombre_pelicula} se estrenó en {peliculas[nombre_pelicula]}")
except KeyError:
     print("La película no está en la lista")