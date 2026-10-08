from .datos import estados_post

def validar_post(new_post):
    if not isinstance(new_post, dict):
        print("El post debe ser un diccionario")
        return False
    try:
        titulo = new_post["titulo"]
        autor = new_post["autor"]
        contenido = new_post["contenido"]
        tags = new_post["tags"]
        estado = new_post["estado"]

    except KeyError as e:
        return False, f"Falta la clave: {e}"

    if titulo == "":
    
        return False, "El titulo no puede estar vacio"

    if contenido == "":
        return False, "El contenido no puede estar vacio"


    if not isinstance(autor,dict):
        return False, "El autor debe ser un diccionario"

    try:
        nombre = autor["nombre"]

    except KeyError as e:
        return False, f"Falta la clave: {e}"

    if not isinstance(tags, list):
        return False, "la clave tags debe ser una lista"

    if not (estado.lower() in estados_post):
        return False, f"Estado no valido, debe ser uno de los estados disponibles: {estados_post}"

    return True, "El post es valido"