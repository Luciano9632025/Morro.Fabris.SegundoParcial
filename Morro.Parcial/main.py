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
    for clave in diccionario2:
        for palabra in diccionario2[clave]:
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


def mostrar_palabras_ocultas(diccionario2, categoria, letras_correctas):
    for palabra in diccionario2[categoria]:
        mostrar_palabra_oculta(palabra, letras_correctas)
        print()


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


def ingresar_palabra_oculta(palabra, palabra_oculta, letra):
    for i in range (len(palabra)):
        palabra_oculta[i] = letra

    return palabra_oculta


def submit(palabra_formada, palabras_validas, puntaje, errores):
    if palabra_formada not in palabras_validas: 
        print("La palabra no existe entre las permitidas.")
        errores += 1

    puntos = len(palabra_formada)
    print(f"✔ ¡Correcto! +{puntos} puntos.")
    puntaje += puntos

    return puntaje, errores, True



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



#COMODINES
def revelar_letra_aleatoria(palabra_oculta, palabra):
    posiciones = []
    for i in range(len(palabra)):
        if palabra_oculta[i] == "_":
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
    retornar = ""

    for letra in letras_posibles:
        if letra not in palabra and letra not in letras_usadas:
            letras_descartables.append(letra)

    if len(letras_descartables) > 0:
        retornar = random.choice(letras_descartables)

    return retornar


def iniciar_partida(diccionario, max_intentos):
    palabra = convertir_a_minuscula(seleccionar_palabra(diccionario))
    letras_correctas = []
    palabra_oculta = mostrar_palabra_oculta(palabra, letras_correctas)
    lista_palabras = obtener_lista_palabras()
    letras_desordenadas = desordenar_cadena(palabra)
    
    print(f"\nNueva partida. La palabra tiene {len(palabra)} letras.")
    print(f"Letras desordenadas: {letras_desordenadas}")
    
    return palabra, letras_correctas, palabra_oculta, lista_palabras, max_intentos


def procesar_palabra_ingresada(palabra_formada, palabra, letras_correctas, lista_palabras):
    errores = 0
    puntaje = 0
    
    if palabra_formada not in lista_palabras:
        print("La palabra no existe entre las permitidas.")
        errores = 1
    else:
        print(f"✔ ¡Correcto! +{len(palabra_formada)} puntos.")
        puntaje = len(palabra_formada)
        for letra in palabra_formada:
            if buscar_caracter_valido(letra, palabra) and letra not in letras_correctas:
                letras_correctas.append(letra)
    
    palabra_oculta = mostrar_palabra_oculta(palabra, letras_correctas)
    return palabra_oculta, letras_correctas, puntaje, errores


def verificar_partida(palabra_oculta, intentos_restantes, palabra):
    if "_" not in palabra_oculta:
        print(f"¡Ganaste la partida! La palabra era: {palabra}")
        return "ganada"
    elif intentos_restantes <= 0:
        print(f"Se acabaron los intentos. La palabra era '{palabra}'.")
        return "perdida"
    return "jugando"


def jugar_partida(puntaje, reinicios_restantes):
    palabra, letras_correctas, palabra_oculta, lista_palabras, intentos_restantes = iniciar_partida(diccionario2, max_intentos)
    errores = 0
    exito = False  # indica si la partida terminó ganada o no

    while True:
        estado = verificar_partida(palabra_oculta, intentos_restantes, palabra)

        if estado == "ganada":
            exito = True
            break
        elif estado == "perdida":
            if reinicios_restantes > 0:
                print(f"Reiniciando partida. Reinicios restantes: {reinicios_restantes - 1}")
                reinicios_restantes -= 1
                # reiniciamos la partida sin recursión
                palabra, letras_correctas, palabra_oculta, lista_palabras, intentos_restantes = iniciar_partida(diccionario2, max_intentos)
                errores = 0
                continue
            else:
                print("Sin reinicios disponibles. Partida perdida.")
                exito = False
                break

        palabra_formada = input("Ingresa una palabra formada con las letras: ")
        palabra_formada = convertir_a_minuscula(palabra_formada)

        palabra_oculta, letras_correctas, puntos_obtenidos, errores_partida = procesar_palabra_ingresada(
            palabra_formada, palabra, letras_correctas, lista_palabras
        )

        puntaje += puntos_obtenidos
        errores += errores_partida
        intentos_restantes -= errores_partida

    return puntaje, errores, exito, reinicios_restantes
        


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
puntaje = 0
reinicios_restantes = 5
#jugar_nivel(nivel, puntaje, reinicios_restantes)


def jugar_encontrar_palabra():
    i = 1
    puntaje = 0
    reinicios_restantes = 5
    while i < 2:
        jugar_nivel(i, puntaje, reinicios_restantes)
        i += 1


jugar_encontrar_palabra()



#############################

'''  
○ calcular_puntuacion_parcial(): calculará y actualizará el puntaje basado en 
aciertos y errores en una partida.  
○ verificar_estado_juego(): determinará si el jugador ganó o no la partida.  
○ calcular_puntuacion_final(): calculará y actualizará el puntaje basado en los 
puntajes parciales de cada partida. 
○ guardar_puntuacion(): guardará el nombre del jugador, junto con la 
puntuación total y la fecha, en un archivo csv. '''



