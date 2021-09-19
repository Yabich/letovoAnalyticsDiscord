import discord
import os


class Myclient (discord.Client):
    emoji = '\N{THUMBS UP SIGN}'

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        channelid = message.channel.id
        channel = client.get_channel(channelid)
        if message.content.startswith('/'):
            if message.content == '/login':
                await channel.send('https://letovo.cf')
            elif message.content == '/schedule':
                await channel.send('What schedule do you want? 1 - Entire schedule 2 - Today\'s schedule 3 - '
                                           'Specific day schedule')
                await message.add_reaction('1️⃣')
            elif message.content == '/homework':
                await channel.send('Your whole homework for the next week:')
            elif message.content == '/help':
                await channel.send('My commands: !login, !schedule, !homework, !grades')
            elif message.content == '/grades':
                await channel.send('What subject do you need grades for?')
            else:
                await channel.send('Sorry, I dont have this command sadly, consider writing !help to see all '
                                           'commands')


client = Myclient()
client.run(os.getenv('TOKEN'))
