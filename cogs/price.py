import yfinance as yf
from discord.ext import commands

class Price(commands.Cog):

    """Shows the financial details of the stock. USE: !price [TICKER]"""

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("price is ready.")

    @commands.command()
    async def price(self, ctx, ticker: str):
        try:
            user = ctx.author

            stock_info = yf.Ticker(ticker)
            stock_data = stock_info.info

            ticker = stock_data.get('symbol', 'N/A')
            company_name = stock_data.get('shortName', 'N/A')
            currency = stock_data.get('currency', 'N/A')
            current_price = stock_data.get('currentPrice', 'N/A')
            dividend_rate = stock_data.get('dividendRate', 'N/A')
            open = stock_data.get('open', 'N/A')
            close = stock_data.get('previousClose', 'N/A')
            day_high = stock_data.get('dayLow', 'N/A')
            day_low = stock_data.get('dayHigh', 'N/A')
            fifty_two_high = stock_data.get('fiftyTwoWeekHigh', 'N/A')
            fifty_two_low = stock_data.get('fiftyTwoWeekLow', 'N/A')
            recommendation = stock_data.get('recommendationKey', 'N/A')

            await user.send(
                f'----------------------\nStock Info for {ticker} ({company_name}):\n Currency - {currency}\n Current Price - {current_price}\n'
                f' Dividend Rate - {dividend_rate}\n Market Open Price - {open}\n'
                f'Previous Market Close Price - {close}\n Day High - {day_high}\n Day Low - {day_low}\n '
                f'52 Week High - {fifty_two_high}\n 52 Week Low - {fifty_two_low}\n Recommendation - {recommendation}\n -----------------------')

        except Exception as e:
            await ctx.send(f'Error fetching Price info of {ticker}: {e}')

async def setup(client):
    await client.add_cog(Price(client))