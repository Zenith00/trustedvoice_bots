import discord

client = discord.Client()


@client.event
async def on_member_join(member : discord.Member):
    await member.add_roles(member.guild.get_role(426861484983975937))


TOKEN = 0

client.run(TOKEN, bot=True)