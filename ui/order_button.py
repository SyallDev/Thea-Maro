from typing import Any

import discord
from discord import ui
from discord.utils import get

from ui.order_form import DropdownView


class OrderButton(ui.Button):
    def __init__(self):
        super().__init__()
        self.label = "New order"

    async def callback(self, interaction: discord.Interaction) -> Any:
        guild = interaction.guild
        ordersCategory = get(guild.categories, name="orders")
        orderChannelName = "order-" + interaction.user.name
        if not (get(ordersCategory.text_channels, name=orderChannelName)):
            orderChannel = await guild.create_text_channel(name=orderChannelName, category=ordersCategory)
            await interaction.response.send_message("Please head to {} to complete your order.".format(orderChannel.mention), ephemeral=True)
            await orderChannel.send(embed=DropdownView.buildOrderEmbed(0, 0, 0))
            await orderChannel.send(view=DropdownView(orderChannel))

        else:
            await interaction.response.send_message("You already have an open order! Please close it before submitting a new order.", ephemeral=True)

class OrderButtonView(ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(OrderButton())