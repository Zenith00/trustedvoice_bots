import collections
import logging
from io import BytesIO

import discord
import requests

import lux

try:
    from CONFIG import IMGBOT as CONFIG
except ImportError:
    raise ImportError("Copy CONFIG_DEFAULT.py to CONFIG.py, editing CONFIG.py for any configuration changes")


logging.basicConfig(level=CONFIG["LOGGING_LEVEL"])

client = lux.client.Lux(CONFIG)

STATES = {"init": False}

trackers = collections.defaultdict(dict)

@client.event
async def on_message(message_in):
    if message_in.author == client.user:
        return
    if message_in.channel.id not in CONFIG["CHANNEL_BLACKLIST_IDS"] and message_in.attachments:
        await copy_attachments(message_in)
    return

@client.event
async def on_reaction_add(reaction : discord.Reaction, user : discord.User):
    if reaction.message.channel.id == CONFIG["IMAGE_TARGET_CHANNEL"]:
        if reaction.count > 1 and reaction.emoji == "❌":
            await reaction.message.delete()
    pass


async def copy_attachments(message: discord.Message):
    if not CONFIG["PRESERVE_IMAGES"]:
        return
    files = []
    for counter, attachment in enumerate(message.attachments):
        print(attachment)
        print(dir(attachment))
        if attachment.url:
            embed = discord.Embed()
            embed.set_image(url=f"attachment://image{counter}.png")
            response = requests.get(attachment.url)
            files.append(discord.File(BytesIO(response.content), filename="image.png"))

    message = await client.get_channel(534925638767738890).send(
        f"Copying images from `UID: [{message.author.id}]` {message.author.mention} in `CID: [{message.channel.id}]` `({message.channel.name})` <#{message.channel.id}>, sourced from message `MID: [{message.id}]` {message.jump_url}",
        files=files)
    await message.add_reaction("❌")


client.run(CONFIG["BOT_TOKEN"], bot=True)
