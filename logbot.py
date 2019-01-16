import logging
import discord
import lux
from PIL import Image
import requests
from io import BytesIO

import collections

import CONFIG

logging.basicConfig(level=logging.INFO)

client = lux.client.Lux(CONFIG)

STATES = {"init": False}

trackers = collections.defaultdict(dict)

@client.event
async def on_message(message_in):
    if message_in.author == client.user:
        return
    print("Message hooked")
    if message_in.attachments:
        print("Message has attachments")
        await copy_attachments(message_in)
    return

@client.even
async def on_reaction_add(reaction : discord.Reaction, user : discord.User):
    if reaction.message.channel == CONFIG.IMAGE_TARGET_CHANNEL:
        if reaction.count > 1 and reaction.emoji == "❌" :
            await reaction.message.delete()
    pass


async def copy_attachments(message: discord.Message):
    if not CONFIG.PRESERVE_IMAGES:
        return
    print("Embed found")
    files = []
    for counter, attachment in enumerate(message.attachments):
        print("Showing embed: " )
        print(attachment)
        print(dir(attachment))
        if attachment.url:
            embed = discord.Embed()
            embed.set_image(url=f"attachment://image{counter}.png")
            response = requests.get(attachment.url)
            img = Image.open(BytesIO(response.content))
            files.append(discord.File(BytesIO(response.content), filename="image.png"))

    message = await client.get_channel(534925638767738890).send(
        f"Copying images from `UID: [{message.author.id}]` {message.author.mention} in `CID: [{message.channel.id}]` `({message.channel.name})` <#{message.channel.id}>, sourced from message `MID: [{message.id}]` {message.jump_url}",
        files=files)
    await message.add_reaction("❌")


client.run(CONFIG.BOT_TOKEN, bot=True)
