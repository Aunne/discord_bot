import asyncio


class MyCommands:
    async def test(message):
        # test command echo
        await message.channel.send('Yes Here!!')

    
    async def clearmsg(message):
        # clearing message
        try:
            clear_number = int(message.content.split(" ", 1)[1])

            queue = []
            async for history_msg_obj in message.channel.history(limit=clear_number+1):
                _task = history_msg_obj.delete()
                queue.append(_task)

            await asyncio.wait(queue)

        except ValueError:
            await message.channel.send(f'\"{message.content.split(" ", 1)[1]}\" is not a number!')
