class Autor:

    def __init__(self, nombre, bio, especialidad, redes_sociales):
        self.nombre = nombre
        self.bio = bio
        self.especialidad = especialidad
        self.redes_sociales = redes_sociales

class Post:
    def __init__(self, id, titulo, contenido, autor, tags, estado):
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags
        self.estado = estado

class Blog:
    def __init__(self, nombre):
        self.nombre = nombre
        self.posts = []

    def listar_posts(self):
        print("-------- Post disponibles ------ \n")
        for post in self.posts:
            print(f"Titulo del post: {post.titulo}| Autor: {post.autor.nombre}")

    def buscar_por_titulo(self, termino):
        lista_auxiliar = []
        for post in self.posts:
            if termino.lower() in post.titulo.lower():
                lista_auxiliar.append(post.titulo)
        return lista_auxiliar

    def filtrar_por_tag(self, tag_value):
        lista_tags = []
        for post in self.posts:
            for tag in post.tags:
                if tag_value.lower() in tag.lower():
                    lista_tags.append(post.titulo)
        return lista_tags

    def agregar_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.titulo}' agregado al blog '{self.nombre}'")

    def validar_post(self, Post):
        if not isinstance(Post, Post):
            return False, "El post debe ser una instancia de la clase Post"
        
        if Post.titulo == "":
            return False, "El titulo no puede estar vacio"
        
        if Post.contenido == "":
            return False, "El contenido no puede estar vacio"
        
        if not isinstance(Post.autor, Autor):
            return False, "El autor debe ser una instancia de la clase Autor"
        
        if not isinstance(Post.tags, list):
            return False, "la clave tags debe ser una lista"
        
        if not (Post.estado.lower() in ["borrador", "publicado", "archivado"]):
            return False, f"Estado no valido, debe ser uno de los estados disponibles: ['borrador', 'publicado', 'archivado']"
        return True, "El post es valido"

    def get_posts(self):
        for post in self.posts:
            print(f"ID: {post.id}, Titulo: {post.titulo}, Autor: {post.autor.nombre}, Estado: {post.estado}")

        