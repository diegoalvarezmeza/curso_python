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