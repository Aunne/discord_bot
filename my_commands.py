import asyncio


class MyCommands:

    # test command echo
    async def test(message):
        await message.channel.send('Yes Here!!')

    # clearing message
    async def clearmsg(message):
        
        try:
            clear_number = int(message.content.split(" ", 1)[1])

            queue = []
            async for history_msg_obj in message.channel.history(limit=clear_number+1):
                _task = history_msg_obj.delete()
                queue.append(_task)

            await asyncio.wait(queue)

        except ValueError:
            await message.channel.send(f'\"{message.content.split(" ", 1)[1]}\" is not a number!')
