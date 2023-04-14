from discord.ext import commands
from discord.ui import View, Select
import discord

class HelpSelect(Select):
    def __init__(self, bot:commands.Bot):
        super().__init__(
            placeholder='Choose a command',
            options=[
                discord.SelectOption(
                    label=cog_name,description=cog.__doc__
                )for cog_name, cog in bot.cogs.items() if cog.__cog_commands__ and cog_name not in ['Jishaku'] #?? was ist dis??
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
    def __init__(self, bot):
        self.bot = bot
        print("Help Loaded\n")

    @commands.hybrid_command(name="help", descripition = "Show a list of commands!", guild_ids = [1072948383955816459])
    async def help(self,ctx:commands.Context):
        embed = discord.Embed(
            title="Help Command",
            description="List of Commands!"
        )
        view = View(timeout=60).add_item(HelpSelect(self.bot))
        await ctx.send(embed=embed, view = view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Help(bot))
