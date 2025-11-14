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
from datos import *

cantidad_niveles = 5
partidas_por_nivel = 3
max_reinicios = 3
max_intentos = 7


def obtener_lista_palabras() -> list:
    lista_palabras = []
    for clave in diccionario:
        for palabra in diccionario[clave]:
            lista_palabras.append(palabra)

    return lista_palabras


def buscar_caracter_valido(caracter, caracteres_validos):
    encontro = False
    for j in range(len(caracteres_validos)):
        if caracter == caracteres_validos[j]:
            encontro = True
            break
    
    return encontro


def convertir_a_minuscula(cadena):
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  #comprende ñ
    cadena_convertida = "" 
    for caracter in cadena:
        letra_minuscula = caracter
        if buscar_caracter_valido(caracter, mayusculas):
            letra_minuscula = chr(ord(caracter) + 32)
        cadena_convertida += letra_minuscula

    return cadena_convertida


def obtener_elemento_aleatorio(lista_elementos)->any:
    elemento = random.choice(lista_elementos)

    return elemento


def seleccionar_palabra(diccionario):
    clave = seleccionar_categoria(diccionario)
    palabra = random.choice(diccionario[clave])
    palabra = convertir_a_minuscula(palabra)
    return palabra


def seleccionar_categoria(lista_palabras):
    palabra = random.choice(list(lista_palabras))

    return palabra


def validar_longitud(cadena: str, minimo_len: int, maximo_len: int) -> bool:
    es_valida = False
    if len(cadena) >= minimo_len and len(cadena) <= maximo_len:
        es_valida = True
    return es_valida


def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo_len:int, maximo_len:int, reintentos:int)->str:
    cadena = input(mensaje)
    if type(cadena) == str:
        cadena_validada = validar_longitud(cadena,minimo_len,maximo_len)
        if cadena_validada == True:
            cadena_validada = cadena
            print("Nombre de usuario ingresado correctamente")
        else:
            print(f"{mensaje_error}, quedan {reintentos} reintentos")
            if reintentos > 0:
                cadena_validada = ingresar_nombre_usuario(mensaje, mensaje_error, minimo_len, maximo_len, reintentos - 1)

    return cadena_validada


