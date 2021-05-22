import discord
import os
import message_text_async


class MyClient(discord.Client):
    async def on_message(self, message):
        # test to echo
        await message_text_async.response(self, message)

    
    async def on_ready(self):
        # print ready after bot turn on
        await message_text_async.print_ready(self)


if __name__ == "__main__":
    assert os.path.isfile("TOKEN")
    with open("TOKEN", "r") as file:
        TOKEN = file.read().strip()

    client = MyClient()
    client.run(TOKEN)
