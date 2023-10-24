def procesar_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"LETRA: {clave}, NUMER0: {valor}")

diccionario = {"a": 1, "b": 2, "c": 3}
procesar_diccionario(diccionario)
