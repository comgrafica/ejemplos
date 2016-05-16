'''
Ejemplo de menu
autor: Carlos Andres Lopez
correo: asrael@utp.edu.co
'''

import pygame

# Constantes

# Colores
NEGRO   = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO      = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO  = 750
ALTO = 600

class Menu():

	color=BLANCO
	fondo=NEGRO
	espacio=30
	titulo_x, titulo_y=200,200
	pos_titulo=(titulo_x, titulo_y)
	opciones=[]
	pos_op=1


	def __init__(self):
		self.fuente = pygame.font.Font(None, 36)
		self.nop=1
		self.seleccion=0

	def abajo(self):
		self.nop+=1
		if self.nop > len(self.opciones):
			self.nop=1

	def arriba(self):
		self.nop-=1
		if self.nop <= 0:
			self.nop=len(self.opciones)


	def draw(self, pantalla):
		self.texto=self.fuente.render('Menu',True,self.color)
		pantalla.blit(self.texto, self.pos_titulo)
		i=1
		for op in self.opciones:
			self.texto=self.fuente.render(op,True,self.color)
			pantalla.blit(self.texto, [self.titulo_x, self.titulo_y+(self.espacio*i)])
			if self.nop==i:
				pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
				pygame.draw.circle(pantalla, self.color, pos, 5, 0)
			else:
				pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
				pygame.draw.circle(pantalla, self.fondo, pos, 5, 0)
			i+=1


if __name__=='__main__':
	""" Programa principal """
	pygame.init()
	tam = [ANCHO, ALTO]
	pantalla = pygame.display.set_mode(tam)
	pygame.display.set_caption("Ejemplo de menu")
	menu=Menu()
	opciones=['Nuevo', 'Continuar', 'Salir']
	menu.opciones=opciones
	fin=False
	reloj = pygame.time.Clock()

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					print 'abajo'
					menu.abajo()
				if event.key == pygame.K_UP:
					print "arriba"
					menu.arriba()
				if event.key == pygame.K_RETURN:
					menu.seleccion=menu.nop
					print 'seleccion'

		print 'opcion: ', menu.nop

		
		if menu.seleccion==3:
			menu.seleccion=0
			fin=True
		
		reloj.tick(60)
		menu.draw(pantalla)
		pygame.display.flip()