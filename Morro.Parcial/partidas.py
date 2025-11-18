def cargar_partidas(archivo_csv):
    partidas = []
    try:
        archivo = open(archivo_csv, "r")
        lineas = archivo.readlines()
        archivo.close()
        for i in range(1, len(lineas)):
            fila = lineas[i].strip().split(",")
            if len(fila) == 3:
                partida = {
                    "nivel": int(fila[0]),
                    "partida": int(fila[1]),
                    "palabra": fila[2]
                }
                partidas.append(partida)
    except:
        partidas = []
    return partidas

def obtener_palabras_por_partida(partidas, nivel, partida):
    palabras_partida = []
    for i in range(len(partidas)):
        if partidas[i]["nivel"] == nivel and partidas[i]["partida"] == partida:
            palabras_partida.append(partidas[i]["palabra"])
    return palabras_partida