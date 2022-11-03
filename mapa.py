from random import sample
from terreno import Terreno

solidoPlano = Terreno(descricao='Solido e Plano',custo=1, cor=[153, 102, 0])
rochoso = Terreno(descricao='Rochoso',custo=10, cor=[0, 153, 51])
arenosos = Terreno(descricao='Arenosos',custo=4, cor=[255, 255, 0])
pantano = Terreno(descricao='Pântano',custo=20, cor=[0, 153, 51])
parede = Terreno(descricao='Parede',custo=100, cor=[0, 153, 51])

terrenos = [solidoPlano, rochoso, arenosos, pantano, parede]

def GerarMapa():
    for i in range(5):
        for j in range(5):
            celula = sample(terrenos, 1)
            #print(str (i) + str (j) + str(celula[0].descricao))
GerarMapa()

mapa = {0: [pantano, 0,0],
        1: [solidoPlano, 0,1],
        2: [solidoPlano, 0,2],
        3: [parede, 0,3],
        4: [parede, 0,4],
        5: [parede, 1,0],
        6: [solidoPlano, 1,1],
        7: [solidoPlano, 1,2],
        8: [solidoPlano, 1,3],
        9: [solidoPlano, 1,4],
        10: [solidoPlano, 2,0],
        11: [solidoPlano, 2,1],
        12: [solidoPlano, 2,2],
        13: [solidoPlano, 2,3],
        14: [solidoPlano, 2,4],
        15: [solidoPlano, 3,0],
        16: [solidoPlano, 3,1],
        17: [solidoPlano, 3,2],
        18: [solidoPlano, 3,3],
        19: [solidoPlano, 3,4],
        20: [solidoPlano, 4,0],
        21: [solidoPlano, 4,1],
        22: [solidoPlano, 4,2],
        23: [solidoPlano, 4,3],
        24: [pantano, 4,4],
}

