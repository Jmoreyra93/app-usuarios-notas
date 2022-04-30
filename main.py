"""
Proyecto Python y Mysql:
-Abrir asistente
-Login o registro
-Si elegimos registro, creará un usuario en la bbdd
-Si elegimos login, identifica al usuario y nos preguntará
-Crear nota, mostrar nota, borrarlas.

CREADO POR : JULIAN MOREYRA 29/04/2022
"""
from usuarios import acciones

print("""
Acciones disponibles:
    -registro
    -login
""")

hazEl = acciones.Acciones()
accion = input("¿Qué quieres hacer?: ")

if accion == "registro":
    hazEl.registro()

elif accion == "login":
    hazEl.login()


