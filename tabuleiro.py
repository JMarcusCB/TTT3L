from casa import Casa

class Tabuleiro():
    def __init__(self, dim=3, tam=100, cor=(255,255,255)):
        self.dim = dim
        self.tam = tam
        self.cor = cor
        self.lista_casas = []

        self.criar_casas()
    
    def update(self):
        ...

    def draw(self, display):
        for casa in self.lista_casas:
            casa.draw(display)
    
    def criar_casas(self):
        indexador = 0
        for x in range(self.dim):
            for y in range(self.dim):
                    casa = Casa(x+0.05, y+0.05, self.tam, self.tam, self.cor, indexador)
                    self.lista_casas.append(casa)
                    indexador += 1    

    def __str__(self):
        index = []
        for casa in self.lista_casas:
            index.append(casa.x)
            index.append(casa.y)
            index.append(casa.a)
            index.append(casa.l)
            index.append(casa.cor)
            index.append(casa.index)
            index.append(" | ")
        
        return f"{str(index)}"

    @property
    def dim(self):
        return self._dim
    
    @dim.setter
    def dim(self, value):
        if (value >= 0 and value <= 5) and type(value) == int:
            self._dim = value
        else:
            raise ValueError("dimensão invalida")

    def verificar_vencedor(self,a,b,c):
        if self.lista_casas[a].ocupante != "n" and (self.lista_casas[a].ocupante == self.lista_casas[b].ocupante) and \
            (self.lista_casas[b].ocupante == self.lista_casas[c].ocupante):
            return [True, a, b, c]
        else:
            return [False]

        

            
                
        