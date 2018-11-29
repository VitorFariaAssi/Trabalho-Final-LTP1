from janela_principal import Janela_Principal
from bd_simulado import BD_Simulado

#Classe Controle
class Controle():
    #Método construtor
    def __init__(self):
        self.bd = BD_Simulado()
        self.bd.carregar_carros()
        self.bd.carregar_compradores()
        self.bd.carregar_vendedores()
        self.jnl = Janela_Principal(self)
        self.jnl.mainloop()