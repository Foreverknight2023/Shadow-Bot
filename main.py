import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from config import TOKEN, GUILD_ID

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class ShadowBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        # تحميل جميع ملفات cogs
        for filename in os.listdir("./cogs"):
            if not filename.endswith(".py"):
                continue

            try:
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"✅ Loaded {filename}")
            except Exception as e:
                print(f"⚠️ Skipped {filename}: {e}")

        print("✅ All Cogs Loaded")

        synced = await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"✅ Synced {len(synced)} Commands")

    async def on_ready(self):
        print("=" * 50)
        print(f"✅ Logged in as {self.user}")
        print("🚀 Shadow Bot is Online!")
        print("=" * 50)


bot = ShadowBot()
bot.run(TOKEN)