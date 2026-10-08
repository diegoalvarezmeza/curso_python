def listar_posts(posts):
    print("-------- Post disponibles ------ \n")
    for post in posts:
        print(f"Titulo del post: {post['titulo']}| Autor: {post['autor']['nombre']}")


def buscar_por_titulo(posts, termino):
    lista_auxiliar = []
    for post in posts:
        if termino.lower() in post['titulo'].lower():
            lista_auxiliar.append(post['titulo'])
    return lista_auxiliar


def filtrar_por_tag(posts, tag_value):
    lista_tags = []
    for post in posts:
        for tag in post["tags"]:
            if tag_value.lower() in tag.lower():
                lista_tags.append(post["titulo"])
    return lista_tags