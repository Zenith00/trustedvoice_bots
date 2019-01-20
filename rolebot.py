import discord
import logging
from lux.contexter import Contexter
import lux
CONFIG = lux.config.Config(botname="ROLEBOT").load()

logging.basicConfig(level=CONFIG["LOGGING_LEVEL"])

def auth_func(ctx):
    return True


client = lux.client.Lux(CONFIG, auth_function=auth_func)
CONFIG = lux.config.Config(botname="PINBOT").load()

# Offering
@client.command(ack=CONFIG["ACK_TYPE"])
async def offering(ctx: Contexter):
    await ctx.m.author.add_roles(ctx.find_role("offering"))

@client.command(ack=CONFIG["ACK_TYPE"])
async def offeringt(ctx: Contexter):
    if ctx.find_role("offering") in ctx.m.author.roles:
        await ctx.m.author.remove_roles(ctx.find_role("offering"))
    else:
        await ctx.m.author.add_roles(ctx.find_role("offering"))

@client.command(name="-offering", ack=CONFIG["ACK_TYPE"])
async def deoffering(ctx):
    await ctx.m.author.remove_roles(ctx.find_role("offering"))

# Seeking
@client.command(ack=CONFIG["ACK_TYPE"])
async def looking(ctx: Contexter):
    await ctx.m.author.add_roles(ctx.find_role("looking"))

@client.command(ack=CONFIG["ACK_TYPE"])
async def lookingt(ctx: Contexter):
    if ctx.find_role("looking") in ctx.m.author.roles:
        await ctx.m.author.remove_roles(ctx.find_role("looking"))
    else:
        await ctx.m.author.add_roles(ctx.find_role("looking"))

@client.command(name="-looking", ack=CONFIG["ACK_TYPE"])
async def delooking(ctx):
    await ctx.m.author.remove_roles(ctx.find_role("looking"))

@client.event
async def on_member_join(member : discord.Member):
    await member.add_roles(member.guild.get_role(CONFIG["ROLE_TO_ID"]["Member"]))


client.run(CONFIG["BOT_TOKEN"], bot=True)
