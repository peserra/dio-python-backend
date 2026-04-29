# `Herança simples: herda de uma. Multipla: herda de varias

# herança simples
class Veiculo:
    # em comum para todos os veiculos
    # classes filha herdam tudo que tem aqui
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    # sobrescrevendo o constrututor para classe filha
    def __init__(self, cor, placa, numero_rodas, is_eletrico):
        super().__init__(cor, placa, numero_rodas)
        self.is_eletrico = is_eletrico

    def is_carro_eletrico(self):
        return self.is_eletrico
    pass

# herança multipla

class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
        pass
    pass

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    pass

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    pass

class Gato(Mamifero):
    pass

class Quimera(Mamifero, Ave):
    def __str__(self):
        return f"Esta quimera tem: {self.numero_patas} patas, bico da cor {self.cor_bico} e pelo da cor {self.cor_pelo}"


quimera = Quimera(cor_pelo="vermelho", cor_bico = "laranja", numero_patas = 2)
print(quimera)


# teste
class Foo:
    def hello(self):
        print(self.__class__.__name__.lower())

class Bar(Foo):
    def hello(self):
        return super().hello()
    

bar = Bar()
bar.hello