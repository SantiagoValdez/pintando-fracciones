#!/usr/bin/env python

import os, pygame,math
import pygame.font, pygame.event, pygame.draw, string
from matrix import *
from pygame.locals import *
from math import sin, cos, pi, sqrt

IMAGES_PATH = 'images/'

class pyGrafic:
	def __init__(self):
		matrix=CreateMatrix(60)
		self.matrix=matrix
		self.rows=matrix.Rows
		self.columns=matrix.Columns		
	
	def init(self):
		#pygame.init()		
		self.screen = pygame.display.set_mode((600, 600),1)
		pygame.display.set_caption('Pintando Fracciones')
		self.cargaImgs()
		self.draw()	
		self.gridRect = pygame.Rect(0,0,50,45)
		self.palet()
		self.color=self.back
		self.colorName='white'
		
	def cargaImgs(self):
		self.purple= pygame.image.load(IMAGES_PATH + "purple.png").convert()
		self.purple.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
		
		self.brown= pygame.image.load(IMAGES_PATH + "brown.png").convert()
		self.brown.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
		
		self.pink= pygame.image.load(IMAGES_PATH + "pink.png").convert()
		self.pink.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
		
		self.orange= pygame.image.load(IMAGES_PATH + "orange.png").convert()
		self.orange.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
		
		self.gray= pygame.image.load(IMAGES_PATH + "gray.png").convert()
		self.gray.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
		
		self.yellow= pygame.image.load(IMAGES_PATH + "yellow.png").convert()
		self.yellow.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
		
		self.blue = pygame.image.load(IMAGES_PATH + "blue.png").convert()
		self.blue.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
	
		self.green = pygame.image.load(IMAGES_PATH + "green.png").convert()
		self.green.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)

		self.red = pygame.image.load(IMAGES_PATH + "red.png").convert()
		self.red.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)

		self.back = pygame.image.load(IMAGES_PATH + "back.png").convert()
		self.back.set_colorkey((0x80, 0x00, 0x80), RLEACCEL)

	def draw(self):
		self.mapimg = pygame.Surface((600,600),1)
		self.mapimg= self.mapimg.convert()
		self.mapimg.fill((0,0,0))
		
		for y in range(self.columns):
			for x in range(self.rows):
				pixelX,pixelY=x*38,y*41
				self.mapimg.blit(self.back,(pixelX,pixelY))

	def setcolor(self, x, y):
		if(x > 561):
			if(y>=0 and y<41):
				self.color=self.red
				self.colorName='red'
			if(y>=41 and y<82):
				self.color=self.green
				self.colorName='green'
			if(y>=82 and y<123):
				self.color=self.blue
				self.colorName='blue'
			if(y>=123 and y<164):
				self.color=self.brown
				self.colorName='brown'
			if(y>=164 and y<205):
				self.color=self.purple
				self.colorName='purple'
			if(y>=205 and y<246):
				self.color=self.yellow
				self.colorName='yellow'
			if(y>=246 and y<287):
				self.color=self.pink
				self.colorName='pink'
			if(y>=287 and y<328):
				self.color=self.orange
				self.colorName='orange'
			if(y>=328 and y<349):
				self.color=self.gray
				self.colorName='gray'

		c=-1
		f=-1
		for row in range(self.rows+1):
			if (x<=(row*38)):
				f=row-1				
				print "column:" + str(f)
				break
		
		for column in range(self.columns+1):
			if (y<=(column*41)):
				c=column-1
				print "row:" + str(c)
				break
		
		if c<self.rows and f<self.columns and c>-1 and f>-1:
			self.matrix.Values[c][f].PaintCell(self.colorName)
			print "Color:" + self.matrix.Values[c][f].GetColor()

		c=c*41
		f=f*38
		if (c>-1 and f>-1):
			self.mapimg.blit(self.color,(f,c))
			pygame.display.flip()

	def palet (self):
		self.mapimg.blit(self.red,(562,0))
		self.mapimg.blit(self.green,(562,41))
		self.mapimg.blit(self.blue,(562,82))
		self.mapimg.blit(self.brown,(562,123))
		self.mapimg.blit(self.purple,(562,164))
		self.mapimg.blit(self.yellow,(562,205))
		self.mapimg.blit(self.pink,(562,246))
		self.mapimg.blit(self.orange,(562,287))
		self.mapimg.blit(self.gray,(562,328))

	def loop(self):    
		pygame.init()
		self.init()
		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						return
				elif event.type is MOUSEBUTTONDOWN:
					if event.button == 1:
						self.setcolor(event.pos[0],event.pos[1])

			self.screen.blit(self.mapimg, (0, 0))
			pygame.display.flip()

def main():

	pygame.init()
	#se inicia el controlador de pygame
	objeto=pyGrafic(matrix)
	objeto.loop()

#se llama a la funcion main cuando se ejecute el scrip
if __name__ == '__main__':
    main()

