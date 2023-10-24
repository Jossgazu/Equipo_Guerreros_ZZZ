numeros = []
for i in range(6):
        numero = float(input(f"Ingrese el numero{i+1}: "))
        if numero not in numeros:
            numeros.append(numero)
        else:
            print("ERR0R NUMERO INGRESADO")

mayor = max(numeros)
menor = min(numeros)

punto_medio = sum(numeros) / len(numeros)

numero_cercano = min(numeros, key=lambda x: abs(x - punto_medio))

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"El número más cercano al punto medio ({punto_medio}) es: {numero_cercano}")
