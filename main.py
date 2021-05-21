import discord
import os
import message_text_async


class MyClient(discord.Client):
    # test to echo
    async def on_message(self, message):
        await message_text_async.response(self, message)

    # print ready after bot turn on
    async def on_ready(self):
        await message_text_async.print_ready(self)


if __name__ == "__main__":
    assert os.path.isfile("TOKEN")
    with open("TOKEN", "r") as file:
        TOKEN = file.read().strip()

    client = MyClient()
    client.run(TOKEN)
