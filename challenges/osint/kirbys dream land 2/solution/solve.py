import discord

intents = discord.Intents.none()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    async for guild in client.fetch_guilds(limit=150):
        if guild.id != 1313393081017434162: continue
        channel = await guild.fetch_channel(1313393293748342794)
        last_id = channel.last_message_id
        message = await channel.get_partial_message(last_id).fetch()
        print(message.content)

    print(f'We have logged in as {client.user}')

client.run('MTMxMzM5MTY0ODk0Mzc3MTcxOA.Gfp792.riN2ISrFm3mE10wrK3XPZuZQl6VgeAdQzXKAgY')