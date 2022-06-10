"""
This is the most basic outline of a bot as you can get, with an example command to get you started. Make sure you've
read the README, and make sure to reference the docs at https://discordpy.readthedocs.io/en/stable/api.html
"""

import os

import discord.ext
from discord.ext import commands
from discord.ext.commands import Context

from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')  # Instantiate bot with command prefix - prefix can be changed here


# Having this command in your code is optional but highly recommended
@bot.event  # event tag is used to mark events - look in the API docs to see the available event functions
async def on_ready():  # When the bot is ready to start receiving commands, run this function
    """Will print "bot online" in the console when the bot is online"""

    print("Bot Online\n")


# Having this command in your code is *optional*
@bot.event
async def on_message(message: discord.Message):
    """When a message is sent, this event is triggered and this function will run

    :param message: The message that was sent
    """
    if message.author == bot.user:
        return

    await bot.process_commands(message)  # You HAVE to put this at the end, or it simply won't run


# Example command - EVERY command MUST have "ctx" as the first parameter: it holds the Context of the message
@bot.command()  # tag that marks commands - takes some optional kwargs, check the docs
async def ping(ctx: Context):
    """
    Simple command so that when you type "!ping" the bot will respond with "pong!"

    :param ctx: The Context (See https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=context#context)
    the message was called in
    """

    # Send "pong!" in the same channel the original message was sent (the same context, if you will)
    await ctx.send("pong!")


# Logs into bot
load_dotenv()  # Load the .env file
bot.run(os.getenv("TOKEN"))
