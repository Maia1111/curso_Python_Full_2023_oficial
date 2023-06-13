# Heranças Multiplas 


class Animal:

    def andar(self):
        print('Andando como animal')
    
    def correr(self):
        print('Correndo como animal')
    
    def pular(self):
        print('Pulando como animal')


class Cachorro(Animal):

    def latir(self):
        print('Latindo como um cachorro')


class Felino(Animal):
    
        def miar(self):
            print('Miando como um felino')


class Gato(Felino):

   def andar(self):
       super().andar()
       print('Andando como um gato')


# instanciando um objeto da classe gato
gato1 = Gato()


# Chamando metodo da classe gato
gato1.andar()

# Chamando metodo que existe somente na classse pai 
gato1.miar()  

# Tendo informações da classe Gato
print(help(Gato))