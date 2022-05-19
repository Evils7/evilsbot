import discord
from utils import lists
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def userinfo(self, ctx,*,member:discord.User=None):
        flags = dict(member.public_flags).items()
        final = [k for k, v in flags if v]
        a = [badges[str(b)] for b in final if b in lists.badges]
        if not member:
            member = ctx.author
        embed = discord.Embed(color=self.bot.color)
        embed.set_author(name=f"{str(member)}", icon_url=member.avatar_url)
        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Badges", value=a)
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Misc(bot))
