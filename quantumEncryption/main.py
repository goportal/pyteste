from random import randint
from Pessoa import Pessoa
from Canal import Canal

# TODO implementar perda no canal

bob = Pessoa("bob")
alice = Pessoa("alice")
eve = Pessoa("eve")

nQubits = input("quantos qubits? ")

bob.geraBasesAleatorias(nQubits)
bob.geraBitsAleatorios(nQubits)

alice.geraBasesAleatorias(nQubits)

canal = Canal(bob.enviarQubits())

onEve = input("Com eve? 1-T 0-F")

if onEve:
    eve.geraBasesAleatorias(nQubits)
    eve.lerQubits(canal.getQubits())

alice.lerQubits(canal.getQubits())

print("bits do bob: ",bob.bits)
print("  bases bob: ",bob.bases)

print("bases alice: ",alice.bases)
print("bits alice: ",alice.bits)

print("bases enviadas para revisao: ",bob.revisaBase(alice.enviaBaseRevisao()))
alice.recebeRevisaBase(bob.revisaBase(alice.enviaBaseRevisao()))
print("bits alice revisados: ",alice.bits)

print("bits para revisao: ",alice.enviaBitRevisao())

if bob.revisaBit(alice.enviaBitRevisao()):
    print("bits compartilhados seguramente")
    print("bits secretos",alice.bitsSecretos())
else:
    print("alguem interceptou os bits!")
