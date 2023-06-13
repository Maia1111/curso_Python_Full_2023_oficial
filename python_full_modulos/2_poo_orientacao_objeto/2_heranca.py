# Herança em orientação a objeto
# Oque é herança
# Herança é um recurso que permite que classes compartilhem atributos e métodos, afim de reaproveitar código ou comportamento generalizado.

# Vantagens de herança
# Reaproveitamento de código
# Polimorfismo
# Redução de linhas de código
# Aumento de produtividade


# Exemplo de herança

class Pessoa:

    def andar(self):
        print('Estou andando!')
    
    def falar(self):
        print('Estou falando!')


class Cliente(Pessoa):

    def comprar(self):
        print('Estou comprando!')
    
    def falar(self):
        super().falar()
        print('Estou falando como cliente!')

    


class Vendedor(Pessoa):    
    def vender(self):
        print('Estou vendendo!')


c1 = Cliente()
c1.andar()
c1.falar()
c1.comprar()



v1 = Vendedor()
v1.andar()
v1.falar()
v1.vender()

