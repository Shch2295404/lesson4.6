import random


class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, character):
        damage = self.attack_power + random.randint(-10, 10)
        character.health -= self.attack_power
        print(f'{self.name} атаковал {character.name}, и нанёс {damage} очков урона.')
        if character.health > 0:
            print(f'У {character.name} осталось {character.health} очков здоровья.')
        else:
            print(f'{character.name} умер.')

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, hero1, hero2):
        self.hero1 = hero1
        self.hero2 = hero2

    def start(self):
        round_number = 1
        while self.hero1.is_alive() and self.hero2.is_alive():
            print(f"\nРаунд {round_number}.")
            self.hero1.attack(self.hero2)
            if not self.hero2.is_alive():
                break
            self.hero2.attack(self.hero1)
            round_number += 1
        if self.hero1.is_alive():
            print(f'\n{self.hero1.name} выиграл!')
        else:
            print(f'\n{self.hero2.name} выиграл!')


hero_1 = Hero('Игрок', 100, 10)
hero_2 = Hero('Компьютер', 100, 10)

game = Game(hero_1, hero_2)

print(f"\nНачинается бой между {hero_1.name} и {hero_2.name}.")

game.start()
