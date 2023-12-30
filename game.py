import pygame
import sys

# create the Game class
class Game:
    def __init__(self) -> None:
        # initialise the pygame
        pygame.init()

        # create window/screen
        self.screen = pygame.display.set_mode((640, 480))

        # change window caption
        pygame.display.set_caption('Samurai Arena')

        # clocking the game
        self.clock = pygame.time.Clock() 
        
        # give the image to blank screen
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        
        # pos
        self.img_pos = [160, 260]
        
        # defining the black color to be transparent
        self.img.set_colorkey((0, 0, 0))
        
        # move the cloud
        self.movement = [False, False]
        
        # defining area for collision detection
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):
    # create the game loop to synch with the clock and update the screen
        while True:
            # create a screen color
            self.screen.fill((14, 219, 248))
             
            # implementing the collision area
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)
                
            # move the object
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5
            
            # load the screen
            self.screen.blit(self.img, self.img_pos)
           
            # to prevent exiting of the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                        
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                        
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
        
            pygame.display.update()
            self.clock.tick(60) # force the loop to run at 60 fps    

# run the Game instance
Game().run()