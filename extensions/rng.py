from discord.ext import commands
import random

class RNG:
	"""Utilities that provide pseudo-RNG."""

	def __init__(self, bot):
		self.bot = bot

	@commands.group(pass_context=True)
	async def random(self, ctx):
		if ctx.invoked_subcommand is None:
			await self.bot.say('Incorrect random subcommand passed.')

	@random.command()
	async def number(self, minimum = 0, maximum = 100):
		""" Displays a random number within an optional range.

	        The minimum must be smaller than the maximum.
        """

		if minimum >= maximum:
			await self.bot.say('Maximum is smaller than or equal to minimum.')
			return

		await self.bot.say(random.randint(minimum, maximum))

# Required for proper setup - in all command extensions
def setup(bot):
	bot.add_cog(RNG(bot))