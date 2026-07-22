import discord
from discord.ext import commands
from discord import app_commands


class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="userinfo",
        description="يعرض معلومات عن عضو"
    )
    async def userinfo(
        self,
        interaction: discord.Interaction,
        member: discord.Member = None
    ):

        if member is None:
            member = interaction.user

        embed = discord.Embed(
            title=f"👤 معلومات {member}",
            color=member.color if member.color != discord.Color.default() else discord.Color.blurple()
        )

        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(
            name="🆔 ID",
            value=member.id,
            inline=True
        )

        embed.add_field(
            name="🤖 بوت؟",
            value="نعم" if member.bot else "لا",
            inline=True
        )

        embed.add_field(
            name="📅 إنشاء الحساب",
            value=f"<t:{int(member.created_at.timestamp())}:F>",
            inline=False
        )

        embed.add_field(
            name="📥 انضم للسيرفر",
            value=f"<t:{int(member.joined_at.timestamp())}:F>",
            inline=False
        )

        embed.add_field(
            name="🎭 أعلى رتبة",
            value=member.top_role.mention,
            inline=False
        )

        embed.set_footer(text="Shadow Bot")

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(UserInfo(bot))