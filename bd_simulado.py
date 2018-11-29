import os
from carro import Carro
from vendedor import Vendedor
from comprador import Comprador


class BD_Simulado:
    def __init__(self):
        self.carros = []
        self.vendedor = []
        self.comprador = []
        self.venda = []

    def carregar_carros(self):
        if os.path.exists('Carros.txt'):
            file = open('Carros.txt', 'r')
            for carro in file.readlines():
                carro = carro.strip().lstrip('(').rstrip(')').split(',')
                carro = Carro(carro[0].strip().strip('"').strip("'"), carro[1].strip().strip('"').strip("'"), carro[2].strip().strip('"').strip("'"), carro[3].strip().strip('"').strip("'"), carro[4].strip().strip('"').strip("'"), carro[5].strip().strip('"').strip("'"))
                self.carros.append(carro)
        else:
            file = open('Carros.txt', 'w')
        file.close()

    def carregar_vendedores(self):
        if os.path.exists('Vendedores.txt'):
            file = open('Vendedores.txt', 'r')
            for carro in file.readlines():
                carro = carro.strip().lstrip('(').rstrip(')').split(',')
                vendedor = Vendedor(carro[0].strip().strip('"').strip("'"),
                              carro[1].strip().strip('"').strip("'"),
                              carro[2].strip().strip('"').strip("'"))
                self.vendedor.append(vendedor)
        else:
            file = open('Vendedores.txt', 'w')
        file.close()

    def carregar_compradores(self):
        if os.path.exists('Compradores.txt'):
            file = open('Compradores.txt', 'r')
            for carro in file.readlines():
                carro = carro.strip().lstrip('(').rstrip(')').split(',')
                comprador = Comprador(carro[0].strip().strip('"').strip("'"),
                              carro[1].strip().strip('"').strip("'"))
                self.comprador.append(comprador)
        else:
            file = open('Compradores.txt', 'w')
        file.close()

    def adicionar_carro(self, carro):
        self.carros.append(carro)

    def adicionar_vendedor(self, vendedor):
        self.vendedor.append(vendedor)

    def adicionar_comprador(self, comprador):
        self.comprador.append(comprador)

    def save_carros(self):
        file = open('Carros.txt', 'w')
        for carro in self.carros:
            file.write(str(carro.get_dados()))
            file.write('\n')
        file.close()

    def save_vendedor(self):
        file = open('Vendedores.txt', 'w')
        for c in self.vendedor:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def save_comprador(self):
        file = open('Compradores.txt', 'w')
        for c in self.comprador:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def mostrar_carros(self):
        return self.carros

    def mostrar_vendedores(self):
        return self.vendedor

    def mostrar_compradores(self):
        return self.comprador

    def remove_vendedor(self, vendedor):
        removido = vendedor
        self.vendedor.remove(vendedor)
        return removido

    def remove_comprador(self, comprador):
        removido = comprador
        self.comprador.remove(comprador)
        return removido

    def remove_carro(self, carro):
        removido = carro
        self.carros.remove(carro)
        return removido