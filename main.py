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
            help_command=None,
            intents=intents
        )

    async def setup_hook(self):

        # تحميل جميع الـ Cogs
        for root, _, files in os.walk("cogs"):
            for file in files:
                if not file.endswith(".py"):
                    continue

                if file == "__init__.py":
                    continue

                module = os.path.join(root, file)[:-3].replace(os.sep, ".")

                try:
                    await self.load_extension(module)
                    print(f"✅ Loaded {module}")
                except Exception as e:
                    print(f"⚠️ Skipped {module}: {e}")

        print("=" * 50)
        print("✅ All Cogs Loaded")
        print("=" * 50)

        guild = discord.Object(id=GUILD_ID)

        synced = await self.tree.sync(guild=guild)

        print(f"✅ Synced {len(synced)} Commands")

    async def on_ready(self):
        print("=" * 50)
        print(f"✅ Logged in as {self.user}")
        print("🚀 Shadow Bot is Online!")
        print("=" * 50)


bot = ShadowBot()
bot.run(TOKEN)