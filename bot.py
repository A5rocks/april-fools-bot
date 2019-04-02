""" # Basically the code used :
# An April Fools bot

from discord.ext import commands


with open('key.txt') as f:
  token = f.read().strip()

bot = commands.Bot(command_prefix='!')

@bot.command('april-me')
async def surprised_pikachu(ctx):
  await ctx.message.channel.send('April me surprised') # xd I don't know
  async for member in ctx.message.guild.members:
    await member.edit(nick='Surprised Pikachu')

bot.run(token)

"""

(lambda asyncio, commands, token_file: (lambda bot, token, loop: (lambda _, surprised_pikachu_thing: (lambda surprised_pikachu: (lambda _: bot.run(token))(surprised_pikachu_thing(surprised_pikachu)))(asyncio.coroutine(lambda ctx: (lambda _: [loop.create_task(member.edit(nick='Surprised Pikachu')) for member in ctx.message.guild.members])(loop.create_task(ctx.message.channel.send('April me surprised'))))))(token_file.close(), bot.command('april-me')))(commands.Bot(command_prefix='!'), token_file.read().strip(), asyncio.get_event_loop()))(__import__('asyncio'), __import__('importlib').import_module('discord.ext.commands'), open('key.txt'))






