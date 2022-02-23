#exerciocio de class -> dado uma pessoa que informa o nome e idade, diga qual o ano que ela nasceu a partir do ano atual


class Pessoa:
    def __init__(self, nome, idade, ano_atual):
        self.nome = nome
        self.idade = idade
        self.ano = ano_atual
    
    def idade_pessoa (self):
        return self.ano - self.idade
    
    def nome_pessoa (self):
        print(self.nome)


pessoa = Pessoa('Silvio', 25, 2020)

print(pessoa.nome_pessoa())
print(pessoa.idade_pessoa())