import discord
from discord.ext import commands
from discord import app_commands


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="serverinfo",
        description="يعرض معلومات السيرفر"
    )
    async def serverinfo(self, interaction: discord.Interaction):

        guild = interaction.guild

        embed = discord.Embed(
            title=f"📊 معلومات سيرفر {guild.name}",
            color=discord.Color.blurple()
        )

        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        embed.add_field(
            name="👑 المالك",
            value=guild.owner.mention,
            inline=True
        )

        embed.add_field(
            name="🆔 ID",
            value=guild.id,
            inline=True
        )

        embed.add_field(
            name="👥 الأعضاء",
            value=guild.member_count,
            inline=True
        )

        embed.add_field(
            name="💬 الرومات",
            value=len(guild.channels),
            inline=True
        )

        embed.add_field(
            name="😀 الإيموجيات",
            value=len(guild.emojis),
            inline=True
        )

        embed.add_field(
            name="🎭 الرتب",
            value=len(guild.roles),
            inline=True
        )

        embed.set_footer(text="Shadow Bot")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(ServerInfo(bot))