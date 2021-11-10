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
        massage = payload.message_id
        if user != client.user:
            if user.id in self.curusers:
                message = self.curusers[user.id][2]
                if self.curusers[user.id][2].id == massage:
                    if self.curusers[user.id][0] == "Menu":
                        deletion = await message.remove_reaction('🗓️', client.user), await message.remove_reaction('🏡', client.user), await message.remove_reaction('🔢', client.user), await message.remove_reaction('🌲', client.user)
                        if reaction == '🗓️':
                            self.curusers[user.id] = 'Schedule_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                        elif reaction == '🏡':
                            self.curusers[user.id] = 'Homework_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                        elif reaction == '🔢':
                            self.curusers[user.id] = 'Grades', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await message.remove_reaction('🔢', user)
                            await self.status_change(user.id)
                        elif reaction == '🌲':
                            self.curusers[user.id] = 'Holidays', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await message.remove_reaction('🌲', user)
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Schedule_menu':
                        deletion = await message.remove_reaction('▶️', client.user), await message.remove_reaction('📅', client.user), await message.remove_reaction('🔢', client.user), await message.remove_reaction('🌲', client.user), #await message.remove_reaction('▶️', user) await message.remove_reaction('📅', user), await message.remove_reaction('🔢', user), await message.remove_reaction('🌲', user)
                        if reaction == '▶️':
                            await self.curusers[user.id][1].send('Расписание на сегодня')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '📅':
                            await self.curusers[user.id][1].send('Расписание на неделю')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '🔢':
                            self.curusers[user.id] = 'Schedule_choice', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Schedule_choice':
                        deletion = await message.remove_reaction('1️⃣', client.user), await message.remove_reaction('2️⃣', client.user), await message.remove_reaction('3️⃣', client.user), await message.remove_reaction('4️⃣', client.user), await message.remove_reaction('5️⃣', client.user), await message.remove_reaction('6️⃣', client.user), await message.remove_reaction('⬅️', client.user)  # await message.remove_reaction('1️⃣', user), await message.remove_reaction('2️⃣', user), await message.remove_reaction('3️⃣', user), await message.remove_reaction('4️⃣', user), await message.remove_reaction('5️⃣', user), await message.remove_reaction('6️⃣', user), await message.remove_reaction('⬅️', user)
                        if reaction == '1️⃣':
                            await self.curusers[user.id][1].send('Понедельник расписание')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '2️⃣':
                            await self.curusers[user.id][1].send('Вторник расписание')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '3️⃣':
                            await self.curusers[user.id][1].send('Среда расписание')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '4️⃣':
                            await self.curusers[user.id][1].send('Четверг расписание')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '5️⃣':
                            await self.curusers[user.id][1].send('Пятница расписание')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '6️⃣':
                            await self.curusers[user.id][1].send('Суббота расписание')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Schedule_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Homework_menu':
                        deletion = await message.remove_reaction('🏚️', client.user), await message.remove_reaction('🏘️', client.user), await message.remove_reaction('🔢', client.user), await message.remove_reaction('⬅️', client.user) # await message.remove_reaction('🏚️', user), await message.remove_reaction('🏘️', user), await message.remove_reaction('🔢', user), await message.remove_reaction('⬅️', user)
                        if reaction == '🏚️':
                            await self.curusers[user.id][1].send('ДЗ на завтра')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '🏘️':
                            await self.curusers[user.id][1].send('ДЗ на неделю')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '🔢':
                            self.curusers[user.id] = 'Homework_choice', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == 'Homework_choice':
                        deletion = await message.remove_reaction('1️⃣', client.user), await message.remove_reaction('2️⃣', client.user), await message.remove_reaction('3️⃣',client.user), await message.remove_reaction('4️⃣', client.user), await message.remove_reaction('5️⃣',client.user), await message.remove_reaction('6️⃣', client.user), await message.remove_reaction('⬅️',client.user) # await message.remove_reaction('1️⃣', user), await message.remove_reaction('2️⃣', user), await message.remove_reaction('3️⃣', user), await message.remove_reaction('4️⃣', user), await message.remove_reaction('5️⃣', user), await message.remove_reaction('6️⃣', user), await message.remove_reaction('⬅️', user)

                        if reaction == '1️⃣':
                            await self.curusers[user.id][1].send('Понедельник ДЗ')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '2️⃣':
                            await self.curusers[user.id][1].send('Вторник ДЗ')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '3️⃣':
                            await self.curusers[user.id][1].send('Среда ДЗ')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '4️⃣':
                            await self.curusers[user.id][1].send('Четверг ДЗ')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '5️⃣':
                            await self.curusers[user.id][1].send('Пятница ДЗ')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '6️⃣':
                            await self.curusers[user.id][1].send('Суббота ДЗ')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Homework_menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)
                    elif self.curusers[user.id][0] == ' ':
                        deletion = await message.remove_reaction('🔄', client.user), await message.remove_reaction('‼️', client.user), await message.remove_reaction('📅',client.user), await message.remove_reaction('⬅️', client.user) # await message.remove_reaction('🔄',user), await message.remove_reaction('‼️', user), await message.remove_reaction('📅', user), await message.remove_reaction('⬅️',user)

                        if reaction == '🔄':
                            await self.curusers[user.id][1].send('Все оценки')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '‼️':
                            await self.curusers[user.id][1].send('Оценки самматив')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '📅':
                            await self.curusers[user.id][1].send('Оценки недавно')
                            deletion
                            del (self.curusers[user.id])
                        elif reaction == '⬅️':
                            self.curusers[user.id] = 'Menu', self.curusers[user.id][1], self.curusers[user.id][2]
                            deletion
                            await self.status_change(user.id)

    async def status_change(self, user):
        message = self.curusers[user][2]
        channel = self.curusers[user][1]
        if self.curusers[user][0] == 'Homework_menu':
            await message.edit(content = 'Choose an option below. 🏚️ for tomorrow\'s homework , 🏘️ for entire week homework, 🔢 for a specific day homework, ⬅️to go back')
            await message.add_reaction('🏚️')
            await message.add_reaction('🏘️')
            await message.add_reaction('🔢')
            await message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Homework_choice':
            await message.edit(content='Choose an option below. :one: for Monday, :two: for Tuesday, :three: for Wednesday, :four: for Thursday, :five: for Friday, :six: for Saturday, ⬅️to go back')
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
            await message.add_reaction('3️⃣')
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
            await message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Schedule_menu':
            await message.edit(content='Choose an option below. ▶️ for  today\'s schedule, 📅 for entire week schedule, 🔢 for a specific day schedule, ⬅️to go back')
            await message.add_reaction('▶️')
            await message.add_reaction('📅')
            await message.add_reaction('🔢')
            await message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Schedule_choice':
            await message.edit(content='Choose an option below. :one: for Monday, :two: for Tuesday, :three: for Wednesday, :four: for Thursday, :five: for Friday, :six: for Saturday, :arrow_left: to go back')
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
            await message.add_reaction('3️⃣')
            await message.add_reaction('4️⃣')
            await message.add_reaction('5️⃣')
            await message.add_reaction('6️⃣')
            await message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Grades':
            await message.edit(content='Choose an option below. 🔄 for  all marks, ‼️ for summative marks, 📅 for recent marks, ⬅️ to go back')
            await message.add_reaction('🔄')
            await message.add_reaction('‼️')
            await message.add_reaction('📅')
            await message.add_reaction('⬅️')
        elif self.curusers[user][0] == 'Holidays':
            await channel.send('каникулы :D')
            del (self.curusers[user])
        elif self.curusers[user][0] == 'Menu':
            id = int(user)
            name = str(await client.fetch_user(id))
            a = name.find('#')
            await message.edit(content='Greetings, ' + name[:a] + '. Choose an option below. :calendar_spiral: for Schedule, 🏡 for Homework, 🔢 for grades and 🌲 for holidays')
            await message.add_reaction('🗓️')
            await message.add_reaction('🏡')
            await message.add_reaction('🔢')
            await message.add_reaction('🌲')
        else:
            message.edit('Something wrong happened, please contact @yab1ch on telegram')
            print('Problem for ' + str(user) + 'his state is ' + str(self.curusers[user][0]))


if __name__ == "__main__":
    client = Myclient()
    client.run(os.getenv('TOKEN'))
