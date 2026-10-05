perfil_autor = {'nombre':'Diego Alvarez',
                'bio':' Data Scientist con 5 años de experiencia',
                'especialidad':'Series de tiempo y Machine Learning',
                'redes_sociales':["diegoalvarezmeza","diego"]
                }

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {'Data Science', 'Machine Learning', 'Python', 'Series de Tiempo', 'Análisis de Datos', "Data Science"}

posts = [
    {
        "id": 1,
        "titulo": "Introducción a Series de Tiempo",
        "contenido": "En este post aprenderemos sobre series de tiempo...",
        "autor": perfil_autor,
        "tags": ["Series de Tiempo", "Python", "Análisis de Datos"],
        "estado": "Publicado"
    },
    {
        "id": 2,
        "titulo": "Machine Learning para Principiantes con Python",
        "contenido": "Este post es una introducción al Machine Learning usando Python...",
        "autor": perfil_autor,
        "tags": ["Machine Learning", "Python"],
        "estado": "Borrador"
    },
    {
        "id": 3,
        "titulo": "Análisis de Datos con Python",
        "contenido": "",
        "autor": perfil_autor,
        "tags": ["Análisis de Datos", "Python"],
        "estado": "Publicado"
    }
]

def menu():
    try:
        print("\n---MENU DEL BLOG---")
        print("1. Ver todos los posts")
        print("2. Buscar por titulo")
        print("3. Filtrar por tag")
        print("4. Validar posts")
        print("5. Salir")
        
    except ValueError:
        print(f"Debe ingresar un numero del 1 al 5, intente de nuevo")

def listar_posts(posts):
    print("Post disponibles: \n")
    for post in posts:
        print(f"Titulo del post: {post['titulo']}| Autor: {post['autor']['nombre']}")

def buscar_por_titulo(posts, termino):
    lista_auxiliar = []
    for post in posts:
        if termino in post['titulo'].lower():
            lista_auxiliar.append(post['titulo'])
    return lista_auxiliar

def filtrar_por_tag(posts, tag_value):
    lista_tags = []
    for post in posts:
        for tag in post["tags"]:
            if tag_value in tag.lower():
                lista_tags.append(post["titulo"])
    return lista_tags

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
        print(f"Falta la clave: {e}")
        return False, f"Falta la clave: {e}"

    if titulo == "":
    
        return False, "El titulo no puede estar vacio"

    if contenido == "":
        print("El contenido no puede estar vacio")
        return False, "El contenido no puede estar vacio"


    if not isinstance(autor,dict):
        print("El autor debe ser un diccionario")
        return False, "El autor debe ser un diccionario"

    try:
        nombre = autor["nombre"]

    except KeyError as e:
        print(f"Falta la clave: {e}")
        return False, f"Falta la clave: {e}"

    return True, "El post es valido"

    



if __name__ == "__main__":

    while True:
        menu()

        val = input("Ingrese una opcion: \n")

        if val == "1":
            listar_posts(posts)


        elif val == "2":
            termino = input("Ingrese un término para buscar en el título: ").lower()
            lista_auxiliar = buscar_por_titulo(posts, termino)
            print(lista_auxiliar)

        elif val == "3":
            tag = input("Ingrese un tag para filtrar los posts: ").lower()
            lista_tags = filtrar_por_tag(posts, tag)
            print(lista_tags)

        elif val == "4":
            for post in posts:
                is_valid, message = validar_post(post)
                print(f"Post: {post['titulo']} - Validación: {message}")
        
        elif val == "5":
            print("Saliendo del programa...\n")
            break

        else:
            print("Opcion invalida, intenta de nuevo")  