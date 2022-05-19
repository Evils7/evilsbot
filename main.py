import discord
from discord.ext import commands
import config
import json




token = ""
# Fill this area

class EvilsBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(config.prefix),
                         allowed_mentions=discord.AllowedMentions(everyone=False, roles=False, users=False),
                         case_insensitive=True)


        self.color = 0x00dcff
        self.remove_command("help")
        self.load_extension('jishaku')
        self.loop.create_task(self.startup())

    def run(self, *args, **kwargs):
        super().run(token)

    async def startup(self):
        await self.wait_until_ready()
        for extension in config.EXT:
            try:
                self.load_extension(extension)
                print(f'[EXTENSION] {extension} loaded')
            except Exception as e:
                print(f'[WARNING] Cannot load {extension}: {e}')
        print(f"{self.user.name.upper()} is ready")
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching,
                                      name=f"%help"))


bot = EvilsBot()
bot.run()
