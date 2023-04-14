from discord.ext import commands
import discord

from trainAgent import agent

class Ask(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        print("Ask Loaded\n")

    @commands.hybrid_command(name='ask', description="Ask the bot a question!", guild_ids=[1072948383955816459])
    async def ask(self, interaction: discord.Interaction, question:str):
        response = agent.request(question)
        await interaction.reply(f"Hi, {interaction.author.mention}! {response}", ephemeral=True)

    @ask.error
    async def ask_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.errors.MissingRole):
            await ctx.reply(f"You do not have permission to do that!", ephemeral=True)
        else:
            await ctx.reply(f"Sorry {ctx.author.mention},I do not understand! Please ping the Professor!", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Ask(bot))