import pygame
from tile import*
from settings import *
pygame.init()

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,groups,collision_sprites,image1):
		super().__init__(groups)
		self.image = pygame.image.load(image1).convert()
		self.images = []
		self.images.append(pygame.image.load('img_2.png').convert())
		self.images.append(pygame.image.load('img_3.png').convert())

		#(TILE_SIZE // 2, TILE_SIZE)
		#self.image.fill(PLAYER_COLOR)
		self.rect = self.image.get_rect(topleft = pos)

		# player movement
		self.direction = pygame.math.Vector2()
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = 16
		self.collision_sprites = collision_sprites
		self.on_floor = False

	def input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			#image1='img_3.png'
			self.direction.x = 1

		elif keys[pygame.K_LEFT]:
			#image1='img.png'
			self.direction.x = -1
		else:
			self.direction.x = 0

		if keys[pygame.K_SPACE] and self.on_floor:
			self.direction.y = -self.jump_speed

	def horizontal_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.x < 0:
					self.rect.left = sprite.rect.right
				if self.direction.x > 0:
					self.rect.right = sprite.rect.left

	def vertical_collisions(self):
		for sprite in self.collision_sprites.sprites():
			if sprite.rect.colliderect(self.rect):
				if self.direction.y > 0:
					self.rect.bottom = sprite.rect.top
					self.direction.y = 0
					self.on_floor = True
				if self.direction.y < 0:
					self.rect.top = sprite.rect.bottom
					self.direction.y = 0

		if self.on_floor and self.direction.y != 0:
			self.on_floor = False

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def update(self):
		keys = pygame.key.get_pressed()
		self.input()
		self.rect.x += self.direction.x * self.speed
		self.horizontal_collisions()
		self.apply_gravity()
		self.vertical_collisions()
		if keys[pygame.K_RIGHT]:
			self.image=self.images[1]
		elif keys[pygame.K_LEFT]:
			self.image=self.images[0]
		#hits = pygame.sprite.spritecollide(self.rect, TileO, False)





