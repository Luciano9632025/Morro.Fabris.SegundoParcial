import json

USUARIOS_FILE = "usuarios.json"

def cargar_usuarios():
    usuarios = []
    try:
        archivo = open(USUARIOS_FILE, "r")
        contenido = archivo.read()
        archivo.close()
        if contenido != "":
            datos = json.loads(contenido)
            usuarios = datos["usuarios"]
    except:
        usuarios = []
    return usuarios

def guardar_usuarios(usuarios):
    datos = {"usuarios": usuarios}
    archivo = open(USUARIOS_FILE, "w")
    archivo.write(json.dumps(datos, indent=4))
    archivo.close()

def buscar_usuario(usuarios, nombre):
    indice_encontrado = -1
    for i in range(len(usuarios)):
        if usuarios[i]["nombre"] == nombre:
            indice_encontrado = i
    return indice_encontrado

def registrar_usuario(usuarios, nombre, contraseña):
    registrado = False
    if buscar_usuario(usuarios, nombre) == -1:
        nuevo_usuario = {
            "nombre": nombre,
            "contraseña": contraseña,
            "puntaje_total": 0,
            "errores": 0,
            "tiempo_restante": 0,
            "reinicios_restantes": 3,
            "comodines": {
                "revelar_palabra": 3,
                "ubicar_letra": 3,
                "comodin_extra": 3
            },
            "nivel_actual": 1,
            "partida_actual": 1
        }
        usuarios.append(nuevo_usuario)
        guardar_usuarios(usuarios)
        registrado = True
    return registrado

def login_usuario(usuarios, nombre, contraseña):
    usuario_valido = None
    indice = buscar_usuario(usuarios, nombre)
    if indice != -1:
        if usuarios[indice]["contraseña"] == contraseña:
            usuario_valido = usuarios[indice]
    return usuario_valido