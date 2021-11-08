import discord
import os


class Myclient(discord.Client):
    curusers = {}
    logged_on = [469107885536706560]
    message = ''
    channel = ''

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        channelid = message.channel.id
        self.channel = client.get_channel(channelid)
        if message.content.startswith('/'):
            if message.author.id not in self.logged_on:
                await self.channel.send('You aren\'t logged on. Consider typing /login')
            elif message.content == '/login':
                await self.channel.send('letovo.cf')
            elif message.content == '/menu':
                my_message = await message.channel.send(
                    'Greetings, ' + message.author.name + '. Choose an option below. :calendar_spiral: for Schedule, 🏡 for Homework, 🔢 for grades and 🌲 for holidays')
                await my_message.add_reaction('🗓️')
                await my_message.add_reaction('🏡')
                await my_message.add_reaction('🔢')
                await my_message.add_reaction('🌲')
                self.curusers[message.author] = 'Menu', self.channel.id, my_message
            print('Last message in', message.channel, 'sent by', message.author.name)

    async def on_raw_reaction_add(self, payload):
        user = await self.fetch_user(payload.user_id)
        reaction = payload.emoji
        if user != client.user:
            if user in self.curusers:
                if self.curusers[user][0] == 'Menu':
                    if reaction == '🗓️':
                        self.curusers[user.id][0] = 'Schedule_menu'
                        await  self.status_change(user.id)
                    elif reaction == '🏡':
                        self.curusers[user.id][0] = 'Homework_menu'
                        await  self.status_change(user.id)
                    elif reaction == '🔢':
                        self.curusers[user.id][0] = 'Grades'
                        await  self.status_change(user.id)
                    elif reaction == '🌲':
                        self.curusers[user.id][0] = 'Holidays'
                        await self.status_change(user.id)
                elif self.curusers[user][0] == 'Schedule_menu':
                    if reaction == '🗓️':
                        await self.curusers[user.id][1].send('Расписание на сегодня')
                        del (self.curusers[user])
                    elif reaction == '🏡':
                        await self.curusers[user.id][1].send('Расписание на неделю')
                        del (self.curusers[user])
                    elif reaction == '🔢':
                        self.curusers[user.id][0] = 'Schedule_choice'
                        await self.status_change(user.id)
                    elif reaction == '🌲':
                        self.curusers[user.id][0] = 'Menu'
                        await self.status_change(user.id)
                elif self.curusers[user][0] == 'Schedule_choice':
                    if reaction == '1':
                        await self.curusers[user.id][1].send('Понедельник расписание')
                        del (self.curusers[user])
                    elif reaction == '2':
                        await self.curusers[user.id][1].send('Вторник расписание')
                        del (self.curusers[user])
                    elif reaction == '3':
                        await self.curusers[user.id][1].send('Среда расписание')
                        del (self.curusers[user])
                    elif reaction == '4':
                        await self.curusers[user.id][1].send('Четверг расписание')
                        del (self.curusers[user])
                    elif reaction == '5':
                        await self.curusers[user.id][1].send('Пятница расписание')
                        del (self.curusers[user])
                    elif reaction == '6':
                        await self.curusers[user.id][1].send('Суббота расписание')
                        del (self.curusers[user])
                    elif reaction == '7':
                        self.curusers[user.id][0] = 'Schedule_menu'
                        await self.status_change(user.id)
                elif self.curusers[user][0] == 'Homework_menu':
                    if reaction == '🗓️':
                        await self.curusers[user.id][1].send('ДЗ на завтра')
                        del (self.curusers[user])
                    elif reaction == '🏡':
                        await self.curusers[user.id][1].send('ДЗ на неделю')
                        del (self.curusers[user])
                    elif reaction == '🔢':
                        self.curusers[user.id][0] = 'Homework_choice'
                        await self.status_change(user.id)
                    elif reaction == '🌲':
                        self.curusers[user.id][0] = 'Menu'
                        await self.status_change(user.id)
                elif self.curusers[user][0] == 'Homework_choice':
                    if reaction == '1':
                        await self.curusers[user.id][1].send('Понедельник ДЗ')
                        del (self.curusers[user])
                    elif reaction == '2':
                        await self.curusers[user.id][1].send('Вторник ДЗ')
                        del (self.curusers[user])
                    elif reaction == '3':
                        await self.curusers[user.id][1].send('Среда ДЗ')
                        del (self.curusers[user])
                    elif reaction == '4':
                        await self.curusers[user.id][1].send('Четверг ДЗ')
                        del (self.curusers[user])
                    elif reaction == '5':
                        await self.curusers[user.id][1].send('Пятница ДЗ')
                        del (self.curusers[user])
                    elif reaction == '6':
                        await self.curusers[user.id][1].send('Суббота ДЗ')
                        del (self.curusers[user])
                    elif reaction == '7':
                        self.curusers[user.id][0] = 'Homework_menu'
                        await self.status_change(user.id)
                elif self.curusers[user.id][0] == 'Grades':
                    if reaction == '🗓️':
                        await self.curusers[user.id][1].send('Все оценки')
                        del (self.curusers[user])
                    elif reaction == '🏡':
                        await self.curusers[user.id][1].send('Оценки самматив')
                        del (self.curusers[user])
                    elif reaction == '🔢':
                        await self.curusers[user.id][0].send('Оценки недавно')
                        del (self.curusers[user])
                    elif reaction == '🌲':
                        self.curusers[user.id][0] = 'Menu'
                        await self.status_change(user.id)

    async def status_change(self, user):
        await self.curusers[user.id][2].delete()
        if self.curusers[user][0] == 'Homework_menu':
            channel = client.get_channel(self.curusers[user][1])
            my_message = await channel.send(
                'Choose an option below. 🗓️ for tomorrow\'s homework , 🏡 for entire week homework, 🔢 for a '
                'specific day homework, 🌲 to go back')
            self.curusers[user.id][2] = my_message
            await my_message.add_reaction('🗓️')
            await my_message.add_reaction('🏡')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('🌲')
        elif self.curusers[user][0] == 'Homework_choice':
            channel = client.get_channel(self.curusers[user][1])
            my_message = await channel.send(
                'Choose an option below. :one: for Monday, :two: for Tuesday, :three: for Wednesday, :four: for '
                'Thursday, :five: for Friday, :six: for Saturday, :seven: to go back')
            self.curusers[user.id][2] = my_message
            await my_message.add_reaction(':one:')
            await my_message.add_reaction(':two:')
            await my_message.add_reaction(':three:')
            await my_message.add_reaction(':four:')
            await my_message.add_reaction(':five:')
            await my_message.add_reaction(':six:')
            await my_message.add_reaction(':seven:')
        elif self.curusers[user][0] == 'Schedule_menu':
            channel = client.get_channel(self.curusers[user][1])
            my_message = await channel.send(
                'Choose an option below. 🗓️ for  today\'s homework, 🏡 for entire week schedule, 🔢 for a '
                'specific day schedule, 🌲 to go back')
            self.curusers[user.id][2] = my_message
            await my_message.add_reaction('🗓️')
            await my_message.add_reaction('🏡')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('🌲')
        elif self.curusers[user][0] == 'Schedule_choice':
            channel = client.get_channel(self.curusers[user][1])
            my_message = await channel.send(
                'Choose an option below. :one: for Monday, :two: for Tuesday, :three: for Wednesday, :four: for '
                'Thursday, :five: for Friday, :six: for Saturday, :seven: to go back')
            self.curusers[user.id][2] = my_message
            await my_message.add_reaction(':one:')
            await my_message.add_reaction(':two:')
            await my_message.add_reaction(':three:')
            await my_message.add_reaction(':four:')
            await my_message.add_reaction(':five:')
            await my_message.add_reaction(':six:')
            await my_message.add_reaction(':seven:')
        elif self.curusers[user][0] == 'Grades':
            channel = client.get_channel(self.curusers[user][1])
            my_message = await channel.send(
                'Choose an option below. 🗓️ for  all marks, 🏡 for summative marks, 🔢 for recent '
                'marks, 🌲 to go back')
            self.curusers[user.id][2] = my_message
            await my_message.add_reaction('🗓️')
            await my_message.add_reaction('🏡')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('🌲')
        elif self.curusers[user][0] == 'Holidays':
            channel = client.get_channel(self.curusers[user][1])
            await channel.send('каникулы :D')
            del (self.curusers[user])
        elif self.curusers[user][0] == 'Menu':
            channel = client.get_channel(self.curusers[user][1])
            my_message = await channel.send(
                'Greetings, ' + user + '. Choose an option below. :calendar_spiral: for Schedule, 🏡 for Homework, '
                                       '🔢 for grades and 🌲 for holidays')
            await my_message.add_reaction('🗓️')
            await my_message.add_reaction('🏡')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('🌲')
        else:



if __name__ == "__main__":
    client = Myclient()
    client.run(os.getenv('TOKEN'))
