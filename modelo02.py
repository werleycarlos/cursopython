# Vamos começar criando uma classe chamda carro
# Uma classe é um molde ou planta que define como os objetos dessa classe serão
# Ela define o que um objeto pode fazer (os métodos) e o que les tem (os atributos)

class Carro:
    # a classe carro tem dois atributos: "marca" e "modelo". E um método: acelerar.
    # o método especial __init__ é o que chama quando criamos um objeto da classe.
    # ele inicializa os atributos do objeto (marca, modelo)

    def __init__(self, marca, modelo, cor):
        # os atributos do objeto serão definidos dentro do init
        # O self refere-se ao própio  objeto que está sendo criado
        self.modelo = modelo #atributo que armazena o modelo
        self.marca = marca # atributo que armanzena a marca
        self.cor = cor

    # esse é o método que define o comportamento do objeto, aqui estamos falando o que de fato o carro faz
    def acelerar(self):
        print(f"O {self.marca} {self.modelo} está acelerando.")
    
    def parar(self):
         print(f"O {self.marca} {self.modelo} parou.")

    def direita(self):
         print(f"O {self.marca} {self.modelo} {self.cor} virou à direita.")   
    
    def esquerda(self):
         print(f"O {self.marca} {self.modelo} {self.cor} virou à esquerda.")  


carro1 = Carro("Fusca", "1984", "Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.direita()
carro1.esquerda()
carro1.parar()



