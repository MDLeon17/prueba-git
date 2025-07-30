
peliculas = [
    {"nombre": "Avengers", "horarios": ["10:00", "14:30"], "precio": 40.00, "tickets": 100},
    {"nombre": "Batman", "horarios": ["12:00", "16:00"], "precio": 40.00, "tickets": 102},
    {"nombre": "Spiderman", "horarios": ["14:30", "19:00"], "precio": 45.75, "tickets": 75}
]

reservas = []

def mostrar_cartelera():
    print("\n--- CARTELERA ---")
    for i, pelicula in enumerate(peliculas, 1):
        print(f"\n{i}. {pelicula['nombre']}")
        print(f"   Horarios: {', '.join(pelicula['horarios'])}")
        print(f"   Precio: Q{pelicula['precio']:.2f}")
        print(f"   Tickets disponibles: {pelicula['tickets']}")

def comprar_tickets():
    mostrar_cartelera()
    try:
        opcion = int(input("\nSeleccione el número de la película: ")) - 1
        if opcion < 0 or opcion >= len(peliculas):
            print("Opción no válida.")
            return
        
        pelicula = peliculas[opcion]
        
        print("\nHorarios disponibles:")
        for i, horario in enumerate(pelicula['horarios'], 1):
            print(f"{i}. {horario}")
        
        horario_opcion = int(input("Seleccione el número del horario: ")) - 1
        if horario_opcion < 0 or horario_opcion >= len(pelicula['horarios']):
            print("Opción no válida.")
            return
        
        horario_seleccionado = pelicula['horarios'][horario_opcion]
        
    
        nombre_cliente = input("\nIngrese su nombre: ")
        
        
        cantidad = int(input("Ingrese la cantidad de tickets que desea comprar: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return
        if cantidad > pelicula['tickets']:
            print(f"No hay suficientes tickets disponibles. Solo quedan {pelicula['tickets']}.")
            return
        
    
        total = cantidad * pelicula['precio']
        
        print(f"\nResumen de compra:")
        print(f"Película: {pelicula['nombre']}")
        print(f"Horario: {horario_seleccionado}")
        print(f"Cantidad: {cantidad} tickets")
        print(f"Total a pagar: Q{total:.2f}")
        
        confirmacion = input("\n¿Confirmar compra? (s/n): ").lower()
        if confirmacion == 's':

            pelicula['tickets'] -= cantidad
            

            reserva = {
                "cliente": nombre_cliente,
                "pelicula": pelicula['nombre'],
                "horario": horario_seleccionado,
                "cantidad": cantidad,
                "total": total
            }
            reservas.append(reserva)
            
            print("\n¡Compra realizada con éxito!")
            print(f"Número de reserva: {len(reservas)}")
        else:
            print("\nCompra cancelada.")
            
    except ValueError:
        print("Por favor ingrese un valor  válido.")

def mostrar_reservas():
    print("\n--- RESERVAS ---")
    if not reservas:
        print("No hay reservas registradas.")
        return
    
    for i, reserva in enumerate(reservas, 1):
        print(f"\nReserva #{i}")
        print(f"Cliente: {reserva['cliente']}")
        print(f"Película: {reserva['pelicula']}")
        print(f"Horario: {reserva['horario']}")
        print(f"Cantidad: {reserva['cantidad']}")
        print(f"Total: Q{reserva['total']:.2f}")

def cancelar_reserva():
    mostrar_reservas()
    if not reservas:
        return
    
    try:
        num_reserva = int(input("\nIngrese el número de reserva a cancelar: ")) - 1
        if num_reserva < 0 or num_reserva >= len(reservas):
            print("Número de reserva no válido.")
            return
        
        reserva = reservas[num_reserva]
        
        for pelicula in peliculas:
            if pelicula['nombre'] == reserva['pelicula']:
                pelicula['tickets'] += reserva['cantidad']
                break
    
        del reservas[num_reserva]
        print("\nReserva cancelada exitosamente.")
        
    except ValueError:
        print("Por favor ingrese un número válido.")

def modificar_precio():
    mostrar_cartelera()
    try:
        opcion = int(input("\nSeleccione el número de la película a modificar: ")) - 1
        if opcion < 0 or opcion >= len(peliculas):
            print("Opción no válida.")
            return
        
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        if nuevo_precio <= 0:
            print("El precio debe ser mayor a cero.")
            return
        
        peliculas[opcion]['precio'] = nuevo_precio
        print("\nPrecio actualizado exitosamente.")
        
    except ValueError:
        print("Por favor ingrese un valor numérico válido.")

def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver cartelera")
        print("2. Comprar tickets")
        print("3. Ver reservas")
        print("4. Cancelar reserva")
        print("5. Modificar precio de película")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mostrar_cartelera()
        elif opcion == "2":
            comprar_tickets()
        elif opcion == "3":
            mostrar_reservas()
        elif opcion == "4":
            cancelar_reserva()
        elif opcion == "5":
            modificar_precio()
        elif opcion == "6":
            print("\nGracias por usar nuestro sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")
menu_principal()