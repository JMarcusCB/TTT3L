import pygame

def QUIT_verify(self, event):
    if event.type == pygame.QUIT:
        self.gameLoopRun == False
        pygame.quit()
        quit()
    
def MOUSEBUTTONDOWN_verify(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        #LEFT BUTTON
        if event.button == 1:
            self.mouse_clickList[0] = True
            self.mouse_pressList[0] = True
        #MIDDLE BUTTON
        if event.button == 2:
            self.mouse_clickList[1] = True
            self.mouse_pressList[1] = True
        #RIGHT BUTTON
        if event.button == 3:
            self.mouse_clickList[2] = True
            self.mouse_pressList[2] = True

def MOUSEBUTTONUP_verify(self, event):
    if event.type == pygame.MOUSEBUTTONUP:
        #LEFT BUTTON
        if event.button == 1:
            self.mouse_pressList[0] = False
        #MIDDLE BUTTON
        if event.button == 2:
            self.mouse_pressList[1] = False
        #RIGHT BUTTON
        if event.button == 3:
            self.mouse_pressList[2] = False

def KEYDOWN_verify(self, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            self.keyboard_left = True

        if event.key == pygame.K_RIGHT:
            self.keyboard_right = True
             