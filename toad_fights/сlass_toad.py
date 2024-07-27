from abc import ABC, abstractmethod
from random import randint


class Toad(ABC):
    """Базовый абстрактный класс жаба"""

    attack = 15
    health = 150
    armor = 5

    @abstractmethod
    def get_attack() -> int:
        """метод атаки"""
        
        pass

    @abstractmethod
    def get_armor() -> int:
        """метод получения брони"""
        
        pass

    @abstractmethod
    def get_class_name() -> str:
        """метод получения названия класса жабы"""
        
        pass
    
    @abstractmethod
    def get_health() -> int:
        """метод получения здоровья жабы"""
        
        pass


class Assassin(Toad):
    """Класс ассасин"""
    
    def __init__(self):
        # увеличиваем здоровье на 25%
        self.health = int(
            self.__class__.health / 100 * 25 + self.__class__.health
        )

    def get_attack(self) -> int:
        """метод атаки"""
        
        return randint(self.attack // 2, self.attack)

    def get_armor(self):
        """метод получения брони"""
        
        return randint(0, self.armor)
    
    def get_class_name(self) -> str:
        """метод получения названия класса жабы"""
        
        return self.__class__.__name__
    
    def get_health(self) -> int:
        """метод получения здоровья жабы"""
        
        return max(0, self.health)


class Adventurer(Toad):
    """Класс авантюрист"""
    
    def __init__(self):
        # увеличиваем урон на 50%
        self.attack = int(
            self.__class__.attack / 100 * 50 + self.__class__.attack
        )

    def get_attack(self) -> int:
        """метод атаки"""
        
        return randint(self.attack // 2, self.attack)
    
    def get_armor(self) -> int:
        """метод получения брони"""
        
        return randint(0, self.armor)
    
    def get_class_name(self) -> str:
        """метод получения названия класса жабы"""
        
        return self.__class__.__name__
    
    def get_health(self) -> int:
        """метод получения здоровья жабы"""
        
        return max(0, self.health)


class Craftsman(Toad):
    """Класс ремесленник"""
    
    def __init__(self):
        # увеличиваем броню на 100%
        self.armor = int(self.__class__.armor * 2)

    def get_attack(self) -> int:
        """метод атаки"""
        
        return randint(self.attack // 2, self.attack)
    
    def get_armor(self) -> int:
        """метод получения брони"""
        
        return randint(0, self.armor)
    
    def get_class_name(self) -> str:
        """метод получения названия класса жабы"""
        
        return self.__class__.__name__
    
    def get_health(self) -> int:
        """метод получения здоровья жабы"""
        
        return max(0, self.health)


def random_class():
    """Функция вернёт случайный класс для жабы"""

    list_class = [Assassin, Adventurer, Craftsman]
    random_index = randint(0, len(list_class) - 1)

    return list_class[random_index]


def perform_attack(attacker, defender) -> bool:
    """Выполняет атаку жабы."""
    
    damage = max(0, attacker().get_attack() - defender().get_armor())
    if damage > 0:
        defender.health -= damage
        return True
    return False


if __name__ == '__main__':
    toad_assassin = Assassin()
    print(toad_assassin.health, 'характеристика здоровья')
    print(toad_assassin.attack, 'характеристика атаки')
    print(toad_assassin.armor, 'характеристика брони')
    print(toad_assassin.get_class_name(), 'класс жабы')
    print(toad_assassin.get_armor(), 'танкует')
    print(toad_assassin.get_attack(), 'атакует\n')

    toad_adventurer = Adventurer()
    print(toad_adventurer.health, 'характеристика здоровья')
    print(toad_adventurer.attack, 'характеристика атаки')
    print(toad_adventurer.armor, 'характеристика брони')
    print(toad_adventurer.get_class_name(), 'класс жабы')
    print(toad_adventurer.get_armor(), 'танкует')
    print(toad_adventurer.get_attack(), 'атакует\n')

    toad_craftsman = Craftsman()
    print(toad_craftsman.health, 'характеристика здоровья')
    print(toad_craftsman.attack, 'характеристика атаки')
    print(toad_craftsman.armor, 'характеристика брони')
    print(toad_craftsman.get_class_name(), 'класс жабы')
    print(toad_craftsman.get_armor(), 'танкует')
    print(toad_craftsman.get_attack(), 'атакует\n')

    print(random_class(), 'случайный класс жабы')
