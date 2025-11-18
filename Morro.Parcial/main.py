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
from juego import *



        
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


def jugar_encontrar_palabra():
    i = 1
    puntaje = 0
    reinicios_restantes = 5
    while i < 2:
        jugar_nivel(i, puntaje, reinicios_restantes)
        i += 1


jugar_encontrar_palabra()



