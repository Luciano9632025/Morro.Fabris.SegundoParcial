rom utilidades import obtener_categorias, seleccionar_palabra, ubicar_letra, mezclar_letras, revelar_palabra

def jugar(diccionario):

    reinicios_disponibles = 3
    puntaje_total = 0
    errores_totales = 0
    niveles_totales = 5

    for nivel in range(1, niveles_totales + 1):

        print("\n===========================")
        print(f"      NIVEL {nivel}")
        print("===========================\n")

        partidas_ganadas = 0

        while partidas_ganadas < 3:

            categoria, palabra_correcta = seleccionar_palabra(diccionario)
            letras_desordenadas = mezclar_letras(palabra_correcta)

            errores = 0
            tiempo_restante = 15
            comodin_revelar = True
            comodin_ubicar = True
            comodin_extra = True
            seleccion_actual = ""

            print(f"\nCategoría: {categoria}")
            print(f"Letras desordenadas: {letras_desordenadas}")

            while True:
                print("\n--- OPCIONES ---")
                print("1. Mezclar letras")
                print("2. Borrar selección")
                print("3. Enviar palabra")
                print("4. Activar comodín: Revelar palabra")
                print("5. Activar comodín: Ubicar letra")
                print("6. Activar comodín extra (sin definir)")
                print(f"(Tiempo restante simulado: {tiempo_restante})")

                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    letras_desordenadas = mezclar_letras(palabra_correcta)
                    print("Letras mezcladas:", letras_desordenadas)

                elif opcion == "2":
                    seleccion_actual = ""
                    print("Selección borrada.")

                elif opcion == "3":
                    seleccion_actual = input("Ingrese su palabra: ").upper()

                    if seleccion_actual == palabra_correcta:
                        print("¡Correcto!")
                        puntaje_total += len(palabra_correcta)
                        partidas_ganadas += 1
                        break
                    else:
                        print("Palabra incorrecta.")
                        errores += 1
                        errores_totales += 1

                elif opcion == "4" and comodin_revelar:
                    print("Comodín activado:")
                    print("Pista:", revelar_palabra(palabra_correcta))
                    comodin_revelar = False

                elif opcion == "5" and comodin_ubicar:
                    letra = ubicar_letra(palabra_correcta)
                    print(f"La letra '{letra}' aparece en la palabra.")
                    comodin_ubicar = False

                elif opcion == "6" and comodin_extra:
                    print("Comodín extra activado (sin funcionalidad definida).")
                    comodin_extra = False

                tiempo_restante -= 1

                if tiempo_restante <= 0:
                    print("\nSe quedó sin tiempo. El nivel se reinicia.")
                    reinicios_disponibles -= 1
                    if reinicios_disponibles == 0:
                        print("\nSe quedó sin reinicios. Fin del juego.")
                        return
                    print(f"Reinicios restantes: {reinicios_disponibles}")
                    partidas_ganadas = 0
                    break

            print("\nResumen de la partida:")
            print("Errores cometidos:", errores)
            print("Puntaje acumulado:", puntaje_total)

        print(f"\nNIVEL {nivel} COMPLETADO.")

    print("\n=============================")
    print("       ¡VICTORIA!")
    print("=============================")
    print(f"Puntaje total: {puntaje_total}")
    print(f"Errores totales: {errores_totales}\n")
