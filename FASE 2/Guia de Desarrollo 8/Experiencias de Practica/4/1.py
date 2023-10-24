nombre_archivo = "jeje.txt"
try:
    with open(nombre_archivo, "w") as archivo:
        while True:
            linea = input("Ingrese una línea (o ingrese 'chao' para salir): ")
            if linea.lower() == "chao":
                break
            archivo.write(linea + "\n") 
   
    print(f"El archivo '{nombre_archivo}' se ha creado y se le han añadido lo ingresado")
except Exception as e:
    print(f"ERR0R AL CREAR EL ARCHIVO {e}")
