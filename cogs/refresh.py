from discord.ext import commands
from discord.ui import View, Select
import discord
#from ask import __train_agent, __path_creator


class Refresh(commands.Cog):
    """Cog for /refresh command on FaqAiBot
    """
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
        print("Refresh Loaded\n")

    @commands.hybrid_command(name="refresh", description = "Refresh the Bot!", guild_ids = [1072948383955816459])
   
    async def refresh(self, ctx:commands.Context) -> None:
        embed = discord.Embed(
            title="Refresh Command",
            description="Refresh the Bot!"
        )
        await ctx.reply("Refreshed!", ephemeral = True)
        
    
    @refresh.error
    async def refresh_error(self, ctx:commands.Context, error:Exception) -> None:
        if isinstance(error, commands.errors.MissingAnyRole):
            await ctx.reply(f"You do not have permission to do that!", ephemeral=True)
        else:
            print(f"Error: {error}")
            await ctx.reply(f"{ctx.author.mention}, refresh did not work! Please try again later!", ephemeral=True)

    async def _reload(self, *, module : str):
        """Reloads a module."""
        try:
            self.bot.unload_extension(module)
            print("Unloaded")
            self.bot.load_extension(module)
            print("Loaded")

        except Exception as e:
            await self.bot.say('didnt work \n',ephemeral=True)
            await self.bot.say('{}: {}'.format(type(e).__name__, e),ephemeral=True)
        else:
            await self.bot.say(f'Refresh Worked\n',ephemeral=True)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Refresh(bot))