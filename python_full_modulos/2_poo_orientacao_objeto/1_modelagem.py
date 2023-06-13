# Introdução orientação objeto com Python

# agente modela uma entidade 
# classe é um modelo que descreve os atributos e comportamentos de uma entidade
# objeto é uma instância de uma classe
# classe é um modelo de algo que queremos representar no mundo real

# Exemplo 


class Pessoas():
    # atributos de instancia
    possui_olho = True
    possui_braco = True
    raca = 'Ser humano'
    contador = 0
    

    
    def __init__(self, nome, idade, cpf): 
        Pessoas.contador += 1                     
        self.nome = nome
        self.idade = idade
        self.cpf = cpf 


    def logar_sistema(self):
        print(f'{self.nome} está logando no sistema!')

    

    # Metodos de classes
    @classmethod
    def andar(cls, velocidade):
        print(f"Estou andando na velocidade {velocidade} m/s")
   


p1 = Pessoas('Rogerio', 42, '95733019115') 


# Aqui sem método str, vai mostrar o endereço de memória do objeto
print(p1)


# acessando um atributo especifico do objeto
print(p1.nome)


# acessando um metodo da classe
p1.logar_sistema()



# Acessando atributos de classe 
print(Pessoas.possui_olho)
print(Pessoas.possui_braco)
print(Pessoas.raca)


p2 = Pessoas('marcos', 21, '9999999999999')
p3 = Pessoas('Patrick', 22, '9888888888')
p4 = Pessoas('robson', 22, '9888888888')

print(Pessoas.contador)


# Acessando metodos de classe
Pessoas.andar(100)

# Também consigo acessar um método de classe pela instancia
p1.andar(100)