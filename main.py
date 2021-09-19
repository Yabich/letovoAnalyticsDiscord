import discord
import os


class Myclient (discord.Client):
    emoji = '\N{THUMBS UP SIGN}'

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!'):
            if message.content == '!login':
                await message.channel.send('https://letovo.cf')
            elif message.content == '!schedule':
                await message.channel.send('What schedule do you want? 1 - Entire schedule 2 - Today\'s schedule 3 - '
                                           'Specific day schedule')
            elif message.content == '!homework':
                await message.channel.send('Your whole homework for the next week:')
            elif message.content == '!help':
                await message.channel.send('My commands: !login, !schedule, !homework, !grades')
            elif message.content == '!grades':
                await message.channel.send('What subject do you need grades for?')


            else:
                await message.channel.send('Sorry, I dont have this command, sadly consider writing !help to see all '
                                           'commands')


client = Myclient()
client.run(os.getenv('TOKEN'))
