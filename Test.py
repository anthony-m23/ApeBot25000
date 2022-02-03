import discord
import requests
import json

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} is now online!')


@client.event
async def on_message(message):
    # make sure bot doesn't respond to it's own messages to avoid infinite loop
    if message.author == client.user:
        return

    if message.content.startswith(f'$stock'):
        await message.channel.send('What Stock:')

    elif message.content.startswith(f'$hello'):
        await message.channel.send('''Hello there! I\'m ApeBot25000.
    Sorry but I really need to go to the bathroom... Please read my manual by typing $help or $commands while I'm away.''')

    elif message.content.startswith(f'$help'):
        await message.channel.send('Not yet implemented Bitch')
    else:
        if message.content.startswith(f'$'):
            stock = message.content
            response = requests.get(
                "https://finnhub.io/api/v1/quote?symbol=" + stock[1:len(stock)] + "&token=brmhla7rh5re15om4so0")
            # print(response.json())
            x = json.loads(response.content)

            await message.channel.send('OPEN: ' + str(x["o"]) + '    CLOSE:' + str(x["c"]))


client.run('OTM4MzExMDU1OTg0MTg5NDgx.YfocRA.yIlE9PuA5YC1sxv-fW52wM_N9YM')
