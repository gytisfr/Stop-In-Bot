#Stop-In Utilities by ~ Gytis5089

import discord
import asyncio
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name=f"Prefix -"))
	print('Stop-In Utilities is online.')
	print(f'Current ping is {round(client.latency * 100)}ms')

@client.event
async def on_member_join(member):
	welcome = discord.utils.get(member.guild.channels, name="welcome")
	await welcome.send(f"Welcome {member.mention} to Stop-In!")

def is_owner(ctx):
	return ctx.author.id in [301014178703998987, 723532900020256789]

def is_gytis(ctx):
	return ctx.author.id in [301014178703998987]

def is_fin(ctx):
	return ctx.author.id in [723532900020256789]

@client.command(aliases=['purge', 'clear'])
@commands.has_permissions(manage_messages=True)
async def wipe(ctx, amount=1):
	await ctx.channel.purge(limit=amount)
	embed = discord.Embed(
		title = 'Wipe',
		colour = 0xFFAA00,
		description = f'{ctx.author.mention} has wiped {amount} messages in <#{ctx.channel.id}>',
	)
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	embed = discord.Embed(
		title = 'Wipe',
		colour = 0xFFAA00,
		description = f'{ctx.author.mention} has wiped {amount} messages.',
	)
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	message = await ctx.send(embed=embed)
	await asyncio.sleep(1)
	await message.delete()

