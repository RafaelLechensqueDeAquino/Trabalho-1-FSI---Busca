class Terreno:
    def __init__(self, descricao, custo, cor):
        self.descricao = descricao
        self.custo = custo
        self.cor = cor

    def __str__(self):
        return 'Descrição: ' + self.descricao + ' Custo: ' + str (self.custo) + ' Cor: ' + str (self.cor)
    