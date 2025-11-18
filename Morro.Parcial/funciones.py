import random
from diccionario import *
 
def obtener_lista_palabras() -> list:
    lista_palabras = []
    claves = list(diccionario2.keys())

    for i in range(len(claves)):
        clave = claves[i]
        palabras = diccionario2[clave]
        for j in range(len(palabras)):
            lista_palabras.append(palabras[j])

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
    for i in range(len(cadena)):
        caracter = cadena[i]
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

    for i in range(len(palabra)):
        letra = palabra[i]

        # --- reemplazo del "in" ---
        esta = False
        for j in range(len(letras_correctas)):
            if letras_correctas[j] == letra:
                esta = True
                break
        # ---------------------------

        if esta:
            palabra_oculta.append(letra)
        else:
            palabra_oculta.append("_")

    for i in range(len(palabra_oculta)):
        print(palabra_oculta[i], end=" ")
    print()

    return palabra_oculta


def mostrar_palabras_ocultas(diccionario2, categoria, letras_correctas):
    palabras = diccionario2[categoria]
    for i in range(len(palabras)):
        palabra = palabras[i]
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



def calcular_puntuacion_parcial(aciertos, fallos): 
    #calculará y actualizará el puntaje basado en los puntajes parciales de cada partida. 
    cantidad_puntos = aciertos - fallos

    print(f"Puntos Obtenidos: {cantidad_puntos}")
    return cantidad_puntos


def verificar_estado_juego(diccionario_juego:dict)->bool:
    palabra = diccionario_juego["palabra"]
    letras_correctas = diccionario_juego["letras_correctas"]
    jugador_estado = True

    todas = True
    for i in range(len(palabra)):
        letra = palabra[i]

        # verificar si letra está en letras_correctas
        esta = False
        for j in range(len(letras_correctas)):
            if letras_correctas[j] == letra:
                esta = True
                break

        if not esta:
            todas = False
            break

    if todas:
        print(f"¡Ganaste! La palabra era: {palabra}")
        jugador_estado = False
    elif diccionario_juego["intentos_restantes"] <= 0:
        print(f"Te quedaste sin intentos. La palabra era: {palabra}")
        jugador_estado = False
    
    return jugador_estado


def calcular_puntuacion_final(puntaje_final, aciertos, fallos):
    return puntaje_final + calcular_puntuacion_parcial(aciertos, fallos)


def guardar_puntuacion(nombre, puntaje_final) -> bool:
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
        elif buscar_usuario(nombre_usuario, contraseña) == False:
            nuevo_usuario = input("El usuario ingresado no existe, desea crear un usuario(si/no)?")
            if nuevo_usuario == "si":
                crear_usuario()


def submit(palabra_formada, palabras_validas, puntaje, errores):
    existe = False
    for i in range(len(palabras_validas)):
        if palabras_validas[i] == palabra_formada:
            existe = True
            break

    if not existe:
        print("La palabra no existe entre las permitidas.")
        errores += 1

    puntos = len(palabra_formada)
    print(f"✔ ¡Correcto! +{puntos} puntos.")
    puntaje += puntos

    return puntaje, errores, True


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

        repetido = False
        for j in range(len(usados)):
            if usados[j] == indice:
                repetido = True
                break

        if not repetido:
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

    for i in range(len(palabras_pendientes)):
        palabra, palabra_oculta = palabras_pendientes[i]
        for j in range(len(palabra)):
            if palabra[j] == letra_elegida:
                palabra_oculta[j] = letra_elegida

    return letra_elegida



