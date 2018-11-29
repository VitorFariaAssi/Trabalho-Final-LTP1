from tkinter import *
from tkinter import messagebox

class Janela_Venda(Toplevel):
    def __init__(self, parent, controle):
        self.controle = controle
        super().__init__(parent)
        self.geometry('210x200+200+200')
        self.title('Janela de Venda')
        self.transient(parent)
        self.grab_set()