from random import randint
from Pessoa import Pessoa
from Canal import Canal

# bug de quando adiciona eve em quantia pequena e da resultado positivo

def bb84():
    # leitura de dados
    nQubits = input("Quantos qubits? ")
    onEve = input("Com eve? 1-T 0-F ")
    verbose = input("Exibicao completa? 1-T 0-F")
    print("")

    # instancia de pessoas 
    bob = Pessoa("bob")
    alice = Pessoa("alice")

    # gera bases e bits aleatorios de bob 
    bob.geraBasesAleatorias(nQubits)
    bob.geraBitsAleatorios(nQubits)
    if verbose == 1:
        print("bits do bob",bob.bits)
        print("bases bob",bob.bases)
        raw_input("")

    # gera as bases aleatorias de alice
    alice.geraBasesAleatorias(nQubits)
    if verbose == 1:
        print("bases alice",alice.bases)
        raw_input("")

    # bob envia os qubits para o canal
    canal = Canal(bob.enviarQubits())
    if verbose == 1:
        print("bob envia qubits",bob.enviarQubits())
        raw_input("")

    # se a eve observar o canal gera as bases de eve e le os qubits do canal
    if onEve:
        eve = Pessoa("eve")
        eve.geraBasesAleatorias(nQubits)
        eve.lerQubits(canal.getQubits())
        if verbose == 1:
            print("bits que eve leu",eve.bits)
            raw_input("")
    
    # alice le os bits do canal
    alice.lerQubits(canal.getQubits())
    if verbose == 1:
        print("bits que alice intercepta",alice.bits)
        raw_input("")

    # alice envia as bases que recebeu para bob validar
    if verbose == 1:
        print("bases que alice envia para revisar",alice.enviaBaseRevisao())
        raw_input("")

    # bob revisa as bases de alice
    if verbose == 1:
        print("bob revisa as bases enviadas de alice",bob.revisaBase(alice.enviaBaseRevisao()))
    alice.recebeRevisaBase(bob.revisaBase(alice.enviaBaseRevisao()))
    if verbose == 1:
        raw_input("")

    # bits que estao com alice
    if verbose == 1:
        print("bits confirmados de alice",alice.bits)
        raw_input("")

    # alice envia 1/3 de bits para revisao
    bitsRevisao = alice.enviaBitRevisao()
    if verbose == 1:
        print("bits que alice envia para revisao",bitsRevisao)
        raw_input("")

    # bob verifica os bits enviados por alice
    if verbose == 1:
        if bob.revisaBit(bitsRevisao):
            print("bits compartilhados de modo seguro")
            print("bits secretos com alice",alice.bitsSecretos())
            print("bits secretos com bob",bob.bitsSecretos())
        else:
            print("alguem interceptou os bits!")
            print("bits com alice",alice.bitsSecretos())
            print("bits com bob",bob.bitsSecretos())
    else:
        if bob.revisaBit(bitsRevisao):
            print("bits compartilhados de modo seguro")
            print("bits secretos",bob.bitsSecretos())
        else:
            print("alguem interceptou os bits!")

bb84()