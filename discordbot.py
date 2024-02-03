from asyncio import sleep
import discord
from discord.ext import commands
import random
import math
intents = discord.Intents.default()
intents.message_content = True
client = commands.AutoShardedBot(commands.when_mentioned_or('!'), intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

def add(x, y):
	return x + y

def sub(x, y):
	return x - y

def div(x, y):
	return x / y

def sqrt(x):
	return math.sqrt(x)

def mult(x, y):
	return x * y

@client.command()
async def mathadd(ctx, x, y):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsub(ctx, x, y):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathdiv(ctx, x, y):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathmult(ctx, x, y):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsqrt(ctx, x):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass

client.run(#fill in your own key)