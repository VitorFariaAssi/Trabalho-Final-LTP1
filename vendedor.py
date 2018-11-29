class Vendedor():
    def __init__(self, nome, idade, cpf, matricula):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def get_cpf(self):
        return self.cpf

    def get_matricula(self):
        return self.matricula