import discord
from my_commands import test

my_commands={
    'test':test.test
    }

async def response(self,message):
        # make sure message author is mot bot
        if message.author == self.user:
            return
        
        # executing command
        if message.content.startswith('//'):
            test_command = message.content.split(" ")[0].replace("//","")

            if test_command in my_commands:
                await my_commands[test_command](message)
            else:
                await message.channel.send('The command is not exist ! ')



        print(message.content)

async def print_ready(self):
    print('bot is ready!')
