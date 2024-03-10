class ContaBancaria:
 def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
 def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de {valor} realizado com sucesso')
        else:
            print('Valor de depósito inválido')

 def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de {valor} realizado com sucesso')
        else:
            print('Saldo insuficiente para saque')

 def exibir(self):
        print(f'Saldo atual: {self.saldo}')

conta1 = ContaBancaria('vitor', '12345')
conta2 = ContaBancaria('bruno', '67890', 900)
conta1.depositar(1200)
conta2.depositar(300)
conta1.sacar(200)
conta2.sacar(800)
conta1.exibir()
conta2.exibir()