def descartar_letra_incorrecta(palabra, letras_usadas):
    letras_posibles = "abcdefghijklmnopqrstuvwxyz"
    letras_descartables = []
    retornar = ""

    for i in range(len(letras_posibles)):
        letra = letras_posibles[i]

        # verificar si letra está en palabra
        esta_en_palabra = False
        for j in range(len(palabra)):
            if palabra[j] == letra:
                esta_en_palabra = True
                break

        # verificar si letra está en letras_usadas
        esta_en_usadas = False
        for j in range(len(letras_usadas)):
            if letras_usadas[j] == letra:
                esta_en_usadas = True
                break

        # letra descartable si no aparece en ninguno
        if not esta_en_palabra and not esta_en_usadas:
            letras_descartables.append(letra)

    if len(letras_descartables) > 0:
        retornar = random.choice(letras_descartables)

    return retornar


def iniciar_partida(diccionario, max_intentos):
    palabra = convertir_a_minuscula(seleccionar_palabra(diccionario))
    
    # Encontrar la categoría sin usar "in"
    categoria_encontrada = ""
    claves = list(diccionario.keys())
    for i in range(len(claves)):
        clave = claves[i]
        palabras = diccionario[clave]

        for j in range(len(palabras)):
            if convertir_a_minuscula(palabras[j]) == palabra:
                categoria_encontrada = clave
                break

        if categoria_encontrada != "":
            break

    letras_correctas = []
    lista_palabras = obtener_lista_palabras()
    letras_desordenadas = desordenar_cadena(palabra)

    print(f"\nNueva partida. La palabra tiene {len(palabra)} letras.")
    print(f"Letras desordenadas: {letras_desordenadas}\n")

    print("PALABRAS DE LA CATEGORÍA:")
    mostrar_todas_las_palabras_ocultas(diccionario, categoria_encontrada, letras_correctas)

    palabra_oculta = mostrar_palabra_oculta(palabra, letras_correctas)

    # AHORA devuelve 6 cosas
    return palabra, letras_correctas, palabra_oculta, lista_palabras, max_intentos, categoria_encontrada


def procesar_palabra_ingresada(palabra_ingresada, palabras, palabras_ocultas):
    acierto = False
    errores = 0
    puntaje = 0

    # recorrer todas las palabras del nivel
    for i in range(len(palabras)):
        palabra = palabras[i]

        # si coincide exactamente
        if palabra_ingresada == palabra:
            # revelar palabra
            palabras_ocultas[i] = palabra
            acierto = True
            puntaje = len(palabra)   # ejemplo de puntos
            print(f"✔ Correcto. Se reveló: {palabra}")
            break

    if not acierto:
        print("❌ La palabra no coincide con ninguna de la lista.")
        errores = 1

    return palabras_ocultas, puntaje, errores

def verificar_partida(palabra_oculta, intentos_restantes, palabra):
    estado = "jugando"
    if "_" not in palabra_oculta:   # no in
        print(f"¡Ganaste la partida! La palabra era: {palabra}")
        estado = "ganada"
    elif intentos_restantes <= 0:
        print(f"Se acabaron los intentos. La palabra era '{palabra}'.")
        estado = "perdida"
    return estado


def mostrar_todas_las_palabras_ocultas(diccionario2, categoria, letras_correctas):
    palabras = diccionario2[categoria]

    for i in range(len(palabras)):
        palabra = palabras[i]
        
        # Generar palabra oculta sin usar "in"
        palabra_oculta = []
        for j in range(len(palabra)):
            letra = palabra[j]

            esta = False
            for k in range(len(letras_correctas)):
                if letras_correctas[k] == letra:
                    esta = True
                    break
            
            if esta:
                palabra_oculta.append(letra)
            else:
                palabra_oculta.append("_")

        # Imprimir
        for j in range(len(palabra_oculta)):
            print(palabra_oculta[j], end=" ")
        print()

def mostrar_todas(palabras_ocultas):
    for palabra in palabras_ocultas:
        print(palabra)


def actualizar_usuario(usuarios, usuario_actual):
    indice = buscar_usuario(usuarios, usuario_actual["usuario"])
    if indice != -1:
        usuarios[indice] = usuario_actual
        guardar_usuarios(usuarios)