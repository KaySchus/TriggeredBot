from discord.ext import commands

role_whitelist = {
    'tank',
    'healer',
    'dps',
    'ranged dps',
    'melee dps',
    'death knight',
    'demon hunter',
    'druid',
    'hunter',
    'mage',
    'monk',
    'paladin',
    'priest',
    'rogue',
    'shaman',
    'warlock',
    'warrior',
}

class Role:
	"""Utilities that provide discord role functionality."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def role(self, ctx):
		if ctx.invoked_subcommand is None:
			await self.bot.say('Incorrect role subcommand passed.')

	#Allows the user to assign themselves a role from an assigned set.
	@role.command(pass_context=True)
	async def add(self, ctx):
		message = ctx.message.content.replace('!role add', '')
		roles = [x.strip().lower() for x in message.split(',')]
		roles_added = []

		for role in ctx.message.server.roles:
			if role.name.lower() in roles and role.name.lower() in role_whitelist:
				try:
					await self.bot.add_roles(ctx.message.author, role)
					roles_added.append(role.name)
				except Forbidden:
					print("Forbidden")
				except HTTPException:
					print("HTTPException")

		await self.bot.say("Added Role(s): " + ', '.join(map(str, roles_added)))

	#Allows the user to remove themselves from a role from an assigned set.
	@role.command(pass_context=True)
	async def remove(self, ctx):
		message = ctx.message.content.replace('!role remove', '')
		roles = [x.strip().lower() for x in message.split(',')]
		roles_removed = []

		for role in ctx.message.server.roles:
			if role.name.lower() in roles and role.name.lower() in role_whitelist:
				try:
					await self.bot.remove_roles(ctx.message.author, role)
					roles_removed.append(role.name)
				except Forbidden:
					print("Forbidden")
				except HTTPException:
					print("HTTPException")

		await self.bot.say("Removed Role(s): " + ', '.join(map(str, roles_removed)))

	#Allows the user to list their currently assigned roles.
	@role.command(pass_context=True)
	async def list(self, ctx):
		role_list = []

		for role in ctx.message.author.roles:
			if role.name.lower() in role_whitelist:
				role_list.append(role.name)

		await self.bot.say("Current Role(s): " + ', '.join(map(str, role_list)))

# Required for proper setup - in all command extensions
def setup(bot):
	bot.add_cog(Role(bot))