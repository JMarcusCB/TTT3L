import engine
import tabuleiro
from replays import *
from player import Bola, Xis

class Jogo():
    def __init__(self):
        self.navegadorLimit = 0
        self.navegador = 0
        self.totSaves = 5
        self.mostrador = 1
        self.turno = "o"
        self.fim_de_jogo = False

        self.gameNote = []
        self.winCasas = []

        self.tabuleiro = tabuleiro.Tabuleiro(tam=150,cor=(255, 255, 255))
        self.eng = engine.Engine(600,480)
    
    def limpar_tabuleiro(self):
        for casa in self.tabuleiro.lista_casas:
                casa.vencedora = False
                casa.ocupante = "n"
                casa.nivel = 0

        while len(self.eng.drawList) > 1:
            for b in self.eng.drawList:
                if type(b) == Bola:
                    self.eng.drawList.remove(b)
                    self.gameNote.remove(b)

            for x in self.eng.drawList:
                if type(x) == Xis:
                    self.eng.drawList.remove(x)
                    self.gameNote.remove(x)

        self.fim_de_jogo = False  
        self.navegador = 0 
        self.navegadorLimit = 0
        self.winCasas *= 0
        self.gameNote *= 0
        
    def capitar_click(self):
        if self.eng.mouse_clickList[0] == True and self.fim_de_jogo == False and self.navegador == self.navegadorLimit:
            for casa in self.tabuleiro.lista_casas:
                click_valido = False
                if self.eng.mouse_position[0] > casa.get_pos("xi") and self.eng.mouse_position[0] < casa.get_pos("xf") and \
                self.eng.mouse_position[1] > casa.get_pos("yi") and self.eng.mouse_position[1] < casa.get_pos("yf"):
                    click_valido = True

                if click_valido == True and self.turno =="o" and \
                    casa.nivel <= 2 and (casa.ocupante == "n" or casa.ocupante == "x"):
                        self.turno = "x" 
                        casa.ocupante = "o"
                        if casa.nivel <=3:
                            casa.nivel += 1
                        bola = Bola(casa.x, casa.y, (0,0,0), casa)
                        #eng.addToDrawList(bola)
                        self.gameNote.append(bola)
                        self.navegador += 1
                        
                elif click_valido == True and self.turno =="x" and \
                    casa.nivel <= 2 and (casa.ocupante == "n" or casa.ocupante == "o"):
                        self.turno = "o"
                        casa.ocupante = "x"
                        if casa.nivel <=3:
                            casa.nivel += 1
                        xis = Xis(casa.x, casa.y, (0,0,0), casa)
                        #eng.addToDrawList(xis)
                        self.gameNote.append(xis)
                        self.navegador += 1

    def fim_jogo(self):
        dim = self.tabuleiro.dim * self.tabuleiro.dim
        casas = list()
        if self.fim_de_jogo == False and len(self.winCasas) < 1:
            #solução Complexa
            for i in range(0, self.tabuleiro.dim):
                casas *= 0
                count = 0
                for j in range(i, dim, self.tabuleiro.dim):
                    if count < self.tabuleiro.dim:
                        casas.append(j)
                        count += 1

                if count == self.tabuleiro.dim:
                    res = self.tabuleiro.verificar_vencedor(casas[0],casas[1],casas[2])
                    if res[0] == True:
                        self.fim_de_jogo = True
                        self.winCasas.append(res[1:])
                        return 

            for i in range(0, self.tabuleiro.dim):
                casas *= 0
                count = 0
                for j in range(i* self.tabuleiro.dim, (self.tabuleiro.dim)+i*3):
                    if count < self.tabuleiro.dim:
                        casas.append(j)
                        count += 1

                if count == self.tabuleiro.dim:
                    res = self.tabuleiro.verificar_vencedor(casas[0],casas[1],casas[2])
                    if res[0] == True:
                        self.fim_de_jogo = True
                        self.winCasas.append(res[1:])
                        return

            #solução simples
            if res := self.tabuleiro.verificar_vencedor(0,4,8):
                if res[0] == True:
                    self.fim_de_jogo = True
                    self.winCasas.append(res[1:])
                    return
            
            if res := self.tabuleiro.verificar_vencedor(6,4,2):
                if res[0] == True:
                    self.fim_de_jogo = True
                    self.winCasas.append(res[1:])
                    return

        return self.winCasas          

    def drawWinLine(self):
        if len(self.winCasas) > 0:
            #CasaVencendor[0] -> [ '[a, b, c]' ]
            casasVencedora = self.winCasas

            for casa in self.tabuleiro.lista_casas:
                if casa.index in casasVencedora[0] and self.navegador == self.navegadorLimit:
                    casa.vencedora = True
                elif casa.index in casasVencedora[0] and self.navegador != self.navegadorLimit: 
                    for casa in self.tabuleiro.lista_casas:
                        casa.vencedora = False
        else:
            for casa in self.tabuleiro.lista_casas:
                casa.vencedora = False

    def logica_restart_button(self):
        if len(self.eng.drawList) > 2 and \
            self.eng.mouse_clickList[0] == True and self.eng.mouse_position[0] > 480 and self.eng.mouse_position[0] < 480+110 \
            and self.eng.mouse_position[1] > 10 and self.eng.mouse_position[1] < 10+50:

            self.limpar_tabuleiro() 

    def save(self):
        if self.fim_de_jogo == True and self.eng.mouse_clickList[0] == True \
            and self.eng.mouse_position[0] > 480 and self.eng.mouse_position[0] < 480+110 \
            and self.eng.mouse_position[1] > 70 and self.eng.mouse_position[1] < 70+50\
            and self.mostrador > 0:
            #gameNt = gameNote
            marcadorFree = fileToGamenote(self.mostrador)
            if marcadorFree == "free":
                saveFile(self.mostrador, self.gameNote)
                self.limpar_tabuleiro()

    def addBXToDrawList(self):
        index = self.navegador
        for bx in self.gameNote[:self.navegador]:
            if bx not in self.eng.drawList:
                self.eng.addToDrawList(bx)
            index -= 1   

        index = 0
        for bx in self.eng.drawList:
            if type(bx) == Bola or type(bx) == Xis:
                if index > self.navegador:
                    self.eng.drawList.remove(bx)
            index += 1

    def retroceder(self):
        if self.eng.mouse_clickList[2] == True and self.navegador == self.navegadorLimit:
            self.fim_de_jogo = False
            if len(self.gameNote) > 0:
                bx = self.gameNote.pop()
                self.eng.drawList.pop()
                self.winCasas *= 0
                self.navegadorLimit -= 1
                self.navegador = self.navegadorLimit

                if bx.casa.ocupante == "x" and bx.casa.nivel > 1:
                    bx.casa.nivel -= 1
                    bx.casa.ocupante = "o"
                    self.turno = "x"
                    return
                elif bx.casa.ocupante == "o" and bx.casa.nivel > 1:
                    bx.casa.nivel -= 1
                    bx.casa.ocupante = "x"
                    self.turno = "o"
                    return

                if bx.casa.ocupante == "x" and bx.casa.nivel <=1:
                    bx.casa.nivel -= 1
                    bx.casa.ocupante = "n"
                    self.turno = "x"
                    return
                elif bx.casa.ocupante == "o" and bx.casa.nivel <= 1:

                    bx.casa.nivel -= 1
                    bx.casa.ocupante = "n"
                    self.turno = "o"
                    return
                
                return

    def logica_mostrador(self):
        if self.eng.mouse_clickList[0] == True \
            and self.eng.mouse_position[0] > 480 and self.eng.mouse_position[0] < 480+110 \
            and self.eng.mouse_position[1] > 130 and self.eng.mouse_position[1] < 130+50:
            if self.mostrador < self.totSaves:
                self.mostrador += 1
        
        if self.eng.mouse_clickList[0] == True \
            and self.eng.mouse_position[0] > 480 and self.eng.mouse_position[0] < 480+110 \
            and self.eng.mouse_position[1] > 240 and self.eng.mouse_position[1] < 240+50:
            if self.mostrador > 1:
                self.mostrador -= 1
        
        mostradorFree = fileToGamenote(self.mostrador)
        if self.mostrador == 0: 
            #pygame.draw.rect(eng.display, engine.use_color("cinza"), (495, 185, 80,50))
            self.eng.drawButton("cinza", 495, 185, 80, 50)
            self.eng.drawText("font_comicsans", "purple", str(self.mostrador), 495+30, 188)
        elif mostradorFree == "free" and self.mostrador > 0:
            #pygame.draw.rect(eng.display, engine.use_color("cinza"), (495, 185, 80,50))
            self.eng.drawButton("cinza", 495, 185, 80, 50)
            self.eng.drawText("font_comicsans", "purple", str(self.mostrador), 495+30, 188)
        elif mostradorFree != "free" and self.mostrador > 0:
            #pygame.draw.rect(eng.display, engine.use_color("verde"), (495, 185, 80,50))
            self.eng.drawButton("verde", 495, 185, 80, 50)
            self.eng.drawText("font_comicsans", "purple", str(self.mostrador), 495+30, 188)

    def logica_watch(self):
        #watch
        if self.eng.mouse_clickList[0] == True \
            and self.eng.mouse_position[0] > 480 and self.eng.mouse_position[0] < 480+110 \
            and self.eng.mouse_position[1] > 300 and self.eng.mouse_position[1] < 300+50:
            if self.mostrador != 0:
                #LER ARQUIVO E TRANSFORMAR EM ARRAY
                newGameNote = fileToGamenote(self.mostrador)
                if newGameNote != "free":
                    self.limpar_tabuleiro()
                    for i in range(len(newGameNote)):
                        casa = int(newGameNote[i])
                        if i%2 == 0:  
                            bola = Bola(self.tabuleiro.lista_casas[casa].x, self.tabuleiro.lista_casas[casa].y, (0,0,0), self.tabuleiro.lista_casas[casa])
                            self.tabuleiro.lista_casas[casa].ocupante = "o"
                            self.tabuleiro.lista_casas[casa].nivel += 1
                            self.turno = "x"
                            self.eng.drawList.append(bola)
                            self.gameNote.append(bola)
                        else: 
                            xis = Xis(self.tabuleiro.lista_casas[casa].x, self.tabuleiro.lista_casas[casa].y, (0,0,0), self.tabuleiro.lista_casas[casa])
                            self.tabuleiro.lista_casas[casa].ocupante = "x"
                            self.tabuleiro.lista_casas[casa].nivel += 1
                            self.turno = "o"
                            self.eng.drawList.append(xis)
                            self.gameNote.append(xis)
                            self.navegadorLimit = len(newGameNote)
                    self.navegador = len(newGameNote) # -\n
                    self.navegadorLimit = len(newGameNote)
            self.fim_jogo()

    def logica_delete(self):
        #DELETE
        if self.eng.mouse_clickList[0] == True \
            and self.eng.mouse_position[0] > 480 and self.eng.mouse_position[0] < 480+110 \
            and self.eng.mouse_position[1] > 360 and self.eng.mouse_position[1] < 360+50:
            if self.mostrador >= 1:
                #AJUSTAR SAVES NO ARQUIVO
                removeGamenote(self.mostrador)

    def update_navegador(self):
        self.navegadorLimit = len(self.gameNote)

        if self.eng.keyboard_left == True and self.navegador > 1:
            self.vizualizar_volta(self.gameNote[self.navegador-1])
            self.navegador -= 1
            return

        elif self.eng.keyboard_right == True and self.navegador < self.navegadorLimit:
            self.vizualizar_avanco(self.gameNote[self.navegador])
            self.navegador += 1
            return

    def vizualizar_avanco(self, bx):
        bx.casa.nivel += 1
        return 0

    def vizualizar_volta(self, bx):
        bx.casa.nivel -= 1
        return 0
 
    def main(self):
        print("============================================================")
        print(f"\nNaveg Limit -> {self.navegadorLimit}\
                \nNavegador   -> {self.navegador}\
                \nTotsaves    -> {self.totSaves}\
                \nMostrador   -> {self.mostrador}\
                \nTurno       -> {self.turno}\
                \nFim de Jogo -> {self.fim_de_jogo}\
\
                \ngameNote -> {len(self.gameNote)}\
                \nWincasas -> {len(self.winCasas)}\
                \nTabuleirocasas -> {len(self.tabuleiro.lista_casas)}\
                \nDrawList -> {len(self.eng.drawList)}")
        print("============================================================")
        print()
        self.eng.addToFonteDict("font_comicsans", "Comic Sans MS", 30)

        readLine(self.totSaves)
        self.eng.display_config("TTT3L", color = engine.use_color("vinho"))
        self.eng.addToDrawList(self.tabuleiro)
        self.eng.addFunction(self.fim_jogo)
        self.eng.addFunction(self.capitar_click)
        self.eng.addFunction(self.retroceder)
        self.eng.addFunction(self.save)
        self.eng.addFunction(self.logica_watch)
        self.eng.addFunction(self.logica_delete)
        self.eng.addFunction(self.logica_mostrador)
        self.eng.addFunction(self.logica_restart_button)
        self.eng.addFunction(self.update_navegador)
        self.eng.addFunction(self.addBXToDrawList)
        self.eng.addFunction(self.drawWinLine)
        

        print("============================================================")
        print(f"\nNaveg Limit -> {self.navegadorLimit}\
                \nNavegador   -> {self.navegador}\
                \nTotsaves    -> {self.totSaves}\
                \nMostrador   -> {self.mostrador}\
                \nTurno       -> {self.turno}\
                \nFim de Jogo -> {self.fim_de_jogo}\
\
                \ngameNote -> {len(self.gameNote)}\
                \nWincasas -> {len(self.winCasas)}\
                \nTabuleirocasas -> {len(self.tabuleiro.lista_casas)}\
                \nDrawList -> {len(self.eng.drawList)}")
        print("============================================================")
        print()
        

        # BOTAO DE RESTART
        self.eng.drawButton("laranja", 480, 10, 110, 50)
        self.eng.drawText("font_comicsans", "purple", "Restart", 480, 10)

        #BOTAO DE SAVE
        self.eng.drawButton("laranja", 480, 70, 110, 50)
        self.eng.drawText("font_comicsans", "purple", "Save", 500, 70)

        #BOTAO UP
        self.eng.drawButton("laranja", 480, 130, 110, 50)
        self.eng.drawText("font_comicsans", "purple", "->", 520, 130)

        #MOSTRADOR


        #BOTAO DOWN
        self.eng.drawButton("laranja", 480, 240, 110, 50)
        self.eng.drawText("font_comicsans", "purple", "<-", 520, 240)

        #watch
        self.eng.drawButton("verde", 480, 300, 110, 50)
        self.eng.drawText("font_comicsans", "branco_gelo", "watch", 495, 300)

        #DELETE
        self.eng.drawButton("vermelho", 480, 360, 110, 50)
        self.eng.drawText("font_comicsans", "branco_gelo", "delete", 490, 360)

        self.eng.gameLoop()       

if __name__ == "__main__":
    j = Jogo()
    j.main()
