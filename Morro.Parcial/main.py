'''Objetivo general:
Desarrollar un juego de descubrir las palabras, primero en consola y luego en entorno gráfico (Pygame), que permita poner en práctica 
estructuras de datos complejas, archivos externos, modularidad, programación funcional y diseño accesible orientado a distintas 
neurodivergencias.
Enunciado del juego

El objetivo del juego es formar todas las palabras posibles en un tiempo determinado a partir de seis letras desordenadas. Cada palabra 
formada sumará puntos, según la cantidad de letras (las palabras de 6 letras valen 6 puntos, por ejemplo, y así sucesivamente). Contará 
con 3 botones:
Shuffle: modifica el orden de las letras
Clear: borra las letras seleccionadas por el jugador
Submit: ingresa la palabra seleccionada por el jugador.


🧩 Dinámica del juego
Inicio de sesión:
Al comenzar, el jugador debe ingresar su nombre de usuario y contraseña.
Si el usuario ya existe, se recuperan sus datos (estadísticas, partidas guardadas, preferencias de accesibilidad, etc.).
Si no existe, se le ofrecerá la opción de crear un nuevo usuario.


🎮 Desarrollo del juego
El juego está compuesto por 5 niveles, y cada nivel contiene 3 partidas.
Durante cada nivel:
Se indica al jugador en qué nivel se encuentra.
Se llevará cuenta de cada ingreso incorrecto, no habra otra consecuencia por un ingreso incorrecto.
Si el jugador se queda sin tiempo, el nivel se reinicia.
El jugador dispone de un máximo de 3 reinicios durante todo el juego; si los agota, pierde la partida completa.


Al finalizar un nivel, se mostrará un resumen del progreso, incluyendo:
Puntaje acumulado
Cantidad de errores cometidos
Cantidad de tiempo restante


💡 Comodines
Durante la partida, el jugador dispone de 3 comodines de uso único, que podrá activar en cualquier momento:
🔍 Revelar palabra: Mestra parcialmente una de las palabras a descubrir.

🔗 Ubicar letra: Selecciona una letra aleatoriamente y la ubicará en todas las palabras restantes.

🧠 Comodín extra (A definir por el equipo).


🏆 Final del juego
Si el jugador logra completar los 5 niveles, el juego mostrará un mensaje de victoria junto con sus estadísticas finales (puntaje total, errores, tiempo, etc.). En caso contrario, informar la derrota y finalizar el juego.
'''

import random
from diccionario import *
from funciones import *
from datos import *
from usuarios import *






'''def jugar_partida(puntaje, reinicios_restantes, palabras):
    palabra, letras_correctas, palabra_oculta, lista_palabras, intentos_restantes, categoria = iniciar_partida(diccionario2, max_intentos)
    errores = 0
    exito = False  

    while True:
        estado = verificar_partida(palabra_oculta, intentos_restantes, palabra)

        if estado == "ganada":
            exito = True
            break

        elif estado == "perdida":
            if reinicios_restantes > 0:
                print(f"Reiniciando partida. Reinicios restantes: {reinicios_restantes - 1}")
                reinicios_restantes -= 1
                palabra, letras_correctas, palabra_oculta, lista_palabras, intentos_restantes, categoria = iniciar_partida(diccionario2, max_intentos)
                continue
            else:
                print("Sin reinicios disponibles.")
                exito = False
                break

        letra = input("Ingrese UNA letra (o 'comodin'): ")
        letra = convertir_a_minuscula(letra)

        if len(letra) != 1:
            print("Debe ingresar solo UNA letra.")
            continue

        aciertos, fallos = procesar_letra_ingresada(letra, palabra, letras_correctas)

        # actualizar palabra oculta solo para esta palabra
        palabra_oculta, _, _ = actualizar_palabra_oculta(palabra, palabra_oculta, letra)

        intentos_restantes -= fallos
        puntaje += aciertos * 2  # ejemplo

        mostrar_palabra_oculta(palabra, letras_correctas)
        print(f"Intentos restantes: {intentos_restantes}")

    return puntaje, errores, exito, reinicios_restantes'''
        
def login(usuarios):
    nombre = input("Usuario: ")
    contra = input("Contraseña: ")

    indice = buscar_usuario(usuarios, nombre)
    if indice != -1:
        if usuarios[indice]["contraseña"] == contra:
            print("Login exitoso")
            return usuarios[indice]
        else:
            print("Contraseña incorrecta")
            return None
    else:
        print("Usuario no encontrado")
        return None


def jugar_partida_nivel(palabras):
    palabras_ocultas = ["_" * len(p) for p in palabras]
    intentos = 7
    puntaje = 0

    print("Debes adivinar TODAS las palabras del nivel.")
    mostrar_todas(palabras_ocultas)

    while intentos > 0:
        palabra_ingresada = input("Ingresa una palabra: ")
        palabra_ingresada = convertir_a_minuscula(palabra_ingresada)

        palabras_ocultas, puntos, errores = procesar_palabra_ingresada(
            palabra_ingresada,
            palabras,
            palabras_ocultas
        )

        puntaje += puntos
        intentos -= errores

        mostrar_todas(palabras_ocultas)

        todas = True
        for i in range(len(palabras)):
            if palabras_ocultas[i] != palabras[i]:
                todas = False
                break

        if todas:
            print("🎉 ¡Ganaste el nivel! Adivinaste todas las palabras.")
            return True, puntaje

    print("💀 Te quedaste sin intentos.")
    return False, puntaje



def jugar_nivel(nivel, puntaje, reinicios_restantes):
    print(f"\n=== NIVEL {nivel} ===")

    categoria = list(diccionario2.keys())[nivel - 1]        #CAMBIAR
    palabras = diccionario2[categoria]

    exito, puntos = jugar_partida_nivel(palabras)

    puntaje += puntos

    if not exito:
        print("Nivel fallado.")

    print(f"Puntaje acumulado: {puntaje}")

    return puntaje, 0, exito, reinicios_restantes


nivel = 2
puntaje = 0
reinicios_restantes = 5


def jugar_encontrar_palabra():
    i = 1
    puntaje = 0
    reinicios_restantes = 5
    while i < 2:
        jugar_nivel(i, puntaje, reinicios_restantes)
        i += 1


def main():
    usuarios = cargar_usuarios()

    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar sesión")
    print("2. Registrarse")
    opcion = input("Elige una opción: ")

    usuario = None

    if opcion == "1":
        usuario = login(usuarios)
        if usuario is None:
            return
    elif opcion == "2":
        nombre = input("Nuevo usuario: ")
        contraseña = input("Contraseña: ")
        if registrar_usuario(usuarios, nombre, contraseña):
            print("Usuario registrado correctamente. Inicia sesión ahora.")
            return
        else:
            print("Ese usuario ya existe.")
            return
    else:
        print("Opción inválida")
        return

    print(f"\nBienvenido, {usuario['nombre']}!")
    print("Iniciando partida...\n")

    jugar_encontrar_palabra()  


main()



