import discord
import os

class Myclient(discord.Client):
    curusers = {}
    logged_on = [469107885536706560, 525400773375426590]
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
                await self.channel.send('https://letovo-analytics.web.app/')
            elif message.content == '/menu':
                my_message = await message.channel.send(
                    'Greetings, ' + message.author.name + '. Choose an option below. :calendar_spiral: for Schedule, 🏡 for Homework, 🔢 for grades and 🌲 for holidays')
                await my_message.add_reaction('🗓️')
                await my_message.add_reaction('🏡')
                await my_message.add_reaction('🔢')
                await my_message.add_reaction('🌲')
                self.curusers[message.author.id] = 'Menu', self.channel, my_message
            print('Last message in', message.channel, 'sent by', message.author.name)
    async def on_raw_reaction_add(self, payload):
        user = await self.fetch_user(payload.user_id)
        reaction = str(payload.emoji)
        message = payload.message_id
        if user != client.user:
            if user.id in self.curusers:
                if self.curusers[user.id][2].id == message:
                    if self.curusers[user.id][0] == "Menu":
                        if reaction == '🗓️':
                            self.curusers[user.id] = 'Schedule_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                        elif reaction == '🏡':
                            self.curusers[user.id] = 'Homework_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                        elif reaction == '🔢':
                            self.curusers[user.id] = 'Grades', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                        elif reaction == '🌲':
                            self.curusers[user.id] = 'Holidays', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Schedule_menu':
                        if reaction == '🗓️':
                            await self.curusers[user.id][1].send('Расписание на сегодня')
                            del (self.curusers[user.id])
                        elif reaction == '🏡':
                            await self.curusers[user.id][1].send('Расписание на неделю')
                            del (self.curusers[user.id])
                        elif reaction == '🔢':
                            self.curusers[user.id] = 'Schedule_choice', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Schedule_choice':
                        if reaction == '1️⃣':
                            await self.curusers[user.id][1].send('Понедельник расписание')
                            del (self.curusers[user.id])
                        elif reaction == '2️⃣':
                            await self.curusers[user.id][1].send('Вторник расписание')
                            del (self.curusers[user.id])
                        elif reaction == '3️⃣':
                            await self.curusers[user.id][1].send('Среда расписание')
                            del (self.curusers[user.id])
                        elif reaction == '4️⃣':
                            await self.curusers[user.id][1].send('Четверг расписание')
                            del (self.curusers[user.id])
                        elif reaction == '5️⃣':
                            await self.curusers[user.id][1].send('Пятница расписание')
                            del (self.curusers[user.id])
                        elif reaction == '5️⃣':
                            await self.curusers[user.id][1].send('Суббота расписание')
                            del (self.curusers[user.id])
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Schedule_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Homework_menu':
                        if reaction == '🏚️':
                            await self.curusers[user.id][1].send('ДЗ на завтра')
                            del (self.curusers[user.id])
                        elif reaction == '🏘️':
                            await self.curusers[user.id][1].send('ДЗ на неделю')
                            del (self.curusers[user.id])
                        elif reaction == '🔢':
                            self.curusers[user.id] = 'Homework_choice', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Homework_choice':
                        if reaction == '1️⃣':
                            await self.curusers[user.id][1].send('Понедельник ДЗ')
                            del (self.curusers[user.id])
                        elif reaction == '2️⃣':
                            await self.curusers[user.id][1].send('Вторник ДЗ')
                            del (self.curusers[user.id])
                        elif reaction == '3️⃣':
                            await self.curusers[user.id][1].send('Среда ДЗ')
                            del (self.curusers[user.id])
                        elif reaction == '4️⃣':
                            await self.curusers[user.id][1].send('Четверг ДЗ')
                            del (self.curusers[user.id])
                        elif reaction == '5️⃣':
                            await self.curusers[user.id][1].send('Пятница ДЗ')
                            del (self.curusers[user.id])
                        elif reaction == '5️⃣':
                            await self.curusers[user.id][1].send('Суббота ДЗ')
                            del (self.curusers[user.id])
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Homework_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == ' ':
                        if reaction == '🔄':
                            await self.curusers[user.id][1].send('Все оценки')
                            del (self.curusers[user.id])
                        elif reaction == '‼️':
                            await self.curusers[user.id][1].send('Оценки самматив')
                            del (self.curusers[user.id])
                        elif reaction == '📅':
                            await self.curusers[user.id][1].send('Оценки недавно')
                            del (self.curusers[user.id])
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            await self.status_change(user.id)

    async def status_change(self, user):
        await self.curusers[user][2].delete()
        channel = self.curusers[user][1]
        if self.curusers[user][0] == 'Homework_menu':
            my_message = await channel.send(
                'Choose an option below. 🏚️ for tomorrow\'s homework , 🏘️ for entire week homework, 🔢 for a '
                'specific day homework, ⬅️to go back')
            self.curusers[user] = self.curusers[user][0], self.curusers[user][1], my_message
            await my_message.add_reaction('🏚️')
            await my_message.add_reaction('🏘️')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Homework_choice':
            my_message = await channel.send(
                'Choose an option below. :one: for Monday, :two: for Tuesday, :three: for Wednesday, :four: for '
                'Thursday, :five: for Friday, :six: for Saturday, ⬅️to go back')
            self.curusers[user] = self.curusers[user][0], self.curusers[user][1], my_message
            await my_message.add_reaction('1️⃣')
            await my_message.add_reaction('2️⃣')
            await my_message.add_reaction('3️⃣')
            await my_message.add_reaction('4️⃣')
            await my_message.add_reaction('5️⃣')
            await my_message.add_reaction('6️⃣')
            await my_message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Schedule_menu':
            my_message = await channel.send(
                'Choose an option below. 🗓️ for  today\'s schedule, 🏡 for entire week schedule, 🔢 for a '
                'specific day schedule, ⬅️to go back')
            self.curusers[user] = self.curusers[user][0], self.curusers[user][1], my_message
            await my_message.add_reaction('🗓️')
            await my_message.add_reaction('🏡')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Schedule_choice':
            my_message = await channel.send(
                'Choose an option below. :one: for Monday, :two: for Tuesday, :three: for Wednesday, :four: for '
                'Thursday, :five: for Friday, :six: for Saturday, :arrow_left: to go back')
            self.curusers[user] = self.curusers[user][0], self.curusers[user][1], my_message
            await my_message.add_reaction('1️⃣')
            await my_message.add_reaction('2️⃣')
            await my_message.add_reaction('3️⃣')
            await my_message.add_reaction('4️⃣')
            await my_message.add_reaction('5️⃣')
            await my_message.add_reaction('6️⃣')
            await my_message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Grades':
            my_message = await channel.send(
                'Choose an option below. 🔄 for  all marks, ‼️ for summative marks, 📅 for recent '
                'marks, ⬅️ to go back')
            self.curusers[user] = self.curusers[user][0], self.curusers[user][1], my_message
            await my_message.add_reaction('🔄')
            await my_message.add_reaction('‼️')
            await my_message.add_reaction('📅')
            await my_message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Holidays':
            await channel.send('каникулы :D')
            del (self.curusers[user])
        elif self.curusers[user][0] == 'Menu':
            id = int(user)
            name = str(await client.fetch_user(id))
            a = name.find('#')
            my_message = await channel.send(
                'Greetings, ' + name[:a] + '. Choose an option below. :calendar_spiral: for Schedule, 🏡 for Homework, '
                                       '🔢 for grades and 🌲 for holidays')
            self.curusers[user] = self.curusers[user][0], self.curusers[user][1], my_message
            await my_message.add_reaction('🗓️')
            await my_message.add_reaction('🏡')
            await my_message.add_reaction('🔢')
            await my_message.add_reaction('🌲')
        else:
            channel.send('Something wrong happened, please contact @yab1ch on telegram')
            print('Problem for ' + str(user) + 'his state is ' + str(self.curusers[user][0]))


if __name__ == "__main__":
    client = Myclient()
    client.run(os.getenv('TOKEN'))#env