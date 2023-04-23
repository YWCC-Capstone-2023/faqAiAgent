import os, logging, asyncio

from discord.ext import commands
import discord

#from ask import __train_agent, __path_creator

class ReloadSelect(discord.ui.Select):
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
            timestamp=interaction.message.created_at,
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
                        value = '\uFEFE',
                    )
                    
                except Exception as e:
                    print(f"Exception: {e}")
                    embed.add_field(
                        name = f"Failed: `{file}`",
                        value = e,
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

    @discord.app_commands.command(name='reload', description="Reload the bot's cogs!")
    async def refresh(self, interaction:discord.Interaction):
        try:
            if interaction.permissions.administrator:
                embed = discord.Embed(
                    title = "Reload",
                    description="Select Which Command To Reload",               
                )

                view = discord.ui.View().add_item(ReloadSelect(self.bot))

                await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
            else: 
                raise commands.errors.MissingPermissions(missing_permissions=['administrator'])
            
        except commands.errors.MissingPermissions as e:
            embed = discord.Embed(
                title = "You are missing the correct permission(s) to run this command!",
                description="",
                                        )

            await interaction.response.send_message(embed=embed, ephemeral=True)

    @refresh.error
    async def __refresh_error(self, ctx:commands.Context, error:Exception) -> None:
        logging.log(error)

        embed = discord.Embed(
            title='',
            description=f"Sorry {ctx.author.mention},something went wrong! Please try again...",
        )
        
        await ctx.reply(embed=embed, ephemeral = True)
    
async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(Reload(bot))