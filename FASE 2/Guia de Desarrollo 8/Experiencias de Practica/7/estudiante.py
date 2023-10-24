class Estudiante:
    def __init__(self, nombre="Ninguno", edad=3, colegio="Ninguno"):
        self.nombre = nombre
        self.edad = edad
        self.colegio = colegio
        self.matricula = False
        self.pension = False

    def ingresarDatos(self):
        self.nombre = str(input("Ingrese el nombre"))
        self.edad = int(input("Ingrese el edad"))
        self.colegio = str(input("Ingrese el colegio"))
    
    def imprimirDatos(self):
        print(f"Nombre: {self.nombre} Edad: {self.edad} Colegio: {self.colegio}")

    def matricular(self):
        opcion = str(input("Desea matricularse?(S/N)"))
        if opcion == "S":
            self.matricula = True
            print("Matriculado")
        else:
            print("No se matriculo")


    def pagarPension(self):
        opcion = str(input("Desea pagar pension? (S/N)"))
        if opcion == "S":
            self.pension = True
            print("Pension Pagada")
        else:
            print("No pago pension")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self._nombre = new_nombre

