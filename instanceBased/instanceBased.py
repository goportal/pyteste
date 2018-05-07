def calculaEuclidiana(obj1,obj2):
    soma = 0
    for I in range(len(obj1)):
        soma += (obj1[I] - obj2[I])**2
    return soma ** 0.5

def calculaMinkowski(obj1,obj2,p):
    # p = 2 => distancia Euclidiana
    # p = 1 => distancia de Manhattan
    soma = 0
    for I in range(len(obj1)):
        soma += (abs(obj1[I] - obj2[I]))**p
    return soma ** (1/p) 

def delta(obj1,obj2):
    if((obj1 == None or obj2 == None) or (obj1 == 'None' or obj2 == 'None')):
        return 0
    else:
        return 1

def calculaMinkowskiNormalizada(obj1,obj2,p):
    soma = 0
    somaDelta = 0
    for I in range(len(obj1)):
        if(delta(obj1[I],obj2[I])):
            somaDelta+=1
            soma += (abs(obj1[I] - obj2[I])) ** p
    return (soma ** (1/p))/somaDelta

# def calculaMahalanobis()

obj1 = {}
obj1[0] = 2
obj1[1] = -1
obj1[2] = None
obj1[3] = 0

# print("len ",obj1[2])

obj2 = {}
obj2[0] = 7
obj2[1] = 0
obj2[2] = -4
obj2[3] = 8

# print("Result Euclidiana = ",calculaEuclidiana(obj1,obj2))

# print("Result Minkowski = ", calculaMinkowski(obj1,obj2,2))

# print("Result Minkowski normalizada = ", calculaMinkowskiNormalizada(obj1,obj2,2))