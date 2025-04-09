class Circulo:
    pi = 3.1416
    def __init__(self, radio):
        self.radio = radio

    def circunferencia(self):
        return (2*self.pi*self.radio)

if __name__=='__main__':
    instancia = Circulo(float(input("Ingrese el radio: ")))
    print(f"La circunferencia de un circulo de radio {instancia.radio} es: {instancia.circunferencia()}")
