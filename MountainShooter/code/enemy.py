#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from MountainShooter.code.entity import Entity
from MountainShooter.code.const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from MountainShooter.code.enemy_shot import EnemyShot
class Enemy(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(self.name, position=(self.rect.centerx, self.rect.centery))



