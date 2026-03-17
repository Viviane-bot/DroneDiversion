from code import entity
from code.enemy import Enemy


class entityMediator:

    @staticmethod
    def __verify_collision_window(ent: entity):
        if isinstance(ent, Enemy):
        pass

    @staticmethod
    def verify_collision(entity_list: list[entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            entityMediator.__verify_collision_window(test_entity)