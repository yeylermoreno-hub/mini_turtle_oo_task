class Tortuga:
    def __init__(self):
        self.posicion_x = 0

    def adelante(self, pasos):
        self.posicion_x += pasos
        # dibuja la línea en la posición actual
        print(" " * self.posicion_x + "___")

    def abajo(self):
        # solo baja una línea, manteniendo la posición
        print(" " * self.posicion_x + "___")

    def reiniciar(self):
        self.posicion_x = 0
        print("Tortuga reiniciada")

