import discord
from discord.ext import commands
import yfinance as yf

class Info(commands.Cog):

    """Gives information about the stock. USE: !stockinfo [TICKER]"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("info is ready.")

    @commands.command()
    async def stockinfo(self, ctx, ticker: str):

     try:
        user = ctx.author

        stock_info = yf.Ticker(ticker)
        stock_data = stock_info.info

        ticker = stock_data.get('symbol','N/A')
        company_name = stock_data.get('shortName','N/A')
        industry = stock_data.get('industry','N/A')
        sector = stock_data.get('sector', 'N/A')
        exchange = stock_data.get('exchange','N/A')
        currency = stock_data.get('financialCurrency','N/A')
        earnings_growth = stock_data.get('earningGrowth','N/A')
        revenue_per = stock_data.get('revenuePerShare','N/A')
        total_revenue = stock_data.get('totalRevenue','N/A')
        total_debt = stock_data.get('totalDebt','N/A')

        await user.send(f'----------------------\nStock Info for {ticker} ({company_name}):\n Industry - {industry}\n Sector - {sector}\n '
                        f'Exchange - {exchange}\n Currency - {currency}\n'
                        f' Company Earnings Growth - {earnings_growth}\n Revenue Per Share - {revenue_per}\n '
                        f'Company Total Revenue - {total_revenue}\n'
                        f'Company Total Debt - {total_debt}\n ---------------------')

     except Exception as e:
        await ctx.send(f'Error fetching stock data for {ticker}: {e}')

async def setup(client):
    await client.add_cog(Info(client))