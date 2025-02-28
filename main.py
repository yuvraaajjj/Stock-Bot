from typing import Final
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")

#code to search for all the .py files inside the cogs directory
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())

# -------------------------------------------------------------------------------------------------------------

watchlist = {}

@client.command(name='addwatch',help='This command is used to add tickers to your watchlist.')
async def add_to_watchlist(ctx, ticker: str):
    try:
        user_id = ctx.author.id
        user = ctx.author

        if user_id not in watchlist:
            watchlist[user_id] = []

        watchlist[user_id].append(ticker)
        await user.send(f'Added {ticker} to your watchlist...')

    except Exception as e:
        await ctx.send(f'{ticker} already in your watchlist...')

@client.command(name='delwatch')
async def del_from_watchlist(ctx, ticker: str):
    user_id = ctx.author.id
    user = ctx.author

    if user_id in watchlist:
        watchlist[user_id].remove(ticker)
        await user.send(f'{ticker} has been removed from your watchlist...')
    else:
        await ctx.send(f'{ticker} was already not present in your watchlist....')

@client.command(name='showatch')
async def show_watchlist(ctx):
    user_id = ctx.author.id
    user = ctx.author

    if user_id in watchlist:
        watchlists = watchlist[user_id]
        if watchlists:
            watchlists_str = ', '.join(watchlists)
            await user.send(f"--------------------\n Your watchlist: {watchlists_str}\n -----------------------")
        else:
            await ctx.send("Your watchlist is empty.")
    else:
        await ctx.send("You don't have a watchlist. Add symbols using `!add_to_watchlist`.")

