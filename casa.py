from pygame import draw
from engine import use_color

class Casa:
    def __init__(self, x, y ,a, l, cor, index, nivel=0):
        self.x = x
        self.y = y
        self.a = a
        self.l = l
        self.cor = cor
        self.nivel = nivel
        self.index = index
        self.ocupante = "n"
        self.vencedora = False

    def __str__(self):
        return f"{self.x, self.y, self.a, self.l, self.cor, self.index, self.nivel}"

    def update(self):
        ...

    def draw(self, display):
        draw.rect(display, self.colorir(self.nivel), ((self.x+0.05)*(self.l + 5), (self.y+0.02)*(self.a + 5), self.a, self.l))

    def colorir(self, nivel):
        if self.vencedora == False:
            match nivel:
                case 1:
                    self.cor = use_color("branco_gelo")
                case 2:
                    #Amarelo
                    self.cor = use_color("amarelo")
                case 3:
                    self.cor = use_color("laranja")
                case _:
                    self.cor = use_color("branco_gelo")
        else:
            self.cor = use_color("purple")
        
        return self.cor
    
    def get_pos(self, ponto=""):
        xi = (self.x+0.05)*(self.l + 5)
        xf = xi + self.l
        yi = (self.y+0.02)*(self.a + 5)
        yf = yi + self.a

        match ponto.lower():
            case "xi":
                return xi 
            case "xf":
                return xf
            case "yi":
                return yi 
            case "yf":
                return yf
            case _:
                return xi,xf,yf,yi

    @property
    def nivel(self):
        return self._nivel

    
    @nivel.setter
    def nivel(self, value):
        try:
            if value >=0 and value <= 3:
                self._nivel = value
            else:
                raise ValueError("Não foi possivel atribuir este valor a variavel \"self.nivel\"")
        except TypeError:
            print("Não foi possivel atribuir uma String a variavel \"self.nivel\". Use um Int entre 1 e 3 inclusive")

    ##
    
    @property
    def ocupante(self):
        return self._ocupante
    
    @ocupante.setter
    def ocupante(self, value):
        self._ocupante = value

        ##
    
    @property
    def vencedora(self):
        return self._vencedora
    
    @vencedora.setter
    def vencedora(self, value):
        self._vencedora = value
