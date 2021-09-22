import discord

bot = discord.Client()

@bot.event
async def on_ready():
    print("on_ready!")

@bot.event
async def on_message(message):
    if message.content == "にゃーん":
        if not message.author.bot:
            await message.channel.send("にゃーん")
  
    if message.content == "!neko":
        await message.channel.send("にゃーん")
        
    if message.content == "!embed":
        await message.channel.send(embed=discord.Embed(title="にゃーん", color=0x2ecc71))

bot.run("YoUrDiScOrDbOtToKeNhErE")
