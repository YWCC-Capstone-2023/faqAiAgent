from discord.ext import commands
import discord

from trainAgent import agent

class Ask(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        print("Ask Loaded\n")

    @commands.hybrid_command(name='ask', description="Ask the bot a question!", guild_ids=[1072948383955816459])
    async def ask(self, interaction: discord.Interaction, question:str):
        
        print('\n')
        print(f"interaction : {interaction}")
        print(f"Q: {question}")
        response = agent.request(question)
        print(f"response: {response}")
        print('\n')

        await interaction.reply(f"Hi, {interaction.author.mention}! {response}", ephemeral=True)

    @ask.error
    async def ask_error(self, interaction:discord.Interaction, error):
            await interaction.reply(f"Sorry {interaction.author.mention},I do not understand! Please ping the Professor!", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Ask(bot))