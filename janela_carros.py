#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from carro import Carro

#Classe Segunda Janela
class Janela_Carros(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)
        self.controle = controle
        self.geometry('275x250+200+200')
        self.title('Janela de Carros')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=5, text='Sair', command=self.destroy)
        self.btn_add = Button(self, width=10, text='Adicionar', command=self.adicionar_carro).grid(row=6, column=1)
        self.btn_excluir = Button(self, width=10, text='Excluir', command=self.remover_carro).grid(row=8, column=1)

        # Posicionando os widgets
        self.btn_close.place(x=229, y=224)

        Label(self, text='').grid(row=0, column=2, padx=20, pady=2)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=2)
        Label(self, text='').grid(row=47, column=0, padx=20, pady=20)

        self.entry_modelo_var = StringVar()
        Label(self, text='Modelo').grid(row=0, column=0)
        self.entry_modelo = Entry(self, textvariable=self.entry_modelo_var).grid(row=0, column=1)

        self.entry_marca_var = StringVar()
        Label(self, text='Marca').grid(row=1, column=0)
        self.entry_marca = Entry(self, textvariable=self.entry_marca_var).grid(row=1, column=1)

        self.entry_estado_var = StringVar()
        Label(self, text='Estado').grid(row=2, column=0)
        self.entry_estado = Entry(self, textvariable=self.entry_estado_var).grid(row=2, column=1)

        self.entry_placa_var = StringVar()
        Label(self, text='Placa').grid(row=3, column=0)
        self.entry_placa = Entry(self, textvariable=self.entry_placa_var).grid(row=3, column=1)

        self.entry_ano_var = StringVar()
        Label(self, text='Ano').grid(row=4, column=0)
        self.entry_ano = Entry(self, textvariable=self.entry_ano_var).grid(row=4, column=1)

        self.entry_preco_var = StringVar()
        Label(self, text='Preço').grid(row=5, column=0)
        self.entry_preco = Entry(self, textvariable=self.entry_preco_var).grid(row=5, column=1)

        self.entry_placa_remov_var = StringVar()
        Label(self, text='Placa do carro').grid(row=7, column=0)
        self.entry_placa_remov = Entry(self, textvariable=self.entry_placa_remov_var).grid(row=7, column=1)



        # Metodo para fechar a janela
        def destroy(self):
            # Janela de confirmação
            if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
                super().destroy()

    def adicionar_carro(self):
        modelo = self.entry_modelo_var.get()
        marca = self.entry_marca_var.get()
        ano = self.entry_ano_var.get()
        preco = self.entry_preco_var.get()
        estado = self.entry_estado_var.get()
        placa = self.entry_placa_var.get()
        carro = Carro(modelo, marca, ano, estado, preco, placa)
        self.controle.bd.adicionar_carro(carro)
        self.controle.bd.save_carros()
        messagebox.showinfo('Sucesso', 'Carro ' f'{placa} adicionado.')

    def remover_carro(self):
        placa = self.entry_placa_remov_var.get()
        remover = None
        if messagebox.askyesno('Excluir', 'Deseja excluir o carro?') is False:
            return None
        for carro in self.controle.bd.mostrar_carros():
            if carro.get_placa() == placa:
                remover = self.controle.bd.remove_carro()
                messagebox.showinfo('Concluído', 'O carro de placa' ,f'{placa} foi removido.')
        if remover is None:
            messagebox.showerror('Erro!!!', 'Não tem carro com esses dados')




