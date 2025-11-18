import random

def obtener_categorias(diccionario):
    categorias = []
    for clave in diccionario:
        categorias.append(clave)
    return categorias

def obtener_palabras(diccionario, categoria):
    return diccionario[categoria]

def mezclar_letras(palabra):
    lista = list(palabra)
    random.shuffle(lista)
    return ''.join(lista)

def seleccionar_palabra(diccionario):
    categorias = obtener_categorias(diccionario)
    categoria = random.choice(categorias)
    palabras = obtener_palabras(diccionario, categoria)
    palabra = random.choice(palabras)
    return categoria, palabra.upper()

def revelar_palabra(palabra):
    cantidad = max(1, len(palabra) // 2)  
    indices = random.sample(range(len(palabra)), cantidad)

    revelada = []
    for i in range(len(palabra)):
        if i in indices:
            revelada.append(palabra[i])
        else:
            revelada.append("_")

    return "".join(revelada)

def ubicar_letra(lista_palabras):
    
    letras = []
    for palabra in lista_palabras:
        for letra in palabra:
            if letra not in letras:
                letras.append(letra)

    letra_seleccionada = random.choice(letras)

    posiciones = {}
    for palabra in lista_palabras:
        ubicaciones = []
        for i in range(len(palabra)):
            if palabra[i] == letra_seleccionada:
                ubicaciones.append(i)
        posiciones[palabra] = ubicaciones

    return letra_seleccionada, posiciones
