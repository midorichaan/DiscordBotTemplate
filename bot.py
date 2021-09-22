import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("on_ready!")

@bot.event
async def on_command_error(ctx, exc):
    await ctx.send(f"```py\n{exc}\n```")

@bot.command(name="neko")
async def neko(ctx):
    await ctx.send("にゃーん")

@bot.command(name="embed")
async def embed(ctx):
    await ctx.send(embed=discord.Embed(title="にゃーん"))

bot.run("YoUrDiScOrDbOtToKeNhErE")
