from discord.ext import commands
from discord.ui import View, Select
import discord

class HelpSelect(Select):
    """Class to Generate Help Select Dropdown
    """
    def __init__(self, bot:commands.Bot):
        super().__init__(
            placeholder='Choose a command',
            options=[
                discord.SelectOption(
                    label=cog_name,description=cog.__doc__
                )for cog_name, cog in bot.cogs.items()
            ]
        )

        self.bot = bot



    async def callback(self, interaction: discord.Interaction) -> None:
        cog = self.bot.get_cog(self.values[0])
        assert cog
        commands_mixer = []
        
        for i in cog.walk_commands():
            commands_mixer.append(i)

        for i in cog.walk_app_commands():
            commands_mixer.append(i)

        embed = discord.Embed(
            title=f'{cog.__cog_name__} Commands',
            description='\n'.join(
                f'**{command.name}**: `{command.description}`'
                for command in commands_mixer
            )
        )
        await interaction.response.send_message(
            embed=embed,
            ephemeral=True
        )
        return await super().callback(interaction)

class Help(commands.Cog):
    """Cog for /help command on FaqAiBot
    """
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
        print("Help Loaded\n")



    @commands.hybrid_command(name="help", description="Show a list of commands!")
    async def help(self, ctx:commands.Context) -> None:
        embed = discord.Embed(
            title="Help",
            description="Need Help? Here's a List of Commands!",
            color=discord.Color.yellow()
        )
        view = View(timeout=60).add_item(HelpSelect(self.bot))
        await ctx.send(embed=embed, view = view, ephemeral=True)



async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Help(bot))
