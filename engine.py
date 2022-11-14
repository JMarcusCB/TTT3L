import pygame
import verifyEvents

class Engine:
    def __init__(self, width=720, height=480, colorBG=(255,200,200)):
        #FONTS
        pygame.font.init()
        self.fontDict = {}
        
        #CREATE DISPLAY
        self.display = pygame.display.set_mode((width, height))
        self.display_config()
        self.colorBG = colorBG

        #DRAW AND UPADTE LIST
        self.drawList = []
        self.updateList = []
        self.useFunction = []
        
        #MOUSE
        self.mouse_clickList = [False, False, False]
        self.mouse_pressList = [False, False, False]
        self.mouse_position = [0,0]

        self.keyboard_left = False
        self.keyboard_right = False

        self.gameLoopRun = True

    def drawButton(self, btn_color, x, y, x_lenght, y_lenght):
        return pygame.draw.rect(self.display, use_color(btn_color), (x, y, x_lenght, y_lenght))

    def addToFonteDict(self, font_name, font_type="Comic Sans MS", font_size="30"):
        self.fontDict[font_name] = pygame.font.SysFont(font_type, font_size) 
    
    def drawText(self, font_name, font_color, text, x, y ):
        self.display.blit(self.fontDict[font_name].render(text, 1, use_color(font_color)), (x, y))

    def display_config(self, title="Display", color=(255,200,200)):
        self.display.fill(color)
        pygame.display.set_caption(title)
        self.colorBG = color

    def addToUpdateList(self, obj):
        self.updateList.append(obj)

    def update(self):
        for obj in self.updateList:
            obj.update()

    def addToDrawList(self, obj):
        self.drawList.append(obj)

    def draw(self):
        for obj in self.drawList:
            obj.draw(self.display)

        pygame.display.flip()
    
    def disableClicks(self):
        for i in range(len(self.mouse_clickList)):
            self.mouse_clickList[i] = False

    def verifyEvents(self):
        for event in pygame.event.get():      
            verifyEvents.QUIT_verify(self, event)
            verifyEvents.MOUSEBUTTONDOWN_verify(self, event)
            verifyEvents.MOUSEBUTTONUP_verify(self, event)

            verifyEvents.KEYDOWN_verify(self, event) # Verifica apenas as teclas arrow_Left(K_LEFT) e arrow_Right(K_RIGHT)

    def get_mousePosition(self):
        mx,my = pygame.mouse.get_pos()
        self.mouse_position[0] = mx
        self.mouse_position[1] = my
    
    def addFunction(self, function):
        self.useFunction.append(function)

    def rulesGame(self):
        for function in self.useFunction:
            function()

    def gameLoop(self):
        while self.gameLoopRun:
            self.disableClicks()
            self.keyboard_left = False
            self.keyboard_right = False
            self.verifyEvents()
            self.get_mousePosition() 
            self.rulesGame()
            self.draw()
            self.update()


def use_color(color_name):
    try:
        match color_name.lower():
            case "vinho":
                return (69, 38, 50)
            case "purple":
                return (145, 32, 77)
            case "laranja":
                return (228, 132, 74)
            case "amarelo":
                return (232, 191, 86)
            case "cinza":
                return (100, 100, 100)
            case "branco_gelo":
                return (226, 247, 206)
            case "vermelho":
                return (255, 50, 50)
            case "verde":
                return (50, 255, 50)
            case "cinza":
                return (112,112,112)
            case _:
                raise ValueError("Nome de cor Inválido. consultar \"def catalogo_cores\"") 
    except AttributeError:
        raise ValueError("Nome de cor Inválido(Utilize uma string). consultar \"def catalogo_cores\"")

    
