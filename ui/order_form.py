import discord
from discord import ui

class Dropdown(ui.Select):
    def __init__(self, id, placeholder, itemName, maxValue):
        formOptions = []
        for i in range(0, maxValue + 1):
            formOptions.append(discord.SelectOption(label="{} {}".format(str(i), itemName)))
        super().__init__(custom_id=id, placeholder=placeholder, options=formOptions)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("Done")

class SubmitOrderButton(ui.Button):
    def __init__(self):
        super().__init__()
        self.label = "Submit order"
        self.style = discord.ButtonStyle.primary


class CancelOrderButton(ui.Button):
    def __init__(self):
        super().__init__()
        self.label = "Cancel order"
        self.style = discord.ButtonStyle.danger

    async def callback(self, interaction: discord.Interaction):
        await interaction.channel.delete(reason="Order cancelled by client")

class DropdownView(ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown("btAmount", "How many BT?", "BT", 4))
        self.add_item(Dropdown("locoAmount", "How many locomotives?", "Locomotive(s)", 2))
        self.add_item(Dropdown("flatbedAmount", "How many flatbed cars?", "Flatbed(s)", 14))

        self.add_item(CancelOrderButton())
        self.add_item(SubmitOrderButton())