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
        return self.nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.nombre = new_nombre


    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, new_edad):
        self.edad = new_edad
    @property
    def colegio(self):
        return self.colegio

    @colegio.setter
    def nombre(self, new_colegio):
        self.colegio = new_colegio

    @classmethod
    def saludo(cls):
        print("Metodo de clase")
    
    @staticmethod
    def statico():
        print("Metodo estatico")
        
    def __new__(cls, *args, **kwargs):
        if args[0] < 3:
            raise ValueError("La edad debe ser mayor o igual a 3")

        instance = super().__new__(cls, *args, **kwargs)

        instance.nombre = args[0]
        instance.edad = args[1]
        instance.colegio = args[2]

        return instance

    def __del__(self):
        print("Estudiante eliminado")