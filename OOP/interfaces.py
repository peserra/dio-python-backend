# O que são interfaces?
# Em programação orientada a objetos, uma interface é um contrato 
# que define um conjunto de métodos que uma classe deve implementar. 
# Ela especifica o comportamento que uma classe deve ter, 
# sem fornecer a implementação desses métodos. 

# As interfaces são usadas para garantir que diferentes classes
# possam ser usadas de maneira intercambiável, 
# desde que implementem a mesma interface. 

# Em python, utilizamos classes abstratas para criar interfaces
# e permite herança múltipla.

# utilizando o modulo abc
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")

