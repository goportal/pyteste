from random import randint
from Pessoa import Pessoa
from Canal import Canal

# TODO implementar perda no canal

bob = Pessoa("bob")
alice = Pessoa("alice")

nQubits = input("quantos qubits? ")

bob.geraBasesAleatorias(nQubits)
bob.geraBitsAleatorios(nQubits)
alice.geraBasesAleatorias(nQubits)


canal = Canal(bob.enviarQubits())


alice.lerQubits(canal.getQubits())

print("bits do bob: ",bob.bits)
print("  bases bob: ",bob.bases)

print("bases alice: ",alice.bases)
print("bits alice: ",alice.bits)



# if(input("bits aleatorios? ") == 1):
    
# else:
    # print(alice.nome)


# randint(0,1)