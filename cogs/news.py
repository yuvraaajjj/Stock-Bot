import discord
from discord.ext import commands
import requests

class News(commands.Cog):

    """Gives news about any topic. USE: !news topic(without spaces)"""

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("news ready.")

    @commands.command()
    async def news(self, ctx, ticker):
        base_url = 'https://newsapi.org/v2/everything'

        # Define parameters for the request
        params = {
            'q': ticker,  # User-specified topic
            'apiKey': 'b537a0cab4904884a43b638c181561eb'
        }

        # Make the request
        response = requests.get(base_url, params=params)

        # Parse and print the response
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data['articles']
            list = []
            for article in articles:
                list.append("TITLE: " + article['title'])
                list.append("URL: " + article['url'])
                list.append("DATE OF PUBLISHING: " + article['publishedAt'])
                list.append(
                    "--------------------------------------------------------------------------------------------------------")

            for i in range(40):
                await ctx.send(list[i])

        else:
            await ctx.send(f"Error: {response.status_code}")

        api_key = 'b537a0cab4904884a43b638c181561eb'

        user_topic = input("Enter the ticker value: ")

        await ctx.send(self.news(api_key, user_topic))

async def setup(client):
    await client.add_cog(News(client))
