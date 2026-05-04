# Como criar classes polimorficas em python

# Uma mesma coisa pode ter várias formas (comportamento)

# exemplo:
len("python")
len([1, 2, 3, 4, 5])

# len é um exemplo de polimorfismo, pois pode receber diferentes tipos de dados e retornar o mesmo resultado (o tamanho do objeto)

# Exemplo de polimorfismo com classes
class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"  
    
class Gato(Animal):
    def falar(self):
        return "Miau"
    
def emitir_som(animal):
    print(animal.falar())

cachorro = Cachorro()
gato = Gato()
emitir_som(cachorro)  # Saída: Au Au
emitir_som(gato)      # Saída: Miau 
# O polimorfismo permite que a função emitir_som possa receber qualquer objeto que seja uma instância da classe Animal ou de suas subclasses, sem precisar se preocupar com o tipo específico do objeto.

