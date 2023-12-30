# resolving imports
import pygame
from tilemap import Tilemap

# class will handle all the physics
class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def update(self, tilemap, movement = (0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        # move the frame
        self.pos[0] += frame_movement[0] # x dimension
        
        # performing collision
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                
                self.pos[0] = entity_rect.x
            
        self.pos[1] += frame_movement[1] # y dimension
        
        # incorporating acceleration to our velocity
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)
        