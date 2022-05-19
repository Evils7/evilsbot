import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def hierarchy(self, member):
        return member.guild.me.top_role > member.top_role and member != member.guild.owner


    @commands.command(help="Ban someone from guild")
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason:str=None):
        if not reason:
            reason = "No reason"
        if not self.hierarchy(member):
            return await ctx.send("You can't do this")
        await member.ban(reason=reason)
        await ctx.send(f"Banned `{member}`")



    @commands.command(help="Kick someone from guild")
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.guild_only()
    @commands.has_permissions(kick_members=True) 
    @commands.bot_has_guild_permissions(ban_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason:str = None):
        if not reason:
            reason = f"No reason"
        if not self.hierarchy(member):
            return await ctx.send("You can't do this")
        await member.kick(reason=f"{reason}")
        await ctx.send(f"{self.bot.succes}Kicked `{member}`")





def setup(bot):
    bot.add_cog(moderation(bot))
