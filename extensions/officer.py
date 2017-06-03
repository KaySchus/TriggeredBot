import discord
from discord.ext import commands
import random

recruitment = '''[WoW Forum Post](https://goo.gl/3HQTJb)
[Recruitment Sheet](https://goo.gl/qTj9Ze)
[Recruitment Template](https://goo.gl/ckT8AO)
[Recruitment App](https://goo.gl/uuyuEM)\n'''

tools = '''[Roster](https://goo.gl/lwQn9P)
[AP Tracker](https://goo.gl/O4OSVB)\n\n'''

class Officer:
	"""Utilities that provide pseudo-RNG."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def officer(self, ctx):
		if ctx.invoked_subcommand is None:
			await self.bot.say('Incorrect officer subcommand passed.')

	@officer.command(pass_context = True, no_pm = True)
	async def links(self, ctx):
		"""
			Displays our current repository of officer links
        """
		member = ctx.message.author
		server = ctx.message.server

		e = discord.Embed()

		e.title = 'Officer Links for ' + server.name + '\n\n'
		if server.icon:
			e.set_thumbnail(url=server.icon_url)

		if server.splash:
			e.set_image(url=server.splash_url)

		e.add_field(name='Recruitment', value=recruitment)
		e.add_field(name='Tools', value=tools)
		e.colour = member.colour

		await self.bot.say(embed=e)

# Required for proper setup - in all command extensions
def setup(bot):
	bot.add_cog(Officer(bot))