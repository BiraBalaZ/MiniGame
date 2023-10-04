from functions import maximum_comparator, minimum_comparator

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

 # # # # # # # # # # # # # # # # # # # # #

class Consumable:
    '''Docstring'''
    rotten = False
    life_points = None
    msg = None

class Drink(Consumable):
    '''Docstring'''
    life_points = 15
    msg = None

class Food(Consumable):
    '''Docstring'''
    life_points = 25
    msg = None

 # # # # # # # # # # # # # # # # # # # # #

class Apple(Food):
    '''Docstring'''
    life_points = 50
    msg = 'eats one beautiful apple'

class Banana(Food):
    '''Docstring'''
    life_points = 35
    msg = 'eats a banana'

class Sandwitch(Food):
    '''Docstring'''
    life_points = 45
    msg = 'eats a wonderful sandwitch'

class Cookie(Food):
    '''Docstring'''
    life_points = 25
    msg = 'eats a Cookie in format of a cat'

# # # # # # # # # # # # # # # # # # # # #

class Coffee(Drink):
    '''Docstring'''
    life_points = 25
    msg = 'drinks a Cuo of Coffee'

class EnergyDrink(Drink):
    '''Docstring'''
    life_points = 25
    msg = 'drinks a MONSTER MANGO LOCO ENERGY DRINK'

class Water(Drink):
    '''Docstring'''
    life_points = 30
    msg = 'drinks a Water Bottle'

class OrangeJuice(Drink):
    '''Docstring'''
    life_points = 25
    msg = 'drinks a Cup of Orange Juice'

# # # # # # # # # # # # # # # # # # # # #

class Enemy:
    '''Docstring'''
    alive = True
    life = 10
    level = 1
    attack_damage = 10

    # Dying
    if life <= 0:
        alive = False
