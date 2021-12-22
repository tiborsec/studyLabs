class Carro(object):


    def __init__(self, portas, cor, marca, modelo, ano):
        self.portas = portas
        self.rodas = 4
        self.cor = cor
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


    def anda(self, kilometros):
        return 'Carro andou ' + str(kilometros) + ' km. '