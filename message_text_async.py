import discord
from my_commands import MyCommands

commands_lib = {
    'test': MyCommands.test,
    'clearmsg': MyCommands.clearmsg
}


async def response(self, message):
    # make sure message author is mot bot
    if message.author == self.user:
        return

    # executing command
    if message.content.startswith('//'):
        test_command = message.content.split(" ")[0].replace("//", "")

        if test_command in commands_lib:
            await commands_lib[test_command](message)
        else:
            await message.channel.send('The command is not exist ! ')


async def print_ready(self):
    print('bot is ready!')
