# variaveis de classe e variaveis de instancia

class Estudante:
    # variavel de classe: compartilhada por todos os objetos da classe
    escola = 'IFSP' 

    def __init__(self, nome, idade):
        # variaveis de instancia: unico para cada objeto
        self.nome = nome
        self.idade = idade

estudante1 = Estudante('João', 20)
estudante2 = Estudante('Maria', 22)
print(estudante1.nome)  # João
print(estudante2.nome)  # Maria
print(estudante1.escola)  # IFSP
print(estudante2.escola)  # IFSP

# metodos de classe e metodos estaticos

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

    @classmethod
    def multiplicar(cls, a, b):
        return a * b
print(Matematica.somar(5, 3))  # 8
print(Matematica.multiplicar(5, 3))  # 15

# a diferença entre metodos de classe e metodos estaticos é 
# que os metodos de classe recebem a classe como primeiro parametro (cls) 
# e podem acessar variaveis de classe, 
# enquanto os metodos estaticos nao recebem nenhum 
# parametro especial e nao podem acessar variaveis de classe.

# quando utilizar?
# metodos de classe: quando queremos criar metodos de fabrica ou metodos que precisam acessar ou modificar o estado da classe.
# metodos estaticos: quando queremos criar funcoes utilitarias que nao precisam acessar ou modificar o estado da classe, mas que tem alguma relacao com a classe.

