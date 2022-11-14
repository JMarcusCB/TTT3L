from pygame import draw
class Player:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, value):
        self._cor = value

    def __str__(self):
        return f"{self.casa.index}"

class Bola(Player):
    def __init__(self, x, y, cor, casa):
        super().__init__(x, y, cor)
        self.casa = casa

    def draw(self, display):
        draw.circle(display ,self.cor, ( ((self.casa.x+0.05)*(self.casa.l + 5))+(self.casa.l/2), ((self.casa.y+0.02)*(self.casa.a + 5))+(self.casa.l/2) ), self.casa.l/2.3)
        draw.circle(display ,self.casa.cor, ( ((self.casa.x+0.05)*(self.casa.l + 5))+(self.casa.l/2), ((self.casa.y+0.02)*(self.casa.a + 5))+(self.casa.l/2) ), self.casa.l/3)        

class Xis(Player):
    def __init__(self, x, y, cor, casa,tam=10):
        super().__init__(x, y, cor)
        self.tam = tam
        self.casa = casa
    

    def draw(self, display):
        draw.line(display, self.cor, (self.casa.get_pos("xi") + 15, self.casa.get_pos("yi") + 15), (self.casa.get_pos("xf") - 15, self.casa.get_pos("yf") - 15), 10)
        draw.line(display, self.cor, (self.casa.get_pos("xf") - 15, self.casa.get_pos("yi") + 15), (self.casa.get_pos("xi") + 15, self.casa.get_pos("yf") - 15), 10)
        pass

    def __str__(self):
        return f"{self.casa.index}"
