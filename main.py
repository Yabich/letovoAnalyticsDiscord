import discord
import os


class Myclient (discord.Client):
    async def on_message(self, message):
        if message.content == 'Schedule':
            await message.channel.send('What schedule do you want? 1 - Entire schedule 2 - Today\'s schedule 3 - Specific day schedule')



    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


client = Myclient()
client.run(os.getenv('TOKEN'))
