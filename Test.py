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

    elif message.content.startswith(f'#hello'):
        await message.channel.send('''Hello there! I\'m ApeBot25000.
    Sorry but I really need to go to the bathroom... Please read my manual by typing #help while I'm away.''')

    elif message.content.startswith(f'#help'):
        await message.channel.send('Type $STOCK_NAME to get information')

    elif message.content.startswith(f'$'):
        stock = message.content.upper()
        response = requests.get(
            "https://finnhub.io/api/v1/quote?symbol=" + stock[1:len(stock)] + "&token=Finhub Api Key Goes Here")
        # print(response.json())
        x = json.loads(response.content)
        await message.channel.send('OPEN: ' + str(x["o"]) + '    CLOSE:' + str(x["c"]))



client.run('Your Discord Bot Key Goes Here')
