from blog.datos import posts
from blog.menu import menu
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post



if __name__ == "__main__":

    while True:
        menu()

        val = input("Ingrese una opcion:")

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