import discord
from discord import ui


class Dropdown(ui.Select):
    def __init__(self, id, placeholder, itemName, maxValue):
        formOptions = []
        for i in range(0, maxValue + 1):
            formOptions.append(discord.SelectOption(label="{} {}".format(str(i), itemName)))
        super().__init__(custom_id=id, placeholder=placeholder, options=formOptions)

    async def callback(self, interaction: discord.Interaction):
        messages = [message async for message in interaction.channel.history(oldest_first=True)]
        await messages[0].edit(embed=self.view.getUpdatedEmbed())
        await interaction.response.defer()

class SubmitOrderButton(ui.Button):
    def __init__(self):
        super().__init__()
        self.label = "Submit order"
        self.style = discord.ButtonStyle.primary

    async def callback(self, interaction: discord.Interaction):
        parentView = self.view
        dropdowns = []
        # prevent empty form being submitted with boolean check
        valid = False
        for each in parentView.children:
            if isinstance(each, Dropdown):
                if len(each.values) > 0:
                    valid = True
                dropdowns.append(each)

        if valid == True:
            self.disabled = True
            values = []
            for each in dropdowns:
                each.disabled = True
                try:
                    values.append(each.values[0].split()[0])
                except IndexError:
                    values.append("0")
            await interaction.response.edit_message(view=parentView)
            msg = await self.view.getOrderEmbedMessage()
            await msg.edit(embed=DropdownView.buildOrderEmbed(values[0], values[1], values[2], True))
        else:
            await interaction.response.send_message("You must select at least one item to submit an order!", ephemeral=True)


class CancelOrderButton(ui.Button):
    def __init__(self):
        super().__init__()
        self.label = "Cancel order"
        self.style = discord.ButtonStyle.danger

    async def callback(self, interaction: discord.Interaction):
        await interaction.channel.delete(reason="Order cancelled by client")

class DropdownView(ui.View):
    @staticmethod
    def buildOrderEmbed(btAmount, locoAmount, flatbedAmount, submitted=False):
        embed = discord.Embed(title="ERG client order form").set_thumbnail(url="https://files.catbox.moe/e8uitu.webp")
        embed.add_field(name="BT", value="{}x".format(btAmount))
        embed.add_field(name="Locomotive", value="{}x".format(locoAmount))
        embed.add_field(name="Flatbed car", value="{}x".format(flatbedAmount))
        embed.add_field(name="Status", value="Submitted" if submitted is True else "Not submitted", inline=False)
        return embed

    async def getOrderEmbedMessage(self):
        messages = [message async for message in self.channel.history(oldest_first=True)]
        return messages[0]

    def getUpdatedEmbed(self):
        dropdowns = []
        for each in self.children:
            if isinstance(each, Dropdown):
                dropdowns.append(each)

        values = []
        for each in dropdowns:
            try:
                values.append(each.values[0].split()[0])
            except IndexError:
                values.append("0")
        return DropdownView.buildOrderEmbed(values[0], values[1], values[2])

    def __init__(self, channel):
        super().__init__()
        self.channel = channel

        self.add_item(Dropdown("btAmount", "How many BT?", "BT", 4))
        self.add_item(Dropdown("locoAmount", "How many locomotives?", "Locomotive(s)", 2))
        self.add_item(Dropdown("flatbedAmount", "How many flatbed cars?", "Flatbed(s)", 14))

        self.add_item(CancelOrderButton())
        self.add_item(SubmitOrderButton())