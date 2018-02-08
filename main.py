from random import randint

def stringToList(frase):
    lista = []
    for letra in frase:
        lista.append(letra)
    return lista

def newList(lista):
    result = []
    for elem in lista:
        result.append("0")
    return result

def getStringFromLista(lista):
    frase = ""
    for letra in lista:
        frase += letra
    return frase

def embaralhar(frase):
    listaFrase = stringToList(frase)
    newFrase = newList(frase)
    for letra in listaFrase:
        posicaoValida = True
        while posicaoValida:
            posicaoAux = randint(0,len(listaFrase)-1)
            if newFrase[posicaoAux] == "0":
                newFrase[posicaoAux] = letra
                posicaoValida = False
    return getStringFromLista(newFrase)

def desembaralhar(fraseOriginal,fraseEmbaralhada):
    listaFraseEmbaralhada = stringToList(fraseEmbaralhada)
    newLista = newList(fraseOriginal)
    for posicao in range(len(fraseOriginal)):
        continua = True
        while continua:
            posicaoAux = randint(0,len(fraseOriginal)-1)
            if fraseOriginal[posicao] == listaFraseEmbaralhada[posicaoAux]:
                newLista[posicao] = listaFraseEmbaralhada[posicaoAux]
                listaFraseEmbaralhada[posicaoAux] = "0"
                continua = False
    return getStringFromLista(newLista)

print("")

frase = input("informe a frase: ")

print("")

print("frase original: "+ frase)

aux = embaralhar(frase)

print("")

print("frase embaralhada: "+aux)

aux2 = desembaralhar(frase,aux)

print("")

print("frase desembaralhada: "+aux2)

print("")









#print("a frase embaralhada: "+ str(frase))






# calculadora completa com funçoes

# v1 = 0
# v2 = 0
# operacao = 0

# def soma(val1,val2):
#     return str(val1+val2)

# def subtrai(val1,val2):
#     return str(val1-val2)

# def multiplica(val1,val2):
#     return str(val1*val2)

# def divide(val1,val2):
#     return str(val1/val2)

# print("inicio da calculadora")
# print(" ")

# continua = True

# while continua:
#     v1 = float(input("informe o valor 1: "))
#     v2 = float(input("informe o valor 2: "))
#     print(" ")
#     print("1 - soma \n2 - subtrai \n3 - multiplica \n4 - divide")
#     operacao = int(input("Oque deseja fazer? "))
#     resultado = 0
#     if operacao == 1:
#         resultado = soma(v1,v2)
#     elif operacao == 2:
#         resultado = subtrai(v1,v2)
#     elif operacao == 3:
#         resultado = multiplica(v1,v2)
#     elif operacao == 4:
#         resultado = divide(v1,v2)
#     else:
#         resultado = "operação invalida !"
#     print(" ")
#     print("resultado: "+resultado)
#     continua = input("continuar? s/n ") == "s"

# print("final")
