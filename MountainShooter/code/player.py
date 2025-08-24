#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from MountainShooter.code.entity import Entity
from MountainShooter.code.player_shot import PlayerShot
from MountainShooter.code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_SHOT_DELAY
from MountainShooter.code.const import PLAYER_KEY_UP,PLAYER_KEY_SHOOT,PLAYER_KEY_DOWN,PLAYER_KEY_LEFT,PLAYER_KEY_RIGHT
class Player(Entity):
    def __init__(self, name: str, position:tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top>0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom<WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left>0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right<WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(self.name, position=(self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
            return None
