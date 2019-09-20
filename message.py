# Work with Python 3.6
import discord
import time
from playsound import playsound
playsound('audio.mp3')

TOKEN = 'NTQwODI3NjIwOTA0Nzk2MTcx.XYEYkA.Ti89SBFWdndBMMzxgFNsNgindrI'

client = discord.Client()
print()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await sendMsg()
    await client.close()



@client.event
async def sendMsg():
    channel = client.get_channel(389400337506631681)
    await channel.send('fuck')


while True:
    time.sleep(10)
    client.run(TOKEN)











