import details

server_prefix = details.server_prefix


def good_morning(msg, message):
    nickname = message.author.nick
    if nickname is None:
        nickname = message.author.name
    if msg == f'{server_prefix}goodmorning':
        return f"Good morning, {nickname}!"


def good_afternoon(msg, message):
    nickname = message.author.nick
    if nickname is None:
        nickname = message.author.name
    if msg == f'{server_prefix}goodafternoon':
        return f"Good afternoon, {nickname}!"


def good_evening(msg, message):
    nickname = message.author.nick
    if nickname is None:
        nickname = message.author.name
    if msg == f'{server_prefix}goodevening':
        return f"Good evening, {nickname}!"


def good_night(msg, message):
    nickname = message.author.nick
    if nickname is None:
        nickname = message.author.name
    if msg == f'{server_prefix}goodnight':
        return f"Good night, {nickname}!"
