from discord.ext import commands
from discord.ui import View, Select
import os
import discord
import asyncio
#from ask import __train_agent, __path_creator


class Reload(commands.Cog):
    """Cog for /refresh command on FaqAiBot
    """
    
    def __init__(self, bot) -> None:
        self.bot = bot
        print("Reload Loaded\n")

    @commands.hybrid_command(name='reload', description="Reload the bot's cogs!", guild_ids=[1072948383955816459])
    async def reload(self, ctx: discord.Interaction):
        print("called reload")
        embed = discord.Embed(
            title = "Reloading cogs...",
            color= 0x808080,
            timestamp=ctx.message.created_at
        )
        for file in os.listdir("./cogs/"):
            print(f"searching cogs...{file}\n")
            if file == 'ask.py' and not file.startswith("_"):
                try:
                    print(f"unloading: {file}")
                    await self.bot.unload_extension(f"cogs.{file[:-3]}")
                    await self.bot.load_extension(f"cogs.{file[:-3]}")
                    embed.add_field(
                        name = f"Reloaded: `{file}`",
                        value = '\uFEFE'
                    )
                except Exception as e:
                    print(f"Exception: {e}")
                    embed.add_field(
                        name = f"Failed: `{file}`",
                        value = e
                    )
                await asyncio.sleep(1)
            continue
        await ctx.send(embed=embed, ephemeral=True)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Reload(bot))