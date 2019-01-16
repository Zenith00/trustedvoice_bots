try:
    import CONFIG
except ImportError:
    raise ImportError("Copy CONFIG_DEFAULT.py to CONFIG.py, editing CONFIG.py for any configuration changes")


import logging
from lux.contexter import Contexter
from lux.client import Lux
logging.basicConfig(level=CONFIG.LOGGING_LEVEL)

CONFIG.ID_TO_ROLE = dict([(v, k) for k, v in CONFIG.ROLE_TO_ID.items()])
CONFIG.ciID_TO_ROLE = dict([(v, k.lower()) for k, v in CONFIG.ROLE_TO_ID.items()])
CONFIG.ciROLE_TO_ID = dict([(k.lower(), v) for k, v in CONFIG.ROLE_TO_ID.items()])

client = Lux(CONFIG)

# Offering
@client.command(ack=CONFIG.ACK_TYPE)
async def offering(ctx: Contexter):
    await ctx.m.author.add_roles(ctx.find_role("offering"))

@client.command(ack=CONFIG.ACK_TYPE)
async def offeringt(ctx: Contexter):
    if ctx.find_role("offering") in ctx.m.author.roles:
        await ctx.m.author.remove_roles(ctx.find_role("offering"))
    else:
        await ctx.m.author.add_roles(ctx.find_role("offering"))

@client.command(name="-offering", ack=CONFIG.ACK_TYPE)
async def deoffering(ctx):
    await ctx.m.author.remove_roles(ctx.find_role("offering"))

# Seeking
@client.command(ack=CONFIG.ACK_TYPE)
async def looking(ctx: Contexter):
    await ctx.m.author.add_roles(ctx.find_role("looking"))

@client.command(ack=CONFIG.ACK_TYPE)
async def lookingt(ctx: Contexter):
    if ctx.find_role("looking") in ctx.m.author.roles:
        await ctx.m.author.remove_roles(ctx.find_role("looking"))
    else:
        await ctx.m.author.add_roles(ctx.find_role("looking"))

@client.command(name="-looking", ack=CONFIG.ACK_TYPE)
async def delooking(ctx):
    await ctx.m.author.remove_roles(ctx.find_role("looking"))



client.run(CONFIG.BOT_TOKEN, bot=True)
