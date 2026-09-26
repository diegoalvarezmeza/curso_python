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
        "autor": perfil_autor,
        "tags": ["Series de Tiempo", "Python", "Análisis de Datos"],
        "estado": "Publicado"
    },
    {
        "id": 2,
        "titulo": "Machine Learning para Principiantes con Python",
        "autor": perfil_autor,
        "tags": ["Machine Learning", "Python"],
        "estado": "Borrador"
    },
    {
        "id": 3,
        "titulo": "Análisis de Datos con Python",
        "autor": perfil_autor,
        "tags": ["Análisis de Datos", "Python"],
        "estado": "Publicado"
    }
]

while True:
    print("---MENU DEL BLOG---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Salir")

    val = input("Ingrese una opcion: \n")

    if val == "1":
        print("Post disponibles: \n")
        for post in posts:
            print(f"Titulo del post: {post['titulo']}| Autor: {post['autor']['nombre']}")

    elif val == "2":
        palabra = input("Ingrese una palabra: ").lower()
        lista_auxiliar = []
        for post in posts:
            if palabra in post['titulo'].lower():
                lista_auxiliar.append(post['titulo'])
        print(lista_auxiliar)

    elif val == "3":
        pass

    elif val == "4":
        print("Saliendo del programa...\n")
        break
