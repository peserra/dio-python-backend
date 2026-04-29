class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar() -> str:
        print("fon fon")
    
    def correr() -> str:
        print("correndo")

    def parar() -> str:
        print("parando")
    

caloi = bicicleta("azul", "razor", 2020, 600)