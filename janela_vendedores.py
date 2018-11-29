#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from vendedor import Vendedor

class Janela_Vendedores(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)
        self.controle = controle
        self.geometry('225x225+200+200')
        self.title('Janela de Vendedores')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=5, text='Fechar', command=self.destroy)
        self.btn_add = Button(self, width=10, text='Adicionar').grid(row=5, column=2)
        self.btn_excluir = Button(self, width=10, text='Excluir').grid(row=7, column=2)

        self.cpf_entry_var = StringVar()
        Label(self, text='CPF').grid(row=1, column=1)
        self.cpf_entry = Entry(self, textvariable=self.cpf_entry_var).grid(row=1, column=2)

        self.nome_entry_var = StringVar()
        Label(self, text='Nome').grid(row=2, column=1)
        self.nome_entry = Entry(self, textvariable=self.nome_entry_var).grid(row=2, column=2)

        self.idade_entry_var = StringVar()
        Label(self, text='Idade').grid(row=3, column=1)
        self.idade_entry = Entry(self, textvariable=self.idade_entry_var).grid(row=3, column=2)

        self.matricula_entry_var = StringVar()
        Label(self, text='Matricula').grid(row=4, column=1)
        self.matricula_entry = Entry(self, textvariable=self.matricula_entry_var).grid(row=4, column=2)

        #Matrícula para remoção
        self.matricula_remov_entry_var = StringVar()
        Label(self, text='Matrícula(remover)').grid(row=6, column=1)
        self.matricula_remov_entry = Entry(self, textvariable=self.matricula_remov_entry_var).grid(row=6, column=2)

        # Posicionando os widgets
        self.btn_close.place(x=0, y=175)

        # Metodo para fechar a janela
        def destroy(self):
            # Janela de confirmação
            if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
                super().destroy()


    def adicionar_vendedor(self):
        nome = self.nome_entry_var.get()
        idade = self.idade_entry_var.get()
        cpf = self.cpf_entry_var.get()
        matricula = self.matricula_entry_var.get()
        vendedor = Vendedor(nome, cpf, idade)
        self.controle.bd.adicionar_vendedor(vendedor)
        messagebox.showinfo('Sucesso', 'Vendedor de matricula ' f'{matricula} adicionado.')

    def remover_vendedor(self):
        matricula = self.matricula_entry_var.get()
        remover = None
        if messagebox.askyesno('Excluir', 'Deseja excluir o comprador?') is False:
            return None
        for vendedor in self.controle.bd.mostrar_vendedores():
            if vendedor.get_matricula() == matricula:
                remover = self.controle.bd.remove_vendedor(vendedor)
                messagebox.showinfo('Concluído', 'O vendedor de matrícula' f'{matricula} foi removido.')
        if remover is None:
            messagebox.showerror('Erro', 'Não tem vendedor com essa matrícula')