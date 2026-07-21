import discord
from discord.ext import commands
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
    name="commands",
    description="عرض جميع أوامر البوت"
    )
    async def help_command(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🌑 Shadow Bot",
            description="أهلاً بك في **Shadow Bot**",
            color=0x2F3136
        )

        embed.add_field(
            name="📋 الأوامر",
            value="`/ping`\n`/commands`",
            inline=False
        )

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    print("✅ Help Cog Loaded")
    await bot.add_cog(HelpCog(bot))