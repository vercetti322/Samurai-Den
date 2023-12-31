# resolving imports
import pygame
import sys
from Scripts.entities import PhysicsEntity
from Scripts.utils import load_image, load_images
from Scripts.tilemap import Tilemap
from Scripts.clouds import Clouds

# create the Game class
class Game:
    def __init__(self) -> None:
        # initialise the pygame
        pygame.init()

        # create window/screen
        self.screen = pygame.display.set_mode((640, 480))

        # change window caption
        pygame.display.set_caption('Samurai Den')
        
        # fix player visibility and produce pixelated effect
        self.display = pygame.Surface((320, 240))

        # clocking the game
        self.clock = pygame.time.Clock() 
        
        # movement variable
        self.movement = [False, False]
        
        # image for player
        self.assets = {
            'player': load_image('entities/player.png'),
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
        }
        
        # define our moving player
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
        # defining our tiles
        self.tilemap = Tilemap(self, tile_size=16)
        
        # defining our camera movements
        self.scroll = [0, 0]
        
        # create the clouds for background
        self.clouds = Clouds(self.assets['clouds'], count=16 )

    def run(self):
    # create the game loop to synch with the clock and update the screen
        while True:
            # create a screen color
            self.display.blit(self.assets['background'], (0, 0))
            
            # move the camera
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            # render the clouds first
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)
            
            # render the tilemap
            self.tilemap.render(self.display, offset=self.scroll)
            
            # player movements
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)
                        
            # to prevent exiting of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                        
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                        
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                        
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
        
        
            # blit the display to screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            
            pygame.display.update()
            self.clock.tick(60) # force the loop to run at 60 fps    

# run the Game instance
Game().run()