@wipe.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member : discord.Member = None, *, arg):
	embed = discord.Embed(
		title = 'Warn',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has warned <@{member.id}> for:\n{arg}',
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	embed = discord.Embed(
		title = 'Warn',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has warned you for:\n{arg}',
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)

@warn.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member = None, *, arg):
	embed = discord.Embed(
		title = 'Mute',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has muted <@{member.id}> for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	role = discord.utils.get(member.guild.roles, name='muted')
	await member.add_roles(role)
	embed = discord.Embed(
		title = 'Mute',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has muted you for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)

@mute.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member = None):
	embed = discord.Embed(
		title = 'Unmute',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has unmuted <@{member.id}>'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	role = discord.utils.get(member.guild.roles, name='muted')
	await member.remove_roles(role)
	embed = discord.Embed(
		title = 'Unmute',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has unmuted you'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)

@unmute.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(administrator=True)
async def suspend(ctx, member : discord.Member = None, *, arg):
	embed = discord.Embed(
		title = 'Suspend',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has suspended <@{member.id}> for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	role = discord.utils.get(member.guild.roles, name='suspended')
	await member.add_roles(role)
	embed = discord.Embed(
		title = 'Suspend',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has suspended you for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)

@suspend.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(administrator=True)
async def unsuspend(ctx, member : discord.Member = None):
	embed = discord.Embed(
		title = 'Unsuspend',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has unsuspended <@{member.id}>'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	role = discord.utils.get(member.guild.roles, name='suspended')
	await member.remove_roles(role)
	embed = discord.Embed(
		title = 'Unsuspend',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has unsuspended you'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)

@unsuspend.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, arg):
	embed = discord.Embed(
		title = 'Kick',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has kicked <@{member.id}> for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	embed = discord.Embed(
		title = 'Kick',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has kicked you for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)
	await member.kick(reason=arg)

@kick.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, arg):
	embed = discord.Embed(
		title = 'Ban',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has banned <@{member.id}> for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	embed = discord.Embed(
		title = 'Ban',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has banned you for:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)
	await member.ban(reason=arg)

@ban.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
	embed = discord.Embed(
		title = 'Unban',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has unbanned <@{member.id}>'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	channel = discord.utils.get(ctx.guild.text_channels, name='logs')
	await channel.send(embed=embed)
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			embed = discord.Embed(
				title = 'Unban',
        		colour = 0xFFAA00,
        		description = f'{ctx.author.mention} has unbanned you'
    		)
			embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
			await user.send(embed=embed)

@client.command(aliases=['promo'])
@commands.check(is_owner)
async def promote(ctx, member : discord.Member = None):
	channel = discord.utils.get(ctx.guild.text_channels, name='promos-mtp')
	role1 = discord.utils.get(member.guild.roles, name='Trial Moderator')
	role2 = discord.utils.get(member.guild.roles, name='Moderator')
	role3 = discord.utils.get(member.guild.roles, name='Senior Moderator')
	role4 = discord.utils.get(member.guild.roles, name='Head Moderator')
	role5 = discord.utils.get(member.guild.roles, name='Trial Administrator')
	role6 = discord.utils.get(member.guild.roles, name='Administrator')
	role7 = discord.utils.get(member.guild.roles, name='Senior Administrator')
	role8 = discord.utils.get(member.guild.roles, name='Head Administrator')
	role9 = discord.utils.get(member.guild.roles, name='Manager')
	if (752825116907274250 in member._roles):
		await member.remove_roles(role1)
		await member.add_roles(role2)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Trial Moderator to Moderator")

	elif (752825242577272954 in member._roles):
		await member.remove_roles(role2)
		await member.add_roles(role3)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Moderator to Senior Moderator")

	elif (752825265087971389 in member._roles):
		await member.remove_roles(role3)
		await member.add_roles(role4)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Senior Moderator to Head Moderator")

	elif (752825294372470794 in member._roles):
		await member.remove_roles(role4)
		await member.add_roles(role5)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Head Moderator to Trial Administrator")

	elif (752825173325119519 in member._roles):
		await member.remove_roles(role5)
		await member.add_roles(role6)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Trial Administrator to Administrator")

	elif (752825350031015936 in member._roles):
		await member.remove_roles(role6)
		await member.add_roles(role7)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Administrator to Senior Administrator")

	elif (752825378535505950 in member._roles):
		await member.remove_roles(role7)
		await member.add_roles(role8)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Senior Administrator to Head Administrator")

	elif (752825422185627670 in member._roles):
		await member.remove_roles(role8)
		await member.add_roles(role9)
		await channel.send(f"{ctx.author.mention} has promoted <@{member.id}> from Head Administrator to Manager")

	else:
		await ctx.send('Uh-oh, looks like that user is already the manager!')

@client.command(aliases=['mtp', 'pass', 'Pass'])
@commands.check(is_owner)
async def MTP(ctx, member : discord.Member = None):
	channel = discord.utils.get(ctx.guild.text_channels, name='promos-mtp')
	role = discord.utils.get(member.guild.roles, name='Paused Mod')
	await member.remove_roles(role)
	embed = discord.Embed(
				title = 'MTP Pass',
        		colour = 0xFFAA00,
        		description = f"<@{member.id}> has passed the MTP.\nConfirmed by {ctx.author.mention}"
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await channel.send(embed=embed)

@unban.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, arg):
	channel = discord.utils.get(ctx.guild.text_channels, name='announcements')
	await channel.send(f'@everyone\n\n**----------**\n\n{arg}\n\n**----------**\n\nAnnouncement by: {ctx.author.mention}')

@announce.error
async def clean_error(ctx, error):
	if ininstance(error, commands.CheckFailure):
		await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.check(is_gytis)
async def gannounce(ctx, *, arg):
	channel = discord.utils.get(ctx.guild.text_channels, name='gytis-announcements')
	await channel.send(f'<@&756880820228194375>\n\n**----------**\n\n{arg}')

@gannounce.error
async def clean_error(ctx, error):
	if ininstance(error, commands.CheckFailure):
		await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.check(is_fin)
async def fannounce(ctx, *, arg):
	channel = discord.utils.get(ctx.guild.text_channels, name='fin-announcements')
	await channel.send(f'<@&756880861898735816>\n\n**----------**\n\n{arg}')

@fannounce.error
async def clean_error(ctx, error):
	if ininstance(error, commands.CheckFailure):
		await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.check(is_owner)
async def mannounce(ctx, *, arg):
	channel = discord.utils.get(ctx.guild.text_channels, name='mod-announcements')
	await channel.send(f'@everyone\n\n**----------**\n\n{arg}\n\n**----------**\n\nAnnouncement by: {ctx.author.mention}')

@mannounce.error
async def clean_error(ctx, error):
	if ininstance(error, commands.CheckFailure):
		await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command()
@commands.check(is_gytis)
async def uannounce(ctx, *, arg):
	channel = discord.utils.get(ctx.guild.text_channels, name='utilities-announcements')
	await channel.send(f'@everyone\n\n**----------**\n\n{arg}')

@uannounce.error
async def clean_error(ctx, error):
	if ininstance(error, commands.CheckFailure):
		await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['DM', 'dm', 'PM', 'pm', 'MSG', 'msg'])
@commands.has_permissions(administrator=True)
async def message(ctx, member : discord.Member = None, *, arg):
	embed = discord.Embed(
		title = 'Message',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has messaged <@{member.id}>:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)
	embed = discord.Embed(
		title = 'Message',
        colour = 0xFFAA00,
        description = f'Message from {ctx.author.mention}:\n{arg}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)

@message.error
async def clean_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You are unable to do this.\nCheck your permissions and try again.")

@client.command(aliases=['join', 'joined', 'created'])
async def create(ctx, member : discord.Member = None):
	embed = discord.Embed(
		title = 'Create',
        colour = 0xFFAA00,
        description = f'{member.name} created their account on {str(member.created_at)[0:10]}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def accept(ctx, member : discord.Member = None):
	role1 = discord.utils.get(member.guild.roles, name='HELP')
	role2 = discord.utils.get(member.guild.roles, name='Paused Mod')
	role3 = discord.utils.get(member.guild.roles, name='Trial Moderator')
	channel = client.get_channel(753287403422089229)
	await member.send(f'{member.mention}, you have been accepted into the Stop-In staff team.\nCongratulations!\nBy {ctx.author.mention}')
	embed = discord.Embed(
		title = 'Acceptance',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has accepted {member.mention}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await channel.send(embed=embed)
	await member.add_roles(role1)
	await member.add_roles(role2)
	await member.add_roles(role3)

@client.command()
@commands.has_permissions(administrator=True)
async def deny(ctx, member : discord.Member = None):
	channel = client.get_channel(753287403422089229)
	embed = discord.Embed(
		title = 'Denial',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has denied you into joining the Stop-In staff team.'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await member.send(embed=embed)
	embed = discord.Embed(
		title = 'Denial',
        colour = 0xFFAA00,
        description = f'{ctx.author.mention} has denied {member.mention}'
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await channel.send(embed=embed)

@client.command(aliases=['member', 'Members', 'Member'])
async def members(ctx):
	await ctx.send(f"Stop-In is currently at {ctx.author.guild.member_count} members!\n8 of those members are bots!")

@client.command(aliases=['Booster', 'booster', 'Boosts', 'boosts', 'Boost', 'boost'])
async def boosters(ctx):
	embed = discord.Embed(
	   title = 'Boosters',
	   colour = 0xFF7DE6,
	   description = f'`Server Level:`{ctx.guild.premium_tier}\n`Total Boosts:`{ctx.guild.premium_subscription_count}'
	)
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")

	premium_subscribers = ctx.guild.premium_subscribers
	
	for guild in premium_subscribers:
		embed.add_field(name=guild.name, value=f'`Boosting Since:`{guild.premium_since}')
	
	await ctx.send(embed=embed)

@client.command()
async def schedule(ctx):
	embed = discord.Embed(
		title = 'Bus Schedule',
		colour = 0xFFAA00,
		description = '**Monday:**N/A, Dog getting groomed.\n**Tuesday:**N/A, Daughter has swimming.\n**Wednesday:**N/A, Movie night.\n**Thursday:**N/A, Son has football practise.\n**Friday:**N/A, Fish and Chips.\n**Saturday:**N/A, Day off.\n**Sunday:**N/A, Day for Jesus.'
	)
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)

@client.command(aliases=["AmongUs", "au", "AU", "Au", "aU", "amongUs", "Amongus"])
async def amongus(ctx):
	quote = ["purple", "pink", "green", "lime", "blue", "cyan", "black", "white", "yellow", "red", "orange", "brown"]
	await ctx.send("I dunno man, " + random.choice(quote) + " seems kinda sus not gonna lie.")

@client.command()
async def love(ctx):
	await ctx.send('Love you too :heart:')

@client.command()
async def kevingames(ctx):
	await ctx.send('Oh Kevin he’s aight but, HE ATE MY COOKIES!!')

@client.command()
async def bus(ctx):
	await ctx.send('Beep beep')

@client.command()
async def car(ctx):
	await ctx.send('Nyoummmm')

@client.command(aliases=['h', 'H'])
async def help(ctx):
	embed = discord.Embed(
		title = 'Help Module',
        colour = 0xFFAA00,
        description = "`-schedule` - Check the bus schedule!\n`-amongus` - Who is sus?\n`-love` - Proclaim your love to <@752987874839887964>\n`-bus` - What's that passing by?\n`-car` - Something else?\n`-kevingames` - Who's Kevin?\n`-boost` - Who is currently boosting?\n`-members` - How many people are in Stop-In?\n`-create` - When did you join discord?\n\n`-clear` - This command removes your set amount of messages. (Make sure to add 1 to the amount you want to remove.)\n`-warn` - This command is used to warn members.\n`-mute` - This command is used to mute members.\n`-unmute` - This command is used to unmute members.\n`-suspend` - This command is used to suspend people. This is mainly used for people with inappropriate usernames or profile pictures.\n`-unsuspend` - This command is used to unsuspend people.\n`-kick` - This command is used to kick members.\n`-ban` - This command is used to ban members.\n`-unban` - This command is used to unban members.\n`-message` - This command is used to message members.\n`-accept` - This command is used to accept users into the staff team.\n`-deny` - This command is used to deny users from the staff team.\n`-promote` - This command is used to promote staff members.\n`-announce` - This command is used to make an announcement into the <#752824927945490493> channel. (-gannounce, -fannounce  & -mannounce counterparts for <#755149071601369109>, <#755149100491603988> & <#752929130646863952> which are exclusive to Gytis, Fin & Admins.)"
    )
	embed.set_thumbnail(url="https://lh5.googleusercontent.com/1ZaPqoiPYB97JFWDfmtUBTPmbOeSm7hp4rUYqCNC3oGd0gWaFhsFWjU2oSR9GlqHNBd7B-IfbuOa4bpRvTW5=w1920-h947")
	await ctx.send(embed=embed)

client.run('NzUyOTg3ODc0ODM5ODg3OTY0.X1fomw.RqaAMBhH7sMcnYeyjaFEdaIysxo')