"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.2.0
"""
from discord.ext import commands
from discord.ext.commands import Context

from ui.order_button import *


# Here we name the cog and create a new class for the cog.
class Order(commands.Cog, name="order"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="createorderform",
        description="This will create a button that clients will click to begin an order.",
    )
    async def createorderform(self, context: Context) -> None:
        """
        This will create a button that allows orders to be submitted from.

        :param context: The application command context.
        """

        await context.send(view=OrderButtonView())


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Order(bot))