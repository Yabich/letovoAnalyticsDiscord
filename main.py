import discord
import os


class Myclient(discord.Client):
    curuser = ''
    message = ''
    channel = ''
    dating = False

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        channelid = message.channel.id
        self.channel = client.get_channel(channelid)
        if message.content.startswith('/'):
            self.curuser = message.author
            print(self.curuser)
            print(f'Last message in {self.channel.name} sent by {message.author.name}: '
                  + message.content)
            if message.content == '/login':
                await self.channel.send('https://letovo.cf')
                self.dating = False
            elif message.content == '/schedule':
                await self.channel.send(
                    'What schedule do you want? Choose in reactions: :one: - Entire schedule :two:️ - Today\'s '
                    'schedule :three: - Specific day schedule')
                self.message = await self.channel.fetch_message(self.channel.last_message_id)
                await self.message.add_reaction('1️⃣')
                await self.message.add_reaction('2️⃣')
                await self.message.add_reaction('3️⃣')
                self.dating = False
            elif message.content == '/homework':
                await self.channel.send('What homework do you want? Choose in reactions: ')
                self.dating = False
            elif message.content == '/help':
                await self.channel.send('My commands: /login, /schedule, /homework, /grades')
                self.dating = False
            elif message.content == '/grades':
                await self.channel.send('What subject do you need grades for?')
                self.dating = False
        elif self.dating is True:
            if message.content == 'Monday' or message.content == 'monday':
                self.dating = False
            elif message.content == 'Tuesday' or message.content == 'tuesday':
                self.dating = False
            elif message.content == 'Wednesday' or message.content == 'wednesday':
                self.dating = False
            elif message.content == 'Thursday' or message.content == 'thursday':
                self.dating = False
            elif message.content == 'Friday' or message.content == 'friday':
                self.dating = False
            elif message.content == 'Saturday' or message.content == 'saturday':
                self.dating = False

    async def on_reaction_add(self, reaction, user):
        if user == self.curuser:
            if str(reaction.emoji) == '1️⃣':
                await self.channel.send('amogus')
            if str(reaction.emoji) == '2️⃣':
                await self.channel.send('amogus')
            if str(reaction.emoji) == '3️⃣':
                await self.channel.send('What day do you want?')
                self.dating = True


if __name__ == "__main__":
    client = Myclient()
    client.run(os.getenv('TOKEN'))
