import discord
from discord.ext import commands

class Help(commands.Cog):# setting up our cog

    """To access Australian stocks - ticker.AX
       To access Canadian stocks - ticker.TO
       To access Indian stocks - ticker.NS(for NSE exchange) or ticker.BO(for Bombay exchange
       To access UK stocks - ticker.L
       To access China stocks - ticker.SS
       To access South Korea stocks - ticker.KS or ticker.TQ
       To access Germany stocks - ticker.DE"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("help ready.")

    @commands.command()
    async def Help(self,ctx,*cog): #fuction to display the list of cogs and their description

        if not cog:
            embed = discord.Embed(color=0x6f03fc)

            cogs_desc = ''
            for x in self.client.cogs:
                cogs_desc += ('**{}** - {}'.format(x,self.client.cogs[x].__doc__)+'\n')
            embed.add_field(name="Cogs",value=cogs_desc[0:len(cogs_desc)-1],inline=False)
            await ctx.send(embed=embed)

        else:
            found = False
            for x in self.client.cogs:
                for y in cog:
                    if x == y:
                        embed = discord.Embed(color=0x6f03fc)
                        scog_info = ''
                        for c in self.client.get_cog(y).get_commands():
                            if not c.hidden:
                                scog_info += f'**{c.name}** - {c.help}\n'
                            embed.add_field(name=f'{cog[0]} Module - {self.client.cogs[cog[0]].__doc__}',value=scog_info)
                            found = True

            if not found:
                for x in self.client.cogs:
                    for c in self.client.get_cog(x).get_commands():

                        if c.name == cog[0]:
                            embed = discord.Embed(color=0x6f03fc)
                            embed.add_field(name=f'{c.name} - {c.help}',value=f'Proper Syntax:\n{c.qualified_name} {c.signature}')

                    found = True
                if not found:
                    embed = discord.Embed(title = 'Error!',description='How do you use'+cog[0]+'?',color=0x6f03fc)

            else:
                await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))