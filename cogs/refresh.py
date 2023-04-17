from discord.ext import commands
from discord.ui import View, Select
import os
import discord
import asyncio
#from ask import __train_agent, __path_creator

class ReloadSelect(Select):
    def __init__(self, bot:commands.Bot):
        super().__init__(
            placeholder="Choose a command",
            options=[
                discord.SelectOption(
                    label = cog_name 
                )for cog_name, _ in bot.cogs.items()
            ]
        )
        self.bot = bot

    async def callback(self, interaction: discord.Interaction) -> None:
        cog = self.bot.get_cog(self.values[0])
        assert cog

        name = cog.__cog_name__.lower()

        embed = discord.Embed(
            title = f"Reloading {name}...",
            color= 0x808080,
            timestamp=interaction.message.created_at
        )

        for file in os.listdir("./cogs/"):
            
            if name in file and not file.startswith("_"):
                try:
                    allow_mentions = discord.AllowedMentions(everyone=True)
                    
                    await interaction.response.send_message(content = f"@everyone, the /{file[:-3]} function will be down for < 1 minute", allowed_mentions = allow_mentions)
                    
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
        await interaction.followup.send(f"The /{name} function is back up and running!")
        await interaction.response.send_message(embed=embed, ephemeral=True)

    
class Reload(commands.Cog):
    """Cog for /refresh command on FaqAiBot
    """
    
    def __init__(self, bot:commands.Bot) -> None:
        self.bot = bot
        print("Reload Loaded\n")

    @commands.hybrid_command(name='reload', description="Reload the bot's cogs!", guild_ids=[1072948383955816459])
    async def reload(self, ctx: discord.Interaction):
        embed = discord.Embed(
            title = "Reload",
            description="Select Which Command To Reload"
        )

        view = View().add_item(ReloadSelect(self.bot))

        await ctx.send(embed=embed, view=view, ephemeral=True)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Reload(bot))