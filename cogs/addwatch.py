from discord.ext import commands

class Add(commands.Cog):

    """Add tickers to watchlist. USE: !addwatch [TICKER]"""
    def __init__(self,client):
        self.client = client


async def setup(client):
    await client.add_cog(Add(client))