def mostrar_palabra_oculta(palabra, letras_correctas):
    palabra_oculta = []
    for letra in palabra:
        if letra in letras_correctas:
            palabra_oculta.append(letra)
        else:
            palabra_oculta.append("_")

    for caracter in palabra_oculta:
        print(caracter, end=" ")
    print()

    return palabra_oculta


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    aciertos = 0
    fallos = 0

    for i in range (len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            aciertos += 1

    if aciertos == 0:
        fallos = 1

    return palabra_oculta, aciertos, fallos


def calcular_puntuacion_parcial(aciertos, fallos): 
    #calculará y actualizará el puntaje basado en los puntajes parciales de cada partida. 
    cantidad_puntos = (aciertos * 3) - fallos

    print(f"Puntos Obtenidos: {cantidad_puntos}")
    return cantidad_puntos


def verificar_estado_juego(diccionario_juego:dict)->bool:
    palabra = diccionario_juego["palabra"]
    letras_correctas = diccionario_juego["letras_correctas"]
    jugador_estado = True

    if all(letra in letras_correctas for letra in palabra):
        print(f"¡Ganaste! La palabra era: {palabra}")
        jugador_estado =  False
    elif diccionario_juego["intentos_restantes"] <= 0:
        print(f"Te quedaste sin intentos. La palabra era: {palabra}")
        jugador_estado = False
    
    return jugador_estado


def calcular_puntuacion_final(puntaje_final, aciertos, fallos):
    return puntaje_final + calcular_puntuacion_parcial(aciertos, fallos)


def guardar_puntuacion(nombre, puntaje_final) -> bool:
    # Ejemplo simple (puedes guardar en archivo más adelante)
    print(f"\n Puntuación de {nombre}: {puntaje_final} puntos guardada correctamente.")

    return True


def crear_usuario():
    nombre = ingresar_nombre_usuario()
    contraseña = input("Ingrese una contraseña para su usuario: ")
    print()

def buscar_usuario(nombre_usuario: str, contraseña: str) -> bool:
    print()

def ingresar_usuario(nombre_usuario: str, contraseña: str) -> bool:
    nuevo_usuario = "no"

    while nuevo_usuario == "no" or buscar_usuario(nombre_usuario, contraseña) != True:
        if buscar_usuario(nombre_usuario, contraseña) == True:
            print(f"Bienvenido {nombre_usuario} a ¡Descubre la Palabra!")
            #recuperar datos
        elif buscar_usuario(nombre_usuario, contraseña) == False:
            nuevo_usuario = input("El usuario ingresado no existe, desea crear un usuario(si/no)?")
            if nuevo_usuario == "si":
                crear_usuario()


def indicar_nivel():
    print()

def indicar_partida():
    pass

def contar_ingresos():
    print()
    #cuenta ingresos correctos e incorrectos

def desordenar_cadena(cadena: str) -> str:
    desordenada = ""
    usados = []  

    while len(usados) < len(cadena):
        indice = random.randint(0, len(cadena) - 1)
        
        if indice not in usados:      
            usados.append(indice)
            desordenada += cadena[indice]

    return desordenada




def calcular_puntaje_acumulado():
    print()

def calcular_errores_cometidos():
    pass

def calcular_cantidad_tiempo_restante():
    #se incluye???
    pass


def jugar_partida(puntaje, reinicios_restantes):
    palabra = seleccionar_palabra(diccionario)
    letras_correctas = []
    intentos_restantes = max_intentos
    errores = 0

    print(f"\nNueva partida. La palabra tiene {len(palabra)} letras.")

    palabra_oculta = mostrar_palabra_oculta(palabra, letras_correctas)

    while True:
        if intentos_restantes <= 0:
            print(f"Se acabaron los intentos. La palabra era '{palabra}'.")
            if reinicios_restantes > 0:
                print(f"Reiniciando partida. Reinicios restantes: {reinicios_restantes - 1}")
                reinicios_restantes -= 1
                return jugar_partida(puntaje, reinicios_restantes)
            else:
                print("Sin reinicios disponibles. Partida perdida.")
                return puntaje, errores, False, reinicios_restantes

        if "_" not in palabra_oculta:
            print(f"¡Ganaste la partida! La palabra era: {palabra}")
            return puntaje, errores, True, reinicios_restantes

        letra = input("Ingresa una palabra: ")
        letra = convertir_a_minuscula(letra)

        palabra_oculta, aciertos, fallos = actualizar_palabra_oculta(palabra, palabra_oculta, letra)

        if aciertos > 0 and letra not in letras_correctas:
            letras_correctas.append(letra)
            print("¡Acierto!")
        else:
            intentos_restantes -= 1
            errores += 1
            print(f"Error. Te quedan {intentos_restantes} intentos.")

        puntaje = calcular_puntuacion_final(puntaje, aciertos, fallos)
        mostrar_palabra_oculta(palabra, letras_correctas)


puntaje = 5
reinicios_restantes = 5

jugar_partida(puntaje, reinicios_restantes)


def jugar_nivel(nivel, puntaje, reinicios_restantes):
    print(f"\n=== NIVEL {nivel} ===")
    errores_nivel = 0

    for i in range(1, partidas_por_nivel + 1):
        print(f"\n--- Partida {i} del Nivel {nivel} ---")
        puntaje, errores, exito, reinicios_restantes = jugar_partida(puntaje, reinicios_restantes)
        errores_nivel += errores
        if not exito:
            print("Nivel fallado.")
            return puntaje, errores_nivel, False, reinicios_restantes

    print(f"\nResumen del Nivel {nivel}:")
    print(f"Puntaje acumulado: {puntaje}")
    print(f"Errores cometidos: {errores_nivel}")
    print(f"Reinicios restantes: {reinicios_restantes}")

    return puntaje, errores_nivel, True, reinicios_restantes


nivel = 2
jugar_nivel(nivel, puntaje, reinicios_restantes)


def jugar_encontrar_palabra():
    pass




#############################

'''  
○ calcular_puntuacion_parcial(): calculará y actualizará el puntaje basado en 
aciertos y errores en una partida.  
○ verificar_estado_juego(): determinará si el jugador ganó o no la partida.  
○ calcular_puntuacion_final(): calculará y actualizará el puntaje basado en los 
puntajes parciales de cada partida. 
○ guardar_puntuacion(): guardará el nombre del jugador, junto con la 
puntuación total y la fecha, en un archivo csv. '''


import random
from diccionario import *
from datos import *


def obtener_lista_palabras() -> list:
    lista_palabras = []
    for clave in diccionario:
        for palabra in diccionario[clave]:
            lista_palabras.append(palabra)

    return lista_palabras


def buscar_caracter_valido(caracter, caracteres_validos):
    encontro = False
    for j in range(len(caracteres_validos)):
        if caracter == caracteres_validos[j]:
            encontro = True
            break
    
    return encontro


def convertir_a_minuscula(cadena):
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"  #comprende ñ
    cadena_convertida = "" 
    for caracter in cadena:
        letra_minuscula = caracter
        if buscar_caracter_valido(caracter, mayusculas):
            letra_minuscula = chr(ord(caracter) + 32)
        cadena_convertida += letra_minuscula

    return cadena_convertida


def obtener_elemento_aleatorio(lista_elementos)->any:
    elemento = random.choice(lista_elementos)

    return elemento


def seleccionar_palabra(diccionario):
    clave = seleccionar_categoria(diccionario)
    palabra = random.choice(diccionario[clave])
    palabra = convertir_a_minuscula(palabra)
    return palabra


def seleccionar_categoria(lista_palabras):
    palabra = random.choice(list(lista_palabras))

    return palabra


def validar_longitud(cadena: str, minimo_len: int, maximo_len: int) -> bool:
    es_valida = False
    if len(cadena) >= minimo_len and len(cadena) <= maximo_len:
        es_valida = True
    return es_valida


def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo_len:int, maximo_len:int, reintentos:int)->str:
    cadena = input(mensaje)
    if type(cadena) == str:
        cadena_validada = validar_longitud(cadena,minimo_len,maximo_len)
        if cadena_validada == True:
            cadena_validada = cadena
            print("Nombre de usuario ingresado correctamente")
        else:
            print(f"{mensaje_error}, quedan {reintentos} reintentos")
            if reintentos > 0:
                cadena_validada = ingresar_nombre_usuario(mensaje, mensaje_error, minimo_len, maximo_len, reintentos - 1)

    return cadena_validada


