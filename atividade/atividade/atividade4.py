class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular(self):
        return self.base * self.altura

retangulo = Retangulo(5, 8)

area = retangulo.calcular()
print(f'A área do retângulo é: {area}')
