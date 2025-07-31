
# CineFácil

CineFácil es un sistema básico desarrollado en Python que permite visualizar la cartelera de un cine de forma clara y ordenada. Está pensado como una herramienta sencilla para practicar el manejo de diccionarios, ciclos `for` y salida de información por consola.

---

## Descripción del sistema

El programa muestra una lista de películas disponibles, junto con información importante como:

- Título de la película
- Horarios de proyección
- Precio por entrada
- Cantidad de boletos disponibles

Está diseñado para funcionar desde consola y puede ser fácilmente ampliado con nuevas funcionalidades.

---

## Funciones del programa

1. **Mostrar la cartelera completa:**
   - Recorre el diccionario de películas e imprime toda la información disponible para cada una.

2. **Manejo de datos estructurados:**
   - Cada película se representa como una entrada del diccionario con subcampos: horarios, precio y cantidad de boletos.

3. **Código claro y fácil de modificar:**
   - Es posible agregar nuevas películas, cambiar horarios, modificar precios o actualizar el número de boletos de manera sencilla.

---

## Ejemplo de salida del programa

```
Película: Avengers: Endgame
  Horarios: 10:00, 14:30, 19:00, 22:15
  Precio: $12.50
  Tickets disponibles: 100
----------------------------------------
Película: The Batman
  Horarios: 11:45, 15:20, 18:30, 21:45
  Precio: $10.75
  Tickets disponibles: 80
----------------------------------------
```

---

## Posibles mejoras futuras

- Permitir que el usuario seleccione una película y compre boletos.
- Descontar boletos disponibles tras cada compra.
- Almacenar y leer datos desde archivos externos (JSON, CSV).
- Crear una interfaz gráfica simple o integración web.

---

## Requisitos para ejecutar

- Python 3.x instalado
- Editor de texto o entorno de desarrollo (por ejemplo, VS Code, PyCharm o IDLE)
