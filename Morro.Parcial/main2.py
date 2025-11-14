import random
import time
from diccionario import diccionario

MAXIMO_REINICIOS = 3
PARTIDAS_POR_NIVEL = 3
CANTIDAD_NIVELES = 5
SIMBOLO_OCULTO = "_"

def seleccionar_palabra(diccionario):
    clave = random.choice(list(diccionario))
    palabra = random.choice(diccionario[clave])
    return palabra

def generar_palabra_oculta(palabra, letras_reveladas):
    palabra_oculta = []
    for letra in palabra:
        if letra in letras_reveladas:
            palabra_oculta.append(letra)
        else:
            palabra_oculta.append(SIMBOLO_OCULTO)
    return palabra_oculta

def actualizar_palabra_oculta(palabra, palabra_oculta, letra_ingresada):
    cantidad_aciertos = 0
    for posicion in range(len(palabra)):
        if palabra[posicion] == letra_ingresada and palabra_oculta[posicion] != letra_ingresada:
            palabra_oculta[posicion] = letra_ingresada
            cantidad_aciertos = cantidad_aciertos + 1

    cantidad_fallos = 1 if cantidad_aciertos == 0 else 0
    return palabra_oculta, cantidad_aciertos, cantidad_fallos

def puntaje_obtenido(cantidada_ciertos, cantidadfallos):
    return cantidada_ciertos * 3 - cantidadfallos

def revelar_letra_aleatoria(palabra_oculta, palabra):
    posiciones = []
    for i in range(len(palabra)):
        if palabra_oculta[i] == SIMBOLO_OCULTO:
            posiciones.append(i)

    if len(posiciones) > 0:
        posicion = random.choice(posiciones)
        palabra_oculta[posicion] = palabra[posicion]

    return palabra_oculta

def aplicar_comodin_ubicar_letra(palabras_pendientes):
    letras_posibles = "abcdefghijklmnopqrstuvwxyz"
    letra_elegida = random.choice(letras_posibles)

    for palabra, palabra_oculta in palabras_pendientes:
        for i in range(len(palabra)):
            if palabra[i] == letra_elegida:
                palabra_oculta[i] = letra_elegida

    return letra_elegida

def descartar_letra_incorrecta(palabra, letras_usadas):
    letras_posibles = "abcdefghijklmnopqrstuvwxyz"
    letras_descartables = []

    for letra in letras_posibles:
        if letra not in palabra and letra not in letras_usadas:
            letras_descartables.append(letra)

    if len(letras_descartables) > 0:
        return random.choice(letras_descartables)

    return ""

def crear_palabra_oculta_vacia(palabra):
    palabra_oculta = []
    for letra in palabra:
        palabra_oculta.append(SIMBOLO_OCULTO)
    return palabra_oculta


def jugar_una_partida():
    palabra = seleccionar_palabra(diccionario)
    letras_reveladas = []
    palabra_oculta = generar_palabra_oculta(palabra, letras_reveladas)

    puntaje_partida = 0
    errores_partida = 0

    while True:
        print("\nPalabra:")
        print(" ".join(palabra_oculta))

        if SIMBOLO_OCULTO not in palabra_oculta:
            print("¡Palabra completa!")
            return puntaje_partida, errores_partida, palabra, None

        entrada = input("Ingrese una letra o un comodin (Raevelar=R, Ubicar=U, Descartar=D): ").strip()
        
        if len(entrada) == 1 and "a" <= entrada <= "z":
            entrada = chr(ord(entrada) - 32)

        if entrada == "R":
            palabra_oculta = revelar_letra_aleatoria(palabra_oculta, palabra)
            print("Se reveló una letra.")
            continue

        elif entrada == "U":
            print("El comodin ubicar letra se aplicará al final del nivel.")
            return puntaje_partida, errores_partida, palabra, "UBICAR"

        elif entrada == "D":
            letra_descartada = descartar_letra_incorrecta(palabra, letras_reveladas)
            if letra_descartada != "":
                print("Letra descartada:", letra_descartada)
            else:
                print("No hay letras descartables.")
                continue

        else:
            letrai = entrada
            palabra_oculta, aciertos, fallos = actualizar_palabra_oculta(
                palabra,
                palabra_oculta,
                letrai
            )
            puntaje_partida = puntaje_partida + puntaje_obtenido(aciertos, fallos)
            if aciertos == 0:
                errores_partida = errores_partida + 1
                print("Incorrecto.")
            else:
                letras_reveladas.append(letrai)
                print("Correcto.")

def jugar_un_nivel(nivel, reinicios):
    print("\n──────────────────────────")
    print("           NIVEL", nivel)
    print("──────────────────────────\n")

    tiempo_inicio = time.time()
    tiempo_maximo = 60

    puntaje_nivel = 0
    errores_nivel = 0
    activar_comodin_final = False

    palabras_pendientes = []

    for partida in range(1, PARTIDAS_POR_NIVEL + 1):
        print("\nPartida", partida)

        puntaje_partida, errores_partida, palabra, comodin = jugar_una_partida()

        palabra_oculta_vacia = crear_palabra_oculta_vacia(palabra)

        palabras_pendientes.append([palabra, palabra_oculta_vacia])

        puntaje_nivel = puntaje_nivel + puntaje_partida
        errores_nivel = errores_nivel + errores_partida

        if comodin == "UBICAR":
            activar_comodin_final = True

        if time.time() - tiempo_inicio > tiempo_maximo:
            print("\n Tiempo agotado. Nivel reiniciado.")
            reinicios = reinicios - 1
            return False, 0, 0, reinicios

    if activar_comodin_final:
        letra_aplicada = aplicar_comodin_ubicar_letra(palabras_pendientes)
        print("\n Se aplicó la letra global:", letra_aplicada)

    tiempo_restante = tiempo_maximo - int(time.time() - tiempo_inicio)
    if tiempo_restante < 0:
        tiempo_restante = 0

    print("\n RESUMEN DEL NIVEL", nivel)
    print("Puntaje:", puntaje_nivel)
    print("Errores:", errores_nivel)
    print("Tiempo restante:", tiempo_restante, "segundos")

    return True, puntaje_nivel, errores_nivel, reinicios

def jugar():
    print(" BIENVENIDO AL JUEGO DE PALABRAS")
    nombre = input("Ingrese su nombre: ")

    reinicios = MAXIMO_REINICIOS
    puntaje_total = 0
    errores_totales = 0

    nivel = 1
    while nivel <= CANTIDAD_NIVELES:
        exitoso, puntaje_nivel, errores_nivel, reinicios = jugar_un_nivel(nivel, reinicios)

        if not exitoso:
            if reinicios <= 0:
                print("\n Has perdido la partida completa. No quedan reinicios.")
                return
            print("\nSe reiniciará el nivel.\n")
        else:
            puntaje_total = puntaje_total + puntaje_nivel
            errores_totales = errores_totales + errores_nivel
            nivel = nivel + 1

    print("\n ¡HAS COMPLETADO LOS 5 NIVELES!")
    print("Jugador:", nombre)
    print("Puntaje total:", puntaje_total)
    print("Errores totales:", errores_totales)


jugar()