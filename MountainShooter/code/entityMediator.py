from MountainShooter.code.entity import Entity
from MountainShooter.code.enemy import Enemy
from MountainShooter.code.const import WIN_WIDTH
from MountainShooter.code.player_shot import PlayerShot
from MountainShooter.code.enemy_shot import EnemyShot

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity_teste = entity_list[i]
            EntityMediator.__verify_collision_window(entity_teste)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
