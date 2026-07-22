import discord
from discord.ext import commands
from discord import app_commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="clear",
        description="يحذف عدد من الرسائل"
    )
    @app_commands.describe(amount="عدد الرسائل المراد حذفها")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear(
        self,
        interaction: discord.Interaction,
        amount: app_commands.Range[int, 1, 100]
    ):

        await interaction.response.defer(ephemeral=True)

        deleted = await interaction.channel.purge(limit=amount)

        await interaction.followup.send(
            embed=discord.Embed(
                title="🗑️ Messages Deleted",
                description=f"تم حذف **{len(deleted)}** رسالة.",
                color=discord.Color.green()
            ),
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Clear(bot))