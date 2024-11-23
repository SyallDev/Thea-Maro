import discord
from discord import ui


class Dropdown(ui.Select):
    def __init__(self, id, placeholder, itemName, maxValue):
        formOptions = []
        for i in range(0, maxValue + 1):
            formOptions.append(discord.SelectOption(label="{} {}".format(str(i), itemName)))
        super().__init__(custom_id=id, placeholder=placeholder, options=formOptions)

class DropdownView(ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown("btAmount", "How many BT?", "BT", 4))
        self.add_item(Dropdown("locoAmount", "How many locomotives?", "Locomotive(s)", 2))