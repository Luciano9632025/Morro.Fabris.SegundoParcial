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


#Shuffle: modifica el orden de las letras
#Clear: borra las letras seleccionadas por el jugador
#Submit: ingresa la palabra seleccionada por el jugador.

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

def hacer_submit(palabra_formada):
    print(palabra_formada)
    return palabra_formada