{
    "usuarios": []
}

import json
import os
from main import *

ARCHIVO_USUARIOS = "usuarios.json"

import json
from datos import niveles  # Ejemplo de archivo con datos del juego

def cargar_usuarios():
    with open("usuarios.json", "r") as f:
        return json.load(f)["usuarios"]

def guardar_usuarios(usuarios):
    with open("usuarios.json", "w") as f:
        json.dump({"usuarios": usuarios}, f, indent=4)

usuarios = cargar_usuarios()
usuario_actual = None

while usuario_actual is None:
    opcion = input("1. Login\n2. Registrar\nElige: ")
    if opcion == "1":
        usuario_actual = login(usuarios)
    elif opcion == "2":
        # Lógica de registrar
        pass

# Jugar
jugar(usuario_actual)

# Actualizar estadísticas
actualizar_usuario(usuarios, usuario_actual)