import discord
from discord.ext import commands

class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def stats(self, ctx):
        evils = self.bot.get_user(412254835849691146)
        embed = discord.Embed(color=self.bot.color)
        embed.description = f"→ Guilds: {len(self.bot.guilds)}\n"
        embed.description += f"→ Users: {len(self.bot.users)}\n"
        embed.description += f"→ Discord.py: {discord.__version__}\n"
        embed.description += f"→ Owner: {evils}"
        
        
        await ctx.send(embed=embed)

    @commands.command(hidden=True, pass_contex=True)
    async def help(self, ctx, *, command=None):
        pre = ctx.prefix
        footer = f"Do '{pre}help [command/cog]' for more information!"
        list_of_cogs = []
        walk_commands = []
        final_walk_command_list = []
        sc = []
        format = []
        try:
            for cog in self.bot.cogs:
                list_of_cogs.append(cog)
            if command:
                cmd = self.bot.get_command(command)
            else:
                cmd = None
            if not command:
                k = []
                for cog_name, cog_object in self.bot.cogs.items():
                    cmds = []
                    for cmd in cog_object.get_commands():
                        if not cmd.hidden:
                            cmds.append(f"`{cmd.name}`")
                    k.append(f'{cog_name}\n{", ".join(sorted(cmds))}\n')
                for wc in self.bot.walk_commands():
                    if not wc.cog_name and not wc.hidden:
                        if isinstance(wc, commands.Group):
                            walk_commands.append(wc.name)
                            for scw in wc.commands:
                                sc.append(scw.name)
                        else:
                            walk_commands.append(wc.name)
                for item in walk_commands:
                    if item not in final_walk_command_list and item not in sc:
                        final_walk_command_list.append(item)
                for thing in final_walk_command_list:
                    format.append(f"`{thing}`")
                k.append("\n" + ", ".join(sorted(format)))
                embed=discord.Embed(colour=self.bot.color, description=f"`[] or <> cannot be used in commands`\n\nModules:\n<:mod:742734928244113469> Moderation")
                embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=embed)
            elif command in list_of_cogs:
                i = []
                cog_doc = self.bot.cogs[command].__doc__ or " "
                for cmd in self.bot.cogs[command].get_commands():
                    if not cmd.aliases:
                        char = "\u200b"
                    else:
                        char = " "
                    help_msg = cmd.help or "No help provided for this command"
                    i.append(f"`{cmd.name}{char}{', '.join(cmd.aliases)} {cmd.signature}` {help_msg}")
                await ctx.send(embed=discord.Embed(title=f"{command}", colour=self.bot.color,
                                                   description=" " + cog_doc + "\n\n" + "\n".join(i)))
            elif command and cmd:
                help_msg = cmd.help or "No help provided for this command"
                parent = cmd.full_parent_name
                if len(cmd.aliases) > 0:
                    aliases = ', '.join(cmd.aliases)
                    cmd_alias_format = f'{cmd.name} [{aliases}]'
                    if parent:
                        cmd_alias_format = f'{parent} {cmd_alias_format}'
                    alias = cmd_alias_format
                else:
                    alias = cmd.name if not parent else f'{parent} {cmd.name}'
                embed = discord.Embed(title=f"{alias} {cmd.signature}", description=help_msg, colour=self.bot.color)
                if isinstance(cmd, commands.Group):
                    sub_cmds = []
                    for sub_cmd in cmd.commands:
                        schm = sub_cmd.help or "No help provided for this command"
                        if not sub_cmd.aliases:
                            char = "\u200b"
                        else:
                            char = ", "
                        sub_cmds.append(
                            f"`{cmd.name} {sub_cmd.name}{char}{', '.join(sub_cmd.aliases)} {sub_cmd.signature}` {schm}")
                    scs = "\n".join(sub_cmds)
                    await ctx.send(
                        embed=discord.Embed(title=f"{alias} {cmd.signature}", description=help_msg + "\n\n" + scs,
                                            colour=self.bot.color))
                else:
                    await ctx.send(embed=embed)
            else:
                await ctx.send(f"No command or category named `{command}` found")
        except Exception as e:
            return await ctx.send(e)






def setup(bot):
    bot.add_cog(Meta(bot))
