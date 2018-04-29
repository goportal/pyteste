import json

print("Rodando")

class Teste:
    colidiu = None
    pista = None
    distancia = None
    velocidade = None
    Abs = None
    def __init__(self, colidiu=None, pista=None, distancia=None, velocidade=None, Abs=None):
        self.colidiu = colidiu
        self.pista = pista
        self.distancia = distancia
        self.velocidade = velocidade
        self.Abs = Abs
        
listaColisao = []




teste = Teste("test1","teste2")

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
