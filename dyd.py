import os,sys
import pygame 

ROJO=(255,0,0)

class Cuadro:
        def __init__(self,rect):
            self.rect = pygame.Rect(rect)
            self.click = False
            self.image = pygame.Surface(self.rect.size).convert()
            self.image.fill(ROJO)

        def update(self,surface):
            if self.click:
                self.rect.center = pygame.mouse.get_pos()
            surface.blit(self.image,self.rect)

def main(pantalla,cuadro):
        #Captura de teclas
        Juego(cuadro)
        pantalla.fill(0)
        cuadro.update(pantalla)

def Juego(cuadro):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cuadro.rect.collidepoint(event.pos):
                    cuadro.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                cuadro.click = False
            elif event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

if __name__ == "__main__":
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pantalla = pygame.display.set_mode((1000,600))
        reloj = pygame.time.Clock()
        cuadro = Cuadro((0,0,150,150))
        cuadro.rect.center = pantalla.get_rect().center
        while 1:
            main(pantalla,cuadro)
            pygame.display.update()
            reloj.tick(60)
