import json

class Fato:
    colidiu = None
    pista = None
    distancia = None
    velocidade = None
    def __init__(self, colidiu, pista, distancia, velocidade):
        self.colidiu = colidiu
        self.pista = pista
        self.distancia = distancia
        self.velocidade = velocidade
    def print(self):
        print("----------------------------------")
        if(self.colidiu == None):
            print("Ainda não avaliado se baterá")
        elif(self.colidiu == True):
            print("colidiu: Sim")
        else:
            print("colidiu: Não")
        print("pista: "+self.pista)
        print("distancia: "+self.distancia)
        print("velocidade: "+self.velocidade)
        print("----------------------------------")
    def classificar(self,fatos):
        bateu = 0
        naoBateu = 0
        pistaTrue = 0
        pistaFalse = 0
        distanciaTrue = 0
        distanciaFalse = 0
        velocidadeTrue = 0
        velocidadeFalse = 0

        for I in range(len(fatos)):
            if fatos[I].colidiu:
                bateu += 1
            else:
                naoBateu += 1
            if(self.pista == fatos[I].pista):
                if(fatos[I].colidiu):
                    pistaTrue += 1
                else:
                    pistaFalse += 1
            if(self.distancia == fatos[I].distancia):
                if(fatos[I].colidiu):
                    distanciaTrue += 1
                else:
                    distanciaFalse += 1
            if(self.velocidade == fatos[I].velocidade):
                if fatos[I].colidiu:
                    velocidadeTrue += 1
                else:
                    velocidadeFalse +=1
        
        perColidiu = (pistaTrue/bateu)*(distanciaTrue/bateu)*(velocidadeTrue/bateu)
        perNaoColidiu = (pistaFalse/naoBateu)*(distanciaFalse/naoBateu)*(velocidadeFalse/naoBateu)

        if(perColidiu > perNaoColidiu):
            self.colidiu = True
        else:
            self.colidiu = False
        

            

fatos = {}

fatos[0] = Fato(False,"seca","alta","baixa")
fatos[1] = Fato(False,"seca","media","baixa")
fatos[2] = Fato(False,"seca","alta","media")
fatos[3] = Fato(False,"molhada","alta","baixa")
fatos[4] = Fato(True,"molhada","media","alta")
fatos[5] = Fato(True,"molhada","media","alta")
fatos[6] = Fato(True,"molhada","baixa","media")
fatos[7] = Fato(True,"molhada","media","media")
fatos[8] = Fato(True,"seca","baixa","alta")
fatos[9] = Fato(True,"seca","baixa","media")


print("insira um novo fato ...")
pista = input("Condicao da pista: ")
distancia = input("Distancia: ")
velocidade = input("velocidade: ")

newFato = Fato(None,pista,distancia,velocidade)

newFato.classificar(fatos)

newFato.print()

# newFato.print()





# teste = Teste("test1","teste2")

# print(teste.bar)

# class dado():
    # colidiu = ""
    # pista = ""
    # distancia = ""
    # velocidade = ""
    # Abs = ""

#     def _new_(self,c,p,d,v,a):
#         self.colidiu = c
#         self.pista = p
#         self.distancia = d
#         self.velocidade = v
#         self.Abs = a


# dado1 = ('')

# dados = [
#     {
#         colidiu:false,
#         pista:"seca",
#         "distancia":"longe",
#         "velocidade":"alta",
#         "abs":true
#     },
#     {
#         "colidiu":true,
#         "pista":"molhada",
#         "distancia":"perto",
#         "velocidade":"alta",
#         "abs":false
#     },
#     {
#         "colidiu":false,
#         "pista":"molhada",
#         "distancia":"longe",
#         "velocidade":"alta",
#         "abs":true
#     },
#     {
#         "colidiu":false,
#         "pista":"seca",
#         "distancia":"longe",
#         "velocidade":"baixa",
#         "abs":false
#     },
#     {
#         "colidiu":true,
#         "pista":"seca",
#         "distancia":"perto",
#         "velocidade":"alta",
#         "abs":false
#     },
#     {
#         "colidiu":true,
#         "pista":"molhada",
#         "distancia":"longe",
#         "velocidade":"alta",
#         "abs":false
#     },
#     {
#         "colidiu":true,
#         "pista":"molhada",
#         "distancia":"perto",
#         "velocidade":"alta",
#         "abs":true
#     }
# ]

# for dado in dados:
#     print("aqui o dado: "+dado)

# try:
#     dados_json = open('./dados.json','r')
#     dados_json = json.load(dados_json)
#     colisoes = dados_json['colisoes']
