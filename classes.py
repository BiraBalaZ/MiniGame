from functions import maximum_comparator, minimum_comparator
import random

# List of items
drink_types = ['Orange juice', 'Water bottle', 'Energy drink', 'Banana vitamin', 'Cup of coffee']

class Player:
    '''Docstring'''
    alive = True
    name = None
    life = 100
    min_life = 0
    max_life = 100
    strength = 5
    sword_damage = 25

    # Defining if player is dead
    if life > min_life:
        live = True

    def consume_item(self, item):
        '''Docstring'''
        if not item.rotten:
            self.life = maximum_comparator(self.life, self.max_life, item.life_points)
            print(f'{self.name} {item.msg} and recovered {item.life_points} points of life')
        else:
            self.life = minimum_comparator(self.life, self.min_life, item.life_points)
            print(f'{self.name} {item.msg} poisonous and lost {item.life_points} points of life')

    def attack(self, damage, target):
        '''Docstring'''
        target.life = target.life-damage

class Consumable:
    '''Docstring'''
    rotten = False
    life_points = None
    msg = None

class Drink(Consumable):
    '''Docstring'''
    life_points = 15
    msg = f'drinks a {drink_types[random.randint(0, 4)]}'

class Food(Consumable):
    '''Docstring'''
    life_points = 25
    msg = 'eats something'

class Enemy:
    '''Docstring'''
    alive = True
    life = 10
    level = 1
    attack_damage = 10

    # Dying
    if life <= 0:
        alive = False
