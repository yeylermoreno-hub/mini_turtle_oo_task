class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        print(f"Tortuga avanza a la posición {self.posicion_x}")

    def abajo(self):
        print("Tortuga baja una línea")

    def reiniciar(self):
        self.posicion_x = 0
        print("Tortuga reiniciada a la posición 0")
