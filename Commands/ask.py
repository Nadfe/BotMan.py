import random


def ask_qn(msg):
    if len(msg.split()) == 1:
        return 'You didn\'t ask the question, smartass'
    else:
        answer = random.randint(0, 5)
        if answer == 0:
            return '_No_'
        if answer == 1:
            return '_Yes_'
        if answer == 2:
            return '_Maybe_'
        if answer == 3:
            return '_Perhaps_'
        if answer == 4:
            return '_Why don\'t you wait and see'
        if answer == 5:
            return '_Can\'t say for sure_'
