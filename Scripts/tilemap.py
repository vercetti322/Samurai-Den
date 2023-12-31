# resolving imports
import pygame

# collisions from neighbours
NEIGHBOUR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'grass', 'stone'}

class Tilemap:
    def __init__(self, game,  tile_size=16):
        self.tile_size = tile_size
        self.tilemap = {}
        self.game = game
        self.offgrade_tiles = []
        
        # creating some tiles
        for i in range(10):
            self.tilemap[str(i + 3) + ';10'] = {'type' : 'grass', 'variant' : 1, 'pos' : (3 + i, 10)}
            self.tilemap[';10' + str(i + 5)] = {'type' : 'stone', 'variant' : 1, 'pos' : (10, i + 5)}
            
    # render the tiles
    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrade_tiles:
            surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))
        
        for x in range(int(offset[0] // self.tile_size), int((offset[0] + surf.get_width()) // self.tile_size + 1)):
            for y in range(int(offset[1] // self.tile_size), int((offset[1] + surf.get_height()) // self.tile_size + 1)):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))
      
        # # we want the offgrade_tiles to go first as they will be rendered behind our main tilemap
        # for loc in self.tilemap:
        #     tile = self.tilemap[loc]
              
    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOUR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
