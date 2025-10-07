class Gato:
    def __init__(self, nome, idade, genero, peso, cor):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.peso = peso
        self.cor = cor
    def andar(self):
        print(f"o {self.nome} de {self.idade} foi andar")
    def saltar(self):
        print(f"o {self.genero} {self.nome} que pesa {self.peso} saltou")
    def comer(self):
        print(f"o {self.nome} de cor {self.cor} comeu muito")
class Cão:
    def __init__(self, nome, idade, genero, peso, cor):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.peso = peso
        self.cor = cor
    def andar(self):
        print(f"o {self.nome} de {self.idade} foi andar")
    def saltar(self):
        print(f"o {self.genero} {self.nome} que pesa {self.peso} saltou")
    def comer(self):
        print(f"o {self.nome} de cor {self.cor} comeu muito")

c1 =Cão("rufus",3,"rapaz",23,"amarelo")
c2 =Cão("daniela",5,"rapariga",40,"rosa")
g1=Gato("destroyer",6,"rapaz",5,"laranja")
g2=Gato("Daisy",7,"rapariga",10,"malhada")
c1.andar()
c2.comer()
g1.saltar()
g2.andar()