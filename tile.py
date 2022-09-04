import pygame
from settings import*

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image=pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLOR)
        self.rect=self.image.get_rect(topleft=pos)
class TileO(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image=pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLORO)
        self.rect=self.image.get_rect(topleft=pos)
class TileF(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image=pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLORF)
        self.rect=self.image.get_rect(topleft=pos)
class TileS(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image=pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image.fill(TILE_COLORS)
        self.rect=self.image.get_rect(topleft=pos)

