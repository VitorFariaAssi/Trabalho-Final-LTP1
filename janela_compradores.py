from tkinter import *
from tkinter import messagebox
from comprador import Comprador

class Janela_Compradores(Toplevel):
    def __init__(self, parent, controle):
        self.controle = controle
        super().__init__(parent)
        self.geometry('210x200+200+200')
        self.title('Janela de Compradores')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=5, text='Fechar', command=self.destroy)
        self.btn_add = Button(self, width=10, text='Adicionar', command=self.adicionar_comprador).grid(row=4, column=2)
        self.btn_excluir = Button(self, width=10, text='Excluir', command=self.remover_comprador).grid(row=6, column=2)

        self.cpf_entry_var = StringVar()
        Label(self, text='CPF').grid(row=1, column=1)
        self.cpf_entry = Entry(self, textvariable=self.cpf_entry_var).grid(row=1, column=2)

        self.nome_entry_var = StringVar()
        Label(self, text='Nome').grid(row=2, column=1)
        self.nome_entry = Entry(self, textvariable=self.nome_entry_var).grid(row=2, column=2)

        self.idade_entry_var = StringVar()
        Label(self, text='Idade').grid(row=3, column=1)
        self.idade_entry = Entry(self, textvariable=self.idade_entry_var).grid(row=3, column=2)

        self.cpf_remov_entry_var = StringVar()
        Label(self, text='CPF(remover)').grid(row=5, column=1)
        self.cpf_remov_entry = Entry(self, textvariable=self.cpf_remov_entry_var).grid(row=5, column=2)



        # Posicionando os widgets
        self.btn_close.place(x=164, y=174)

        # Metodo para fechar a janela
        def destroy(self):
            # Janela de confirmação
            if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
                super().destroy()

    def adicionar_comprador(self):
        cpf = self.cpf_entry_var.get()
        nome = self.nome_entry_var.get()
        idade = self.idade_entry_var.get()
        comprador = Comprador(nome, cpf, idade)
        self.controle.bd.adicionar_comprador(comprador)
        messagebox.showinfo('Sucesso', 'Comprador de CPF ' f'{cpf} adicionado.')

    def remover_comprador(self):
        cpf = self.cpf_remov_entry_var.get()
        remover = None
        if messagebox.askyesno('Excluir', 'Deseja excluir o comprador?') is False:
            return None
        for comprador in self.controle.bd.mostrar_compradores():
            if comprador.get_cpf() == cpf:
                remover = self.controle.bd.remove_comprador(comprador)
                messagebox.showinfo('Concluído', 'O comprador de CPF' f'{cpf} foi removido.')
        if remover is None:
            messagebox.showerror('Erro', 'Não tem comprador com esse CPF')