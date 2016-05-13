import os,sys
import pygame 

class Cuadro:
        def __init__(self,rect):
            self.rect = pygame.Rect(rect)
            self.click = False
            self.image = pygame.Surface(self.rect.size).convert()
            self.image.fill((255,0,0))
        def update(self,surface):
            if self.click:
                self.rect.center = pygame.mouse.get_pos()
            surface.blit(self.image,self.rect)

def main(elemento,jugador):
        Juego(jugador)
        elemento.fill(0)
        jugador.update(elemento)

def Juego(Player):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Player.rect.collidepoint(event.pos):
                    Player.click = True
            elif event.type == pygame.MOUSEBUTTONUP:
                Player.click = False
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

