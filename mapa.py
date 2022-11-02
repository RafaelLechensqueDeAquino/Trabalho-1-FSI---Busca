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
            print(str (i) + str (j) + str(celula[0].descricao))
GerarMapa()

mapa = {0: [pantano, 0,0],
        1: [solidoPlano, 0,0],
        2: [solidoPlano, 0,0],
        3: [solidoPlano, 0,0],
        4: [solidoPlano, 0,0],
        5: [solidoPlano, 0,0],
        6: [solidoPlano, 0,0],
        7: [solidoPlano, 0,0],
        8: [solidoPlano, 0,0],
        9: [solidoPlano, 0,0],
        10: [solidoPlano, 0,0],
        11: [solidoPlano, 0,0],
        12: [solidoPlano, 0,0],
        13: [solidoPlano, 0,0],
        14: [solidoPlano, 0,0],
        15: [solidoPlano, 0,0],
        16: [solidoPlano, 0,0],
        17: [solidoPlano, 0,0],
        18: [solidoPlano, 0,0],
        19: [solidoPlano, 0,0],
        20: [solidoPlano, 0,0],
        21: [solidoPlano, 0,0],
        22: [solidoPlano, 0,0],
        23: [solidoPlano, 0,0],
        24: [solidoPlano, 0,0],
        25: [pantano, 0,0],
}

