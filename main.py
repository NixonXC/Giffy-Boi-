import discord
from discord.ext import commands

client = commands.Bot(command_prefix= '!')

@client.event
async def on_start():
 print('baba boi is now online')

@client.command()
async def gif(ctx):
  await ctx.send("https://media.tenor.com/images/efa12e37ff758c727a9b557495bd3313/tenor.gif")

@client.command()
async def gif1(ctx):
  await ctx.send("https://media.tenor.com/images/6afb17492c5b0a711b51afe70e24d3c4/tenor.gif")

@client.command()
async def gif2(ctx):
  await ctx.send("https://media.tenor.com/images/12e67d227f915a3b8cb24a20d9f38a27/tenor.gif")

@client.command()
async def gif3(ctx):
  await ctx.send("https://media.tenor.com/images/6f78f6a19dc71238659e04d13cbca6b5/tenor.gif")

@client.command()
async def gif4(ctx):
  await ctx.send("https://media.tenor.com/images/79bc59044d2817f49087a5a3e04296d0/tenor.gif")

@client.command()
async def gif5(ctx):
  await ctx.send("https://media.tenor.com/images/8bd3c6af7b717d35a63147dc94c338c3/tenor.gif")

@client.command()
async def gif6(ctx):
  await ctx.send("https://c.tenor.com/oQ_6wxtMrx0AAAAj/pentol-quby.gif")

@client.command()
async def gif7(ctx):
  await ctx.send("https://media.tenor.com/images/f4c8059e75d21aa301174d4374ec4680/tenor.gif")

@client.command()
async def gif8(ctx):
  await ctx.send("https://media.tenor.com/images/90cbdd6b4f1da94c265b8cb77c52f4ba/tenor.gif")

@client.command()
async def gif9(ctx):
  await ctx.send("https://media.tenor.com/images/632e93d49ebd4175de0289e69d7a24f1/tenor.gif")

@client.command()
async def gif10(ctx):
  await ctx.send("https://c.tenor.com/jDn9i5hbQMQAAAAj/555.gif")

@client.command()
async def gif11(ctx):
  await ctx.send("https://c.tenor.com/t1TgAIrGFUAAAAAj/party-time.gif")

@client.command()
async def gif12(ctx):
  await ctx.send("https://cdn.discordapp.com/emojis/828497049259474964.gif?v=1&size=40")

@client.command()
async def gif13(ctx):
  await ctx.send("https://media.tenor.com/images/27a8f06977d97d7ee6a1ac3db3a8a0ea/tenor.gif")

@client.command()
async def gif14(ctx):
  await ctx.send("https://cdn.discordapp.com/emojis/823549798530416730.gif?v=1&size=40")

@client.command()
async def gif15(ctx):
  await ctx.send("https://c.tenor.com/Gs9Ss-nBrTYAAAAj/esselcius-bonalkset.gif")

@client.command()
async def gif16(ctx):
  await ctx.send("https://media.tenor.com/images/8e39158aa2c6f0976541199bfa188f96/tenor.gif")

@client.command()
async def gif17(ctx):
  await ctx.send("https://media.tenor.com/images/4a2cde0d91f491056ae3c26cbd8788e8/tenor.gif")

@client.command()
async def gif18(ctx):
  await ctx.send("https://c.tenor.com/4ILwPySkXq4AAAAj/twitch-logo.gif")

@client.command()
async def gif19(ctx):
  await ctx.send("https://media.tenor.com/images/d20ed50f6d3ae67517b7d9674269eaa5/tenor.gif")

@client.command()
async def gif20(ctx):
  await ctx.send("https://media.tenor.com/images/028d5d4019f46a46f03f5bac3902bf40/tenor.gif")

@client.command()
async def gif21(ctx):
  await ctx.send("https://c.tenor.com/2iym0mC-mzoAAAAj/fortnite-dance.gif")

client.run('Your Bot Token')
