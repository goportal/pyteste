class Nave(object):
    estado = "Pousada"
    def __init__(self,piloto):
        self.piloto = piloto

    def decolar(self):
        self.estado = "Voando na atmosfera"