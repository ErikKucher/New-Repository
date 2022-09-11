import pygame
from settings import*

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image_block):
        super().__init__(groups)
        self.image=pygame.image.load(image_block).convert()
        #self.image.fill(TILE_COLOR)
        self.rect=self.image.get_rect(topleft=pos)
class TileO(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image_lava):
        super().__init__(groups)
        self.image=pygame.image.load(image_lava)
        #self.image.fill(TILE_COLORO)
        self.rect=self.image.get_rect(topleft=pos)
class TileF(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image_leaves):
        super().__init__(groups)
        self.image=pygame.image.load(image_leaves)
        #self.image.fill(TILE_COLORF)
        self.rect=self.image.get_rect(topleft=pos)
class TileS(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image_wood):
        super().__init__(groups)
        self.image=pygame.image.load(image_wood)
        #self.image.fill(TILE_COLORS)
        self.rect=self.image.get_rect(topleft=pos)
class TileGrass(pygame.sprite.Sprite):
    def __init__(self,pos,groups,image_grass):
        super().__init__(groups)
        self.image=pygame.image.load(image_grass)
        #self.image.fill(TILE_COLORS)
        self.rect=self.image.get_rect(topleft=pos)

