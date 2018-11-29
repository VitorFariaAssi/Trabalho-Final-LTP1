from tkinter import *
from tkinter import messagebox
from venda import Venda
from carro import Carro
from janela_venda import Janela_Venda

class Janela_Patio(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)
        self.controle = controle
        self.geometry('250x250+200+200')
        self.title('Pátio')
        self.transient(parent)
        self.grab_set()

        l = 0
        c = 0
        for carro in self.controle.bd.carros:
            self.botao_carro = Button(self, width=10, text=carro.get_placa(), command=self.criar_janela_venda).grid(row=l, column=c)
            c += 1
            if c == 3:
                c = 0
                l += 1

    def criar_janela_venda(self, controle):
        Janela_Venda(self, controle)