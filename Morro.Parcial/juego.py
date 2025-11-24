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



def hacer_shuffle(categoria):
    nuevo_orden = desordenar_cadena(categoria)
    return nuevo_orden

palabra_formada = "banco"
def hacer_clear(palabra_formada):
    nueva = ""
    if palabra_formada == "":
        print("Error..., No hay letras ingresadas.")
    for i in range(len(palabra_formada)-1):
        nueva += palabra_formada[i]
    return nueva


def hacer_submit(palabra_ingresada, palabras, palabras_ocultas):
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


#comodines:


def ubicar_letra_en_palabras(palabras, palabras_ocultas, categoria):
    # elegir letra aleatoria de la categoría
    letra = random.choice(categoria.lower())
    print(f"🔍 Comodín: revelando la letra '{letra}' en todas las palabras")

    for i in range(len(palabras)):
        palabra_real = palabras[i]
        oculta = list(palabras_ocultas[i])   # convertir a lista para editar

        for j in range(len(palabra_real)):
            if palabra_real[j] == letra:     # si la letra coincide
                oculta[j] = letra            # revelar la letra

        palabras_ocultas[i] = "".join(oculta)

    return palabras_ocultas


def revelar_parcialmente_palabra(palabras, palabras_ocultas):
    # encontrar palabras que aún NO fueron descubiertas
    indices_ocultas = [i for i in range(len(palabras)) if palabras_ocultas[i] != palabras[i]]

    if not indices_ocultas:
        print("✔ Todas las palabras ya están descubiertas.")
        return palabras_ocultas

    # elegir una palabra oculta al azar
    idx = random.choice(indices_ocultas)

    palabra_real = palabras[idx]
    palabra_actual = list(palabras_ocultas[idx])

    # cuántas letras vamos a revelar
    cantidad = 2 if len(palabra_real) > 5 else 1

    # obtener posiciones que siguen ocultas ("_")
    posiciones = [i for i, c in enumerate(palabra_actual) if c == "_"]

    if not posiciones:
        return palabras_ocultas

    # elegir posiciones al azar
    posiciones_revelar = random.sample(posiciones, min(cantidad, len(posiciones)))

    for pos in posiciones_revelar:
        palabra_actual[pos] = palabra_real[pos]

    # actualizar la palabra parcialmente descubierta
    palabras_ocultas[idx] = "".join(palabra_actual)

    print(f"🔍 Pista usada: {palabras_ocultas[idx]}")

    return palabras_ocultas


