import discord
from my_commands import MyCommands

commands_lib = {
    'test': MyCommands.test,
    'clearmsg': MyCommands.clearmsg
}


async def response(self, message):
    if message.author == self.user:
        # make sure message author is mot bot
        return

    
    if message.content.startswith('//'):
        # make sure message author is mot bot
        test_command = message.content.split(" ")[0].replace("//", "")

        if test_command in commands_lib:
            await commands_lib[test_command](message)
        else:
            await message.channel.send('The command is not exist ! ')

async def print_ready(self):
    # print ready when bot is ready
    print('bot is ready!')