def mostrar_palabra_oculta(palabra, letras_correctas):
    palabra_oculta = []
    for letra in palabra:
        if letra in letras_correctas:
            palabra_oculta.append(letra)
        else:
            palabra_oculta.append("_")

    for caracter in palabra_oculta:
        print(caracter, end=" ")
    print()

    return palabra_oculta


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    aciertos = 0
    fallos = 0

    for i in range (len(palabra)):
        if palabra[i] == letra:
            palabra_oculta[i] = letra
            aciertos += 1

    if aciertos == 0:
        fallos = 1

    return palabra_oculta, aciertos, fallos


def calcular_puntuacion_parcial(aciertos, fallos): 
    #calculará y actualizará el puntaje basado en los puntajes parciales de cada partida. 
    cantidad_puntos = (aciertos * 3) - fallos

    print(f"Puntos Obtenidos: {cantidad_puntos}")
    return cantidad_puntos


def verificar_estado_juego(diccionario_juego:dict)->bool:
    palabra = diccionario_juego["palabra"]
    letras_correctas = diccionario_juego["letras_correctas"]
    jugador_estado = True

    if all(letra in letras_correctas for letra in palabra):
        print(f"¡Ganaste! La palabra era: {palabra}")
        jugador_estado =  False
    elif diccionario_juego["intentos_restantes"] <= 0:
        print(f"Te quedaste sin intentos. La palabra era: {palabra}")
        jugador_estado = False
    
    return jugador_estado


def calcular_puntuacion_final(puntaje_final, aciertos, fallos):
    return puntaje_final + calcular_puntuacion_parcial(aciertos, fallos)


def guardar_puntuacion(nombre, puntaje_final) -> bool:
    # Ejemplo simple (puedes guardar en archivo más adelante)
    print(f"\n Puntuación de {nombre}: {puntaje_final} puntos guardada correctamente.")

    return True




def jugar_ahorcado()->None:
    #Arranca el juego
    #Aca creamos todas las variables temporales que necesite nuestro juego
    palabra = seleccionar_palabra(diccionario)
    letras_correctas = []
    letras_usadas = []
    intentos_restantes = 7
    puntaje = 0

    print("\n--- 🎮 BIENVENIDO AL JUEGO DEL AHORCADO ---\n")
    nombre = ingresar_nombre_usuario("Ingresa tu nombre: ", "Nombre inválido", 3, 12, 3)
    print(f"\nHola, {nombre}. ¡Adivina la palabra!")

    diccionario_juego = {
    "palabra": palabra,
    "letras_correctas": [],
    "estado": True,
    "intentos_restantes": 7
    }
    
    while verificar_estado_juego(diccionario_juego):
        #Jugamos
        #Verificamos si la partida sigue o no
        palabra_oculta = mostrar_palabra_oculta(palabra, letras_correctas)

        #convertir en funcion ingresar_letra_valida?
        letra = input("\nIngresa una letra: ")
        
        palabra_oculta, aciertos, fallos = actualizar_palabra_oculta(palabra, palabra_oculta, letra)

        if aciertos > 0 and letra not in letras_correctas:
            letras_correctas.append(letra)
            diccionario_juego["letras_correctas"] = letras_correctas
            print(f"Acierto con '{letra}'!")
        else:
            diccionario_juego["intentos_restantes"] -= 1
            print(f"Fallo. Te quedan {diccionario_juego['intentos_restantes']} intentos.")

        puntaje = calcular_puntuacion_final(puntaje, aciertos, fallos)

        if not verificar_estado_juego(diccionario_juego):
            break

    #Pido el nombre del jugador para guardar la puntuación
    #puntuacion_final
    guardar_puntuacion(nombre, puntaje)

jugar_ahorcado()

