perfil_autor = {'nombre':'Diego Alvarez',
                'bio':' Data Scientist con 5 años de experiencia',
                'especialidad':'Series de tiempo y Machine Learning',
                'redes_sociales':["diegoalvarezmeza","diego"]
                }

estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {'Data Science', 'Machine Learning', 'Python', 
                  'Series de Tiempo', 'Análisis de Datos', "Data Science"}

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
