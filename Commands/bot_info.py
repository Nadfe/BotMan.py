import discord
import details

prefix = details.server_prefix

bot_bio = '''Hello! I am Botman, a bot written in Python by Mahasvan Mohan (github: Mahas1). 
I am open-source, and the source code for me can be viewed and downloaded here. Feel free to check it out!
https://github.com/Mahas1/BotMan.py/'''


def bot_help():
    help_text = discord.Embed(colour=discord.Colour.blue())
    help_text.set_author(name='List of commands')
    help_text.add_field(name=f'{prefix}ping', value='Replies with "Pong!"', inline=False)
    help_text.add_field(name=f'{prefix}hello', value='Says hello', inline=False)
    help_text.add_field(name=f'{prefix}userid [user: optional]', value='Replies with the user\'s ID', inline=False)
    help_text.add_field(name=f'{prefix}inspire', value='Sends a random quote', inline=False)
    help_text.add_field(name=f'{prefix}link [name]', value=f'Use `{prefix}link list` for a list of links', inline=False)
    help_text.add_field(name=f'{prefix}goodmorning', value='Wishes a good morning to you, because it\'s your friend',
                        inline=False)
    help_text.add_field(name=f'{prefix}goodafternoon',
                        value='Wishes a good afternoon to you, because it\'s your friend',
                        inline=False)
    help_text.add_field(name=f'{prefix}goodevening', value='Wishes a good evening to you, because it\'s your friend',
                        inline=False)
    help_text.add_field(name=f'{prefix}goodnight', value='Wishes a good night to you, because it\'s your friend',
                        inline=False)
    help_text.add_field(name=f'{prefix}flip', value='Flips a coin, and tells you the result', inline=False)
    help_text.add_field(name=f'{prefix}roll', value='Rolls a die, and tells you the result', inline=False)
    help_text.add_field(name=f'{prefix}ask', value='Gives honest opinion in the form of yes/no', inline=False)
    help_text.add_field(name=f'A few Easter eggs', value='Find them out yourself', inline=False)
    return help_text
