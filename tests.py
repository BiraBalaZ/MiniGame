from classes import Player, Apple, OrangeJuice
from functions import print_life

# Creating Player object
player = Player()
initial_life = player.life
assert player.life == player.max_life
assert player.alive == True

# Creating Consumable Food Item
apple = Apple()
assert apple.life_points == 50
assert apple.rotten == False

# Checking consumable function of the food item
try:
    player.consume_item(apple)
    print_life(player)
    assert player.life == player.max_life
except AssertionError as error:
    print(f"{player.life} != {player.max_life}")
    raise error

# Creating Consumable Drink Item
orange_juice = OrangeJuice()
assert orange_juice.life_points == 25
assert orange_juice.rotten == False

# Checking consumable function of the drink item
try:
    player.consume_item(orange_juice)
    print_life(player)
    assert player.life == player.max_life
except AssertionError as error:
    print(f"{player.life} != {player.max_life}")
    raise error

# Giving rotten consumables for Player
# Checking consumable function of the food item
apple.rotten = True
assert apple.rotten == True

player.consume_item(apple)
print_life(player)
assert player.life < player.max_life
assert player.life > player.min_life
assert player.life == 50

# Checking consumable function of the drink item
orange_juice.rotten = True
assert orange_juice.rotten == True

player.consume_item(orange_juice)
print_life(player)
assert player.life < player.max_life
assert player.life > player.min_life
assert player.life == 25

# Killing Player
player.consume_item(apple)
print_life(player)

# Checking if Player is dead
assert player.life == 0

# Checking tests results
print("Passed all tests! =D")
