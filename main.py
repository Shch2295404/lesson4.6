import random


class Hero:
    def __init__(self, name, health, attack_power):
        # Инициализация героя с именем, здоровьем и силой атаки
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, character):
        # Атака другого персонажа
        # Урон определяется как сила атаки героя плюс случайное число от -10 до 10
        damage = self.attack_power + random.randint(-10, 10)
        character.health -= damage  # Уменьшаем здоровье атакуемого персонажа
        print(f'{self.name} атаковал {character.name}, и нанёс {damage} очков урона.')
        # Выводим остаток здоровья атакуемого или сообщение о смерти
        if character.health > 0:
            print(f'У {character.name} осталось {character.health} очков здоровья.')
        else:
            print(f'{character.name} умер.')

    def is_alive(self):
        # Проверка, жив ли герой (здоровье больше 0)
        return self.health > 0


class Game:
    def __init__(self, hero1, hero2):
        # Инициализация игры с двумя героями
        self.hero1 = hero1
        self.hero2 = hero2

    def start(self):
        # Начало игры
        round_number = 1  # Номер текущего раунда
        # Пока оба героя живы, игра продолжается
        while self.hero1.is_alive() and self.hero2.is_alive():
            print(f"\nРаунд {round_number}.")
            # Первый герой атакует второго
            self.hero1.attack(self.hero2)
            if not self.hero2.is_alive():
                # Если второй герой умирает, игра заканчивается
                break
            # Второй герой атакует первого
            self.hero2.attack(self.hero1)
            round_number += 1  # Переход к следующему раунду
        # Определяем победителя
        if self.hero1.is_alive():
            print(f'\n{self.hero1.name} выиграл!')
        else:
            print(f'\n{self.hero2.name} выиграл!')


# Создаём двух героев
hero_1 = Hero('Игрок', 100, 10)
hero_2 = Hero('Компьютер', 100, 10)

# Инициализируем игру с созданными героями
game = Game(hero_1, hero_2)

# Выводим сообщение о начале игры
print(f"\nНачинается бой между {hero_1.name} и {hero_2.name}.")

# Запускаем игру
game.start()
