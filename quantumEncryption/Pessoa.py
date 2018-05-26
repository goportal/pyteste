from random import randint
class Pessoa():
    nome = None
    bits = []
    bases = []

    def __init__(self,nome):
        self.nome = nome

    # def lerQubits(qubit,base):

    # dd => diagonal direita 
    # de => diagonal esquerda 
    # rh => retilineo horizontal
    # rv => retilineo vertical

    def gerarQubits(self,bit,base):
        if(bit == 0 and base == "D"):
            return "dd"
        elif(bit == 0 and base == "R"):
            return "rv"
        elif(bit == 1 and base == "D"):
            return "de"
        elif(bit == 1 and base == "R"):
            return "rh"
        
    def lerQubit(self,qubit,base):
        if(qubit == "dd" and base == "D"):
            return 0
        elif(qubit == "de" and base == "D"):
            return 1
        elif(qubit == "rv" and base == "R"):
            return 0
        elif(qubit == "rh" and base == "R"):
            return 1
        else:
            v = randint(0,3)
            if(v == 0): return ""
            elif(v==1): return ""
            elif(v==2): return 1
            else: return 0
            

    def geraBasesAleatorias(self,nBases):
        self.bases = range(nBases)
        # 1 retilinea
        # 0 diagonal
        for I in self.bases:
            aux = randint(0,1)
            if(aux == 1):
                self.bases[I] = "R"
            else: 
                self.bases[I] = "D"

    def geraBitsAleatorios(self,nBits):
        self.bits = range(nBits)
        for I in self.bits:
            self.bits[I] = randint(0,1)

    def enviarQubits(self):
        qubits = range(len(self.bits))
        for I in range(len(self.bits)):
            qubits[I] = self.gerarQubits(self.bits[I],self.bases[I])
        return qubits

    def lerQubits(self,qubits):
        print("qbits alice leu",qubits)
        bits = range(len(qubits))
        bases = self.bases
        for I in bits:
            bits[I] = self.lerQubit(qubits[I],bases[I])
        self.bits = bits
        

    # def lerQubits(self,qubits,bases):
    #     for I in range(bases):
    #         self.bits = 