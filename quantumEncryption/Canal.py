from random import randint
class Canal():
    qubits = None

    def __init__(self,qubits):
        self.qubits = qubits

    def convertQubit(self,n):
        if(n == 0):
            return "rd"
        elif(n == 1):
            return "rh"
        elif(n == 2):
            return "dd"
        elif(n == 3):
            return "de"

    def alteraQubits(self):
        aux = self.qubits
        for I in range(len(self.qubits)):
            aux[I] = self.convertQubit(randint(0,3))
        self.qubits = aux

    def getQubits(self):
        auxQubits = self.qubits[:]
        self.alteraQubits()
        return auxQubits 

