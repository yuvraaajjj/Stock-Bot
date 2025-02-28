from discord.ext import commands

class Show(commands.Cog):

    """Shows your watchlist. USE: !showatch"""

    def __init__(self,client):
        self.client = client

async def setup(client):
    await client.add_cog(Show(client))