class cachorro :
    def __init__(self, nome, idade, ):
     self.idade = idade
     self.nome = nome
    
    def latir(self):
     print('latindo...')
     
dog = cachorro ('7', 'boby', )

print(dog.idade)
print(dog.nome)
dog.latir()