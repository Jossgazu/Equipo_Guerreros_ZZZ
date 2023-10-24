def verificar_palabra_en_archivo(archivo, palabra_a_buscar):
    try:
        with open(archivo, 'r') as file:
            contenido = file.read()
            palabras = contenido.split()

            if palabra_a_buscar in palabras:
                print(f"La palabra '{palabra_a_buscar}' fue encontrada en el archivo.")
            else:
                print(f"La palabra '{palabra_a_buscar}' no fue encontrada en el archivo.")
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

archivo = input("Ingrese el nombre del archivo: ")
palabra_a_buscar = input("Ingrese la palabra que desea buscar: ")

verificar_palabra_en_archivo(archivo, palabra_a_buscar)
