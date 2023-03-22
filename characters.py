import pygame
from pygame.locals import *
from random import randint, choice, uniform
from assets import IMAGES
import math

GRAVITY = 1
GROUND_LEVEL = 550

class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, pos, asset_lib, **kwargs):
        pygame.sprite.Sprite.__init__(self)


        self.create_physics(pos,**kwargs)
        self.create_animation(asset_lib, **kwargs)

    def update_physics(self, update_gravity, own_movement, jump=False):
        self.on_ground = self.position.y > self.ground_level

        if update_gravity:
            self.gravity_force.y += self.gravity * self.mass / 100

            if self.gravity_force.y > 9.8:
                self.gravity_force.y = 9.8

            if not self.position.y > self.ground_level:

                self.position.y += self.gravity_force.y

        if own_movement:

            keys = pygame.key.get_pressed()

            self.velocity.x += (keys[K_d] - keys[K_a]) * self.speed
            if not jump:
                self.velocity.y += (keys[K_s] - keys[K_w]) * self.speed
            else:
                if keys[K_SPACE] and self.on_ground:
                    self.velocity.y = -((self.speed - self.friction)*self.speed * 80) / self.gravity

        self.velocity = self.velocity.move_towards((0,0), self.friction)

        
        self.position += self.velocity

        if self.position.y > self.ground_level:
            self.gravity_force.y = 0 
            self.velocity.y = 0
            self.position.y -= self.velocity.y

        if self.velocity.x > self.max_speed:
            self.velocity.x = self.max_speed 
        if self.velocity.x < self.max_speed *-1:
            self.velocity.x = self.max_speed *-1

        if not jump:
            if self.velocity.y > self.max_speed:
                self.velocity.y = self.max_speed 
            if self.velocity.y < self.max_speed *-1:
                self.velocity.y = self.max_speed *-1
 
    def create_physics(self,pos, **kwargs):
        global GRAVITY, GROUND_LEVEL

        self.gravity = GRAVITY
        self.ground_level = GROUND_LEVEL
        self.mass = kwargs["mass"]
        self.friction = self.gravity * self.mass / 50
        self.speed = kwargs["speed"]
        self.speed_squared = self.speed * self.speed
        self.gravity_force = pygame.math.Vector2(0,0)
        self.velocity = pygame.math.Vector2(0,0)

        self.max_speed =  self.mass  / (self.speed * 5)

        self.position = pygame.math.Vector2(pos)
        self.on_ground = self.position.y > self.ground_level

    def animate(self):
        self.update_anim_info()
        time_now = pygame.time.get_ticks()

        if time_now > self.next_frame:
            self.index += 1 
            
            self.next_frame = time_now + self.anim_cooldown
            if self.index > self.max_index:
            
                self.index = 0

                if not self.repeat_anim:
                    self.animation = self.base_anim
        

        self.image = self.anim_list[self.index]

        if self.flip:
            self.image = pygame.transform.flip(self.anim_list[self.index], True, False)

    def update_anim_info(self):
        self.anim_list = self.images[self.anim_path][self.animation]
        self.max_index = len(self.anim_list) -1
        self.anim_cooldown = self.animation_info[self.animation][0]
        self.repeat_anim = self.animation_info[self.animation][1]
        self.anim_done = self.index>self.max_index

    def create_animation(self, asset_lib, **kwargs):

        self.anim_path = kwargs["anim_group"]
        self.animation_info = kwargs["anim_names"]
        self.base_anim = kwargs.get("base_anim", "idle")
        self.index = 0 
        self.anim_done = False
        self.flip = False

        if "idle" in self.animation_info.keys():
            self.animation = "idle"
        else:
            raise Exception("Please set an idle animation state")

        self.images = asset_lib

        self.anim_cooldown = self.animation_info[self.animation][0]
        self.repeat_anim = self.animation_info[self.animation][1]

        self.next_frame = pygame.time.get_ticks() + self.anim_cooldown

        self.anim_list = self.images[self.anim_path][self.animation]

        self.max_index = len(self.anim_list) - 1

        self.image = self.anim_list[self.index]

    def set_animation(self, animation):
        if self.animation != animation:
            self.animation = animation
            self.index = 0 
            self.update_anim_info()
            self.next_frame = pygame.time.get_ticks() + self.anim_cooldown


class Player(PhysicsEntity):
    def __init__(self, pos, **kwargs):
        super().__init__(pos, kwargs.pop('asset_lib'), **kwargs)

        self.not_idled_anims = ["punch"]

        self.not_runned_anims = ["punch"]

    def update(self, screen):
        self.animate()
        self.control()
        self.update_physics(True, True, True)

        print(self.velocity, self.gravity_force)

        screen.blit(self.image, self.position)

    def control(self):
        keys = pygame.key.get_pressed()

        buttons = [keys[K_a], keys[K_d]]

        if True in buttons:
            if not self.animation in self.not_runned_anims:
                self.set_animation("run")
        else:
            if not self.animation in self.not_idled_anims:
                self.set_animation("idle")

        if keys[K_r]:
            self.flip = True
        else:
            self.flip = False

        if keys[K_r]:
            self.set_animation("punch")

plr = Player(
    (200, 200),
    asset_lib=IMAGES,
    anim_group="player",
    anim_names={"idle": (400, True), "run": (200, True), "punch": (500, False)},
    mass=10,
    speed=.5,
)