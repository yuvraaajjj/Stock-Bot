from discord.ext import commands

class Del(commands.Cog):

    """Deletes tickers from your watchlist. USE: !delwatch [TICKER]"""

    def __init__(self,client):
        self.client = client

async def setup(client):
    await client.add_cog(Del(client))