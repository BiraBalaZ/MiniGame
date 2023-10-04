from classes import Player, Food, Drink
from functions import print_life

# Creating Player object
player = Player()
assert player.life == player.max_life
assert player.alive == True

# Creating Consumable Food Item
food = Food()
assert food.life_points == 25
assert food.rotten == False

# Checking consumable function of the food item
try:
    player.consume_item(food)
    print_life(player)
    assert player.life == player.max_life
except AssertionError as error:
    print(f"{player.life} != {player.max_life}")
    raise error

# Creating Consumable Drink Item
drink = Drink()
assert drink.life_points == 15
assert drink.rotten == False

# Checking consumable function of the drink item
try:
    player.consume_item(drink)
    print_life(player)
    assert player.life == player.max_life
except AssertionError as error:
    print(f"{player.life} != {player.max_life}")
    raise error

# Giving rotten consumables for Player
# Checking consumable function of the food item
food.rotten = True
assert food.rotten == True

player.consume_item(food)
print_life(player)
assert player.life < player.max_life
assert player.life > player.min_life
assert player.life == 75

# Checking consumable function of the drink item
drink.rotten = True
assert drink.rotten == True

player.consume_item(drink)
print_life(player)
assert player.life < player.max_life
assert player.life > player.min_life
assert player.life == 60

# Killing Player
player.consume_item(food)
print_life(player)
player.consume_item(food)
print_life(player)
player.consume_item(drink)
print_life(player)

# Checking if Player is dead
assert player.life == 0

# Checking tests results
print("Passed all tests! =D")
