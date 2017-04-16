import pygame


class Character(object):

    width = 0
    height = 0
    x = 0
    y = 0

    speed = 10

    left_anim = []
    left_anim_num = 0

    right_anim = []
    right_anim_num = 0

    front_anim = []
    front_anim_num = 0

    back_anim = []
    back_anim_num = 0

    glued_preload = {}

    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        #just incase no set_animation is ever called
        self.set_animation_back(["spoongey.png"])
        self.set_animation_front(["spoongey.png"])
        self.set_animation_left(["spoongey.png"])
        self.set_animation_right(["spoongey.png"])



    def move_x(self, delta):
        self.x += delta

    def move_y(self, delta):
        self.y += delta


    def set_animation_front(self, frames):
        self.front_anim = []
        self.front_anim_num = 0
        for img in frames:
            i = pygame.image.load(img)
            preload = pygame.transform.scale(i, (self.width, self.height))
            self.front_anim.append(preload)
            self.front_anim_num += 1

    def set_animation_back(self, frames):
        self.back_anim = []
        self.back_anim_num = 0
        for img in frames:
            i = pygame.image.load(img)
            preload = pygame.transform.scale(i, (self.width, self.height))
            self.back_anim.append(preload)
            self.back_anim_num += 1

    def set_animation_left(self, frames):
        self.left_anim = []
        self.left_anim_num = 0
        for img in frames:
            i = pygame.image.load(img)
            preload = pygame.transform.scale(i, (self.width, self.height))
            self.left_anim.append(preload)
            self.left_anim_num += 1

    def set_animation_right(self, frames):
        self.right_anim = []
        self.right_anim_num = 0
        for img in frames:
            i = pygame.image.load(img)
            preload = pygame.transform.scale(i, (self.width, self.height))
            self.right_anim.append(preload)
            self.right_anim_num += 1

    def glue_animations(self):
        self.glued_preload.update({"front": self.front_anim})
        self.glued_preload.update({"back": self.back_anim})
        self.glued_preload.update({"left": self.left_anim})
        self.glued_preload.update({"right": self.right_anim})



    def set_speed(self, x):
        self.speed = x




