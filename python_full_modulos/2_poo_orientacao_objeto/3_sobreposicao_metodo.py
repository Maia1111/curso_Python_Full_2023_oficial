class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf    

    def andar(self):
        print('Estou andando!')
            
    def falar(self):
        print('Estou falando!')



class Cliente(Pessoa):

    def __init__(self, id_cliente, nome, cpf):

        super().__init__(nome, cpf)
        self.id_cliente = id_cliente
        

    def comprar(self):
        print('Estou comprando!')
    
    def falar(self):
        super().falar()
        print('Estou falando como cliente!')

    


class Vendedor(Pessoa):    
    def vender(self):
        print('Estou vendendo!')



c1 = Cliente(1, 'Manoe', '999999999')
c1.andar()
c1.falar()
c1.comprar()