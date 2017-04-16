from Mash.Character import Character
from Mash.Map import Map
import pygame


class Game(object):

    m = 1
    c = 1

    frame_rate = 30


    def __init__(self):
        print('cool')

    def set_map(self, m):
        self.m = m

    def set_main_character(self, c):
        self.c = c

    def set_frame_rate(self, x):
        self.frame_rate = x

    def start_game(self):

        def checkCentered(coordinate, panelLength):# object_mod):
            return coordinate == int(panelLength / 2)# + (object_mod/2)


        def future_char_coor(x_centered, y_centered, deltax, deltay, c_x, c_y):

            if x_centered:
                x = abs(background_x) + int(window_width/2)
            else:
                x = abs(background_x) + int(window_width / 2)
                adder = c_x + abs(background_x) - x
                x += adder
            if y_centered:
                y = abs(background_y) + int(window_height/2)
            else:
                y = abs(background_y) + int(window_height/2)
                adder = c_y + abs(background_y) - y
                y += adder

            l = [x + deltax, y + deltay]
            return l


        speed = self.c.speed
        pygame.init()
        window_width = 600
        window_height = 600
        game_display = pygame.display.set_mode((window_width, window_height))
        background_x = 0
        background_y = 0
        background = pygame.image.load(self.m.entire_map)
        preload_background = pygame.transform.scale(background, (self.m.map_total_width, self.m.map_total_height))
        game_display.blit(preload_background, (background_x, background_y))
        c_x = int(window_width / 2) #- (int(self.c.width / 2))
        c_y = int(window_height / 2) #- int(self.c.height / 2)
        game_display.blit(self.c.front_anim[0], (c_x, c_y))
        pygame.display.update()
        game_over = False
        clock = pygame.time.Clock()
        animation_counter = 0
        key = "front"
        x_centered = True
        y_centered = True
        while not game_over:

            x_centered = checkCentered(c_x, window_width)#int(float(self.c.width)/2))
            y_centered = checkCentered(c_y, window_height)#int(float(self.c.height)/2))
            keys = pygame.key.get_pressed()

            if keys[pygame.K_DOWN]:
                key = "front"
                if abs(background_y) < self.m.map_total_height - window_height and y_centered:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, 0, -speed, c_x, c_y)):
                        background_y -= speed
                elif c_y < window_height - self.c.height - speed:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, 0, -speed, c_x, c_y)):
                        c_y += speed

            if keys[pygame.K_UP]:
                key = "back"
                if background_y < -speed and y_centered:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, 0, -speed, c_x, c_y)):
                        background_y += speed
                elif c_y > speed-(self.c.height/2):
                    if not self.m.collide(future_char_coor(x_centered, y_centered, 0, -speed, c_x, c_y)):
                        c_y -= speed

            if keys[pygame.K_LEFT]:
                key = "left"
                if background_x < -speed and x_centered:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, speed, 0, c_x, c_y)):
                        background_x += speed
                elif c_x > speed:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, speed, 0, c_x, c_y)):
                        c_x -= speed


            if keys[pygame.K_RIGHT]:
                key = "right"
                if abs(background_x) < self.m.map_total_width - window_width and x_centered:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, -speed, 0, c_x, c_y)):
                        background_x -= speed
                elif c_x < window_width - self.c.width - speed:
                    if not self.m.collide(future_char_coor(x_centered, y_centered, -speed, 0, c_x, c_y)):
                        c_x += speed



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True


            game_display.blit(preload_background, (background_x, background_y))
            game_display.blit(self.c.glued_preload[key][animation_counter], (c_x, c_y))
            pygame.display.update()
            clock.tick(self.frame_rate)









