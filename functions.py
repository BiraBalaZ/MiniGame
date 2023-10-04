from time import sleep

# Function to compare maximum value
def maximum_comparator(current_value, upper_limit, change):
    '''Docstring'''
    if current_value + change > upper_limit:
        return upper_limit
    else:
        return current_value + change

# Function to compare minimum value
def minimum_comparator(current_value, lower_limit, change):
    '''Docstring'''
    if current_value - change < lower_limit:
        return lower_limit
    else:
        return current_value - change

# Checking life
def check_life(player):
    '''Docstring'''
    if player.life <= player.min_life:
        print(f'Player {player.name} is dead...')

# Function to show player's life in terminal
def print_life(player):
    '''Docstring'''
    sleep(1)
    print(f'The life of {player.name} is {player.life}/{player.max_life}')
    check_life(player)

def action_consume(item, player):
    '''Docstring'''
    if player.alive:
        sleep(1)
        player.consume_item(item)
        sleep(2.5)
        print_life(player)
