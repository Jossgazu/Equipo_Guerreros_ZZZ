from estudiante import Estudiante


tapir = Estudiante("Tapir", 90, "Publico")
tapir2 = Estudiante("Tapir2", 92, "Publico")
tapir3 = Estudiante("Tapir3", 93, "Publico")
tapir4 = Estudiante("Tapir4", 94, "Publico")
tapir5 = Estudiante("Tapir5", 95, "Publico")

listas = [tapir, tapir2, tapir3, tapir4, tapir5]
for lista in listas:
    lista.imprimirDatos()

