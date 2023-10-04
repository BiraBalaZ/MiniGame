from classes import Player, Apple, OrangeJuice
from functions import print_life, action_consume

# Creating the object of Player 1
player_one = Player()
player_one.name = input(str('What is the name of Player1?\n>>>'))

# Creating the object of Player 2
player_two = Player()
player_two.name = input(str('What is the name of Player2?\n>>>'))

# Creating a consumable objects
apple = Apple()
orange_juice = OrangeJuice()

# Result of code:
print_life(player_one)
action_consume(apple, player_one)
action_consume(orange_juice, player_one)

print_life(player_two)
action_consume(apple, player_two)
action_consume(orange_juice, player_two)
