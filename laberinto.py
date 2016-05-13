import pygame
import random
 
ALTO =500
ANCHO = 700
NEGRO  = (   0,   0,   0)
BLANCO = ( 255, 255, 255)
VERDE  = (   0, 255,   0)
ROJO   = ( 255,   0,   0)
AZUL   = (   0,   0,   255)

class Jugador(pygame.sprite.Sprite):
    muros=None

    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(AZUL)        
        self.rect = self.image.get_rect()
        self.mover_x=0
        self.mover_y=0

    def Mover(self, x,y):
        self.mover_x=x
        self.mover_y=y

    def update(self):
        self.rect.x+=self.mover_x

        choque=pygame.sprite.spritecollide(self, self.muros, False)
	for b in choque:
            if self.mover_x >0:
               self.rect.right=b.rect.left
 	    else:
               self.rect.left=b.rect.right

        self.rect.y+=self.mover_y
	choque=pygame.sprite.spritecollide(self, self.muros, False)
	for b in choque:
            if self.mover_y >0:
               self.rect.bottom=b.rect.top
 	    else:
               self.rect.top=b.rect.bottom
               
        if self.rect.y < 0:
           self.rect.y=ALTO


class Muro(pygame.sprite.Sprite):

    def __init__(self, ancho, alto):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(ROJO)        
        self.rect = self.image.get_rect()

if __name__ == '__main__':
   pygame.init()
   dim=[ANCHO, ALTO]
   pantalla=pygame.display.set_mode(dim)
   pantalla.fill(BLANCO)
   #Definimos tipo de fuente
   fuente = pygame.font.Font(None, 36) 

   ls_muros=pygame.sprite.Group()
   ls_todos=pygame.sprite.Group()

   for i in range(8):
      m=Muro(40,40)
      m.rect.x=random.randrange(0, ANCHO-40)
      m.rect.y=random.randrange(0, ALTO-40)
      ls_muros.add(m)
      ls_todos.add(m)

   
   jugador=Jugador(20,20)
   jugador.rect.x=50
   jugador.rect.y=50
   jugador.muros=ls_muros
   ls_todos.add(jugador)
      
   terminar=False
   fin_juego=False
   reloj=pygame.time.Clock()

   while not terminar:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminar=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               print 'espacio'
               fin_juego=True
            if fin_juego:
               texto=fuente.render("FIN DE JUEGO", True, BLANCO)
  	       pantalla.blit(texto, (250,200))

            if event.key == pygame.K_UP:
	       print 'arriba'
               jugador.Mover(0,-3)
	    if event.key == pygame.K_RIGHT:
	       print 'derecha'
               jugador.Mover(3,0)
            if event.key == pygame.K_DOWN:
               jugador.Mover(0,3)
            if event.key == pygame.K_LEFT:
               jugador.Mover(-3,0)

     pantalla.fill(BLANCO)
     ls_todos.update()
     ls_todos.draw(pantalla)
     reloj.tick(60)
     pygame.display.flip()
     








