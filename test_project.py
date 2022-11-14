from engine import use_color
import casa
from project import Jogo
from player import Bola
import pytest

def tests():
    def test_usecolor():
        assert use_color("vinho") == (69, 38, 50)
        assert use_color("VINHO") == (69, 38, 50)

        with pytest.raises(ValueError):
            use_color("v")  

        with pytest.raises(ValueError):
            use_color(0)

    def test___str__():
        c1 = casa.Casa(10, 10 ,10, 10, "cinza", 0, 0)
        assert c1.__str__() == "(10, 10, 10, 10, 'cinza', 0, 0)"

        c2 = casa.Casa(10, 10 ,10, 10, "cinza", 0, "1")
        with pytest.raises(AttributeError):
            assert c2.__str__() 

    def test_vizualizar_volta():
        j1 = Jogo()
        c1 = casa.Casa(10, 10 ,10, 10, "cinza", 0, 3)
        b1 = Bola(10, 10, "cinza", c1)

        assert j1.vizualizar_volta(b1) == 0

        with pytest.raises(AttributeError):
            j1.vizualizar_volta(c1)
            j1.vizualizar_volta(1)
            j1.vizualizar_volta("CS50'P")

if __name__ == "__main_":
    tests()