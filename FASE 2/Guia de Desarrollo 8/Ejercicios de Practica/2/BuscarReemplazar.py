def buscar_y_reemplazar(archivo, texto_buscar, texto_reemplazar):
    with open(archivo, 'r') as file:
        contenido = file.read()

    contenido_modificado = contenido.replace(texto_buscar, texto_reemplazar)

    with open(archivo, 'w') as file:
        file.write(contenido_modificado)

archivo = input("Ingrese el nombre del archivo: ")
texto_buscar = input("Texto a buscar: ")
texto_reemplazar = input("Texto de reemplazo: ")

buscar_y_reemplazar(archivo, texto_buscar, texto_reemplazar)
print(f"Texto '{texto_buscar}' reemplazado con '{texto_reemplazar}' en el archivo '{archivo}'.")
