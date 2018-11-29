class Venda():
    def __init__(self, carro, comprador, vendedor, preco):
        self.carro = carro
        self.comprador = comprador
        self.vendedor = vendedor
        self.preco = preco

    def get_carro(self):
        return self.carro

    def get_comprador(self):
        return self.comprador

    def get_vendedor(self):
        return self.vendedor