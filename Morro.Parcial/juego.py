import random
from diccionario import *
from funciones import *
from datos import *
from usuarios import *

cantidad_niveles = 5
partidas_por_nivel = 3
max_reinicios = 3
max_intentos = 7





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

        # verificar si ganó → todas reveladas
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

    # obtener palabras del nivel
    categoria = list(diccionario2.keys())[nivel - 1]        #CAMBIAR
    palabras = diccionario2[categoria]

    exito, puntos = jugar_partida_nivel(palabras)

    puntaje += puntos

    if not exito:
        print("Nivel fallado.")

    print(f"Puntaje acumulado: {puntaje}")

    return puntaje, 0, exito, reinicios_restantes