from discord.ext import commands
import discord
from discord.ui import View, Select

class HelpSelect(Select):
    def __init__(self, bot:commands.Bot):
        super().__init__(
            placeholder='Choose a category',
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

        commands_mixer = [i for i in cog.walk_commands()]

        commands_mixer.append(i for i in cog.walk_app_commands())

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

class Utils(commands.Cog):
    """The description for Utils goes here."""

    def __init__(self, bot):
        self.bot = bot




    @commands.hybrid_command(name="help", descripition = "Show a list of commands!")
    async def help(self,ctx:commands.Context):
        embed = discord.Embed(
            title="Help Command",
            description="This is a help command"
        )
        view = View().add_item(HelpSelect(self.bot))
        await ctx.send(embed=embed, view = view)

    

    # @commands.hybrid_command(name='test', description = "Just a test!")
    # async def test(self, ctx:commands.Context):
    #     await ctx.send(10)

    @commands.hybrid_command(name='ask', description='Ask the Bot a question!')
    async def test(self, ctx:commands.Context):
        embed = discord.Embed(
            title="Ask Command",
            description="Ask the Bot a question!"
        )
        view = View().add_item(HelpSelect(self.bot))
        await ctx.send(embed=embed, view = view)


async def setup(bot):
    await bot.add_cog(Utils(bot))
