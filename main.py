import os
import datetime
import asyncio
import configparser

import discord
from discord.ext import commands

initial_extensions = [
    'extensions.rng',
    'extensions.role',
    'extensions.util',
    'extensions.officer'
]

description = "Triggered Guild Discord Bot"
prefix = ['?', '!', '\N{HEAVY EXCLAMATION MARK SYMBOL}']

bot = commands.Bot(command_prefix = prefix, description = description)

@bot.event
async def on_ready():
	print('Logged in as')
	print('Username: ' + bot.user.name)
	print('ID: ' + bot.user.id)
	print('------')

	if not hasattr(bot, 'uptime'):
		bot.uptime = datetime.datetime.utcnow()

@bot.event
async def on_message(message):
	if message.author.bot:
		return

	await bot.process_commands(message)

def load_config(filename):
	basedir = os.path.abspath(os.path.dirname(__file__))
	config = configparser.ConfigParser()
	config.read(os.path.join(basedir, filename))

	return config

if __name__ == '__main__':
	config = load_config('config.ini')

	for extension in initial_extensions:
		try:
			bot.load_extension(extension)
		except Exception as e:
			print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

	bot.run(config['Security']['Key'])
