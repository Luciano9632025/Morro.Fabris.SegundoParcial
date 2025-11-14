def buscar_caracter_valido(caracter: str, caracteres_validos: str) -> bool:
    """Verifica si un caracter pertenece a un grupo de caracteres validos.

    Args:
        caracter (str): caracter a validar.
        caracteres_validos (str): cadena que contiene todos los caracteres validos.

    Returns:
        bool: Retorna true si el caracter esta dentro de los caracteres validos, False en caso contrario
    """   
    encontro = False
    for j in range(len(caracteres_validos)):
        if caracter == caracteres_validos[j]:
            encontro = True
            break
    
    return encontro


def normalizar_texto(cadena: str) -> str:
    """Convierte la cadena dada para que la primera letra sea mayuscula y el resto minuscula.

    Args:
        cadena (str): texto a cambiar.

    Returns:
        str: Devuelve una cadena con primera letra en mayuscula y el resto en minuscula.
    """
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    cadena_convertida = ""

    for i in range(len(cadena)):
        caracter = cadena[i]
        letra_convertida = caracter

        if i == 0:
            #primera letra mayuscula
            if buscar_caracter_valido(caracter, minusculas) == True:
                letra_convertida = chr(ord(caracter) - 32)
        else:
            if buscar_caracter_valido(caracter, mayusculas) == True:
                letra_convertida = chr(ord(caracter) + 32)

        cadena_convertida += letra_convertida

    return cadena_convertida


def buscar_elemento(lista: list, elemento: str) -> int:
    """Busca un elemento dentro de una lista y devuelve su posición.

    Args:
        lista (list): Lista en la que se busca el elemento.
        elemento (str): Elemento a buscar.

    Returns:
        int: Indice del elemento si se encuentra, -1 si no se encuentra.
    """
    posicion = -1
    i = 0
    while i < len(lista):
        if lista[i] == elemento:
            posicion = i
            i = len(lista)
        else:
            i += 1

    return posicion


def validar_numero(cadena_numero: str) -> bool:
    """Verifica si una cadena representa un numero entre 1 y 10.

    Args:
        cadena_numero (str): Cadena de texto a validar.

    Returns:
        bool: True si es numero valido, False en caso contrario.
    """    
    es_numero_valido = False
    #Un solo digito
    if len(cadena_numero) == 1:
        if cadena_numero[0] >= "1" and cadena_numero[0] <= "9":
            es_numero_valido = True
    #dos digitos
    elif len(cadena_numero) == 2:
        if cadena_numero[0] == "1" and cadena_numero[1] == "0":
            es_numero_valido = True

    return es_numero_valido


puntaje_final = 0