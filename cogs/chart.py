import discord
from discord.ext import commands
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import io

class Chart(commands.Cog):

    """Displays a chart of past 6 months. USE: !chart [TICKER]"""

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("chart ready.")

    @commands.command()
    async def chart(self, ctx, ticker: str):
        try:
            user = ctx.author

            stock_data = yf.Ticker(ticker)
            hist = stock_data.history(period='6mo')

            hist.to_csv('hist.csv')

            df = pd.read_csv('hist.csv')
            df['Date'] = pd.to_datetime(df['Date'], utc=True)

            # Save the modified DataFrame back to a CSV file
            df.to_csv('hist.csv', index=False)

            #         convert the dates into the month format
            df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d", utc=True)
            df['Month'] = df['Date'].dt.month
            df['Month'] = df['Month'].apply(lambda x: pd.Timestamp(year=2023, month=x, day=1).strftime('%B'))

            df['Mean'] = df.groupby('Month')['Close'].transform('mean')

            df.to_csv('hist.csv', index=False)

            data = pd.read_csv('hist.csv')

            x = data['Month']
            y = data['Mean']

            plt.figure(figsize=(15, 10))
            plt.plot(x, y)

            plt.title('History')
            plt.ylabel('Mean Close price')
            plt.xlabel('Months')

            image_stream = io.BytesIO()
            plt.savefig(image_stream, format='png')
            image_stream.seek(0)

            # Send the plot image to the server chat
            await user.send(file=discord.File(image_stream, 'plot.png'))


        except Exception as e:
            await ctx.send(f'Error fetching historical data for {ticker}: {e}')

async def setup(client):
    await client.add_cog(Chart(client))