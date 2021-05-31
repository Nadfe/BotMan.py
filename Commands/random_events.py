import random

outcomes = ['Heads', 'Tails', 'Nothing']


def coin_flip():
    result = random.choice(outcomes)
    return f'You tossed a coin and got... **_{result}_**.'


def roll_dice():
    result = random.randint(1, 6)
    return f'You rolled a die and got a _**{result}**_'
