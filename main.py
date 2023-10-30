import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ticket(ctx):
    category = await ctx.guild.create_category("Tickets")

    channel_name = f"ticket-{ctx.author.name}"
    channel = await ctx.guild.create_text_channel(channel_name, category=category)
    await channel.send(f"Ticket created by {ctx.author.mention}")

    await ctx.send(f"Ticket channel created: {channel.mention}")

@bot.command()
async def close(ctx):
    category = discord.utils.get(ctx.guild.categories, name="Tickets")
    if category:
        if isinstance(ctx.channel, discord.TextChannel) and ctx.channel.category == category:
            await ctx.channel.delete()
        else:
            await ctx.send("You can only use this command in a ticket channel.")
    else:
        await ctx.send("Ticket category not found.")

bot.run('YOUR_BOT_TOKEN')