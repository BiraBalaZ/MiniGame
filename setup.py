from classes import Player, Food, Drink
from functions import print_life, action_consume

# Creating the object of Player 1
player_one = Player()
player_one.name = input(str('What is the name of Player1?\n>>>'))

# Creating the object of Player 2
player_two = Player()
player_two.name = input(str('What is the name of Player2?\n>>>'))

# Creating a consumable objects
food = Food()
drink = Drink()

# Result of code:
print_life(player_one)
action_consume(food, player_one)
action_consume(drink, player_one)

player_one.attack(player_one.sword_damage, player_two)

print_life(player_two)
action_consume(food, player_two)
action_consume(drink, player_two)
