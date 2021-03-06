import pprint

CONFIG_DEFAULT = {
    "ROLE_TO_ID"             :
        {"SR_Shrubbery_Hiraeth"    : 533038573792919553, "SR_Shrubbery_Grey": 533028882035769374,
         "SRSuzuya𝖚𝖓𝖙𝖎𝖙𝖑𝖊𝖉": 532990712325865492, "SR_ChouTofu_DERANGEDcitiZen": 532980885297823785, "Member": 426861484983975937,
         "Muted"                   : 426487777669152770, "Offering": 427624125679403008, "Looking": 427624132134567937,
         "TrustedVoices"           : 426487730382569483, "Chat-Moderator-": 446642041191923712, "Chat-Moderator": 426487602691047460,
         "KindVoice-Moderator"     : 426487509183234060, "Bots": 441181488789323777},
    "CHANNEL_TO_ID"          : {
        "bot-commands"          : 441360491390959626, "public-rant": 441804219037646850, "rules": 441659037390471188, "sr_ratedrex_vex": 534923596808716289,
        "bot-debug-output"      : 440709967524134913, "trustedvoicebot-bug-report": 441277803984322560, "subreddit-feed": 439123029558296576,
        "subreddit-suggestions" : 441782350855143445, "Moderator Stuff": 426496179862241301, "public-support-1": 441804136556527636,
        "bot-suggestions"       : 441782501661343744, "Other": 426497958977077252, "posting-guidelines": 464432402698207233,
        "technical-help"        : 426497773605617665, "discord-suggestions": 441782449043668994, "faq": 441420715049091075,
        "moderator-bot-controls": 440760004484661252, "mod-offtopic-chat": 439184293214945300, "Off-Topic": 426496239987851267,
        "media-sharing"         : 488068343572594689, "announcements": 426486432421642240, "relationship-support": 464104614715719691,
        "public-support-2"      : 441804181691564043, "feel-good-posting": 464456067573874689, "Technical Support": 426496314445135873,
        "message-the-moderators": 426489669685870592, "general": 441801826858303499, "Support Rooms": 426497538544107540,
        "post-support-requests" : 441360517559484416, "Welcome": 426484172404555798, "reported-chats": 441360848729014281,
        "roombot-bug-report"    : 440554180457922610, "public-support-3": 488560643755212802, "mod-chat": 426489987387621396
    },
    "CHANNEL_BLACKLIST_NAMES": [
        "bot-commands",
        "public-rant",
        "rules",
        "sr_ratedrex_vex",
        "bot-debug-output",
        "trustedvoicebot-bug-report",
        "subreddit-feed",
        "subreddit-suggestions",
        "Moderator Stuff",
        "public-support-1",
        "bot-suggestions",
        "Other",
        "posting-guidelines",
        "technical-help",
        "discord-suggestions",
        "faq",
        "moderator-bot-controls",
        "mod-offtopic-chat",
        "Off-Topic",
        "announcements",
        "relationship-support",
        "public-support-2",
        "Technical Support",
        "message-the-moderators",
        "general",
        "Support Rooms",
        "post-support-requests",
        "Welcome",
        "reported-chats",
        "roombot-bug-report",
        "public-support-3",
        "mod-chat",
    ],
}

CONFIG_DEFAULT["CHANNEL_BLACKLIST_IDS"] = [
    CONFIG_DEFAULT["CHANNEL_TO_ID"][name] for name in CONFIG_DEFAULT["CHANNEL_BLACKLIST_NAMES"]
]

CONFIG_DEFAULT["ID_TO_ROLE"] = {v:k for k,v in CONFIG_DEFAULT["ROLE_TO_ID"].items()}

CONFIG_DEFAULT["ROLE_BY_CONFIG"] = True
CONFIG_DEFAULT["LOGGING_LEVEL"] = "INFO"
CONFIG_DEFAULT["GUILD_ID"] = 534907871339741194
CONFIG_DEFAULT["ACK_TYPE"] = "react"
CONFIG_DEFAULT["PREFIX"] = "!"


# ===================================================================================
# ===============================End of config section===============================
# ===================================================================================



import discord
import logging
from lux.contexter import Contexter
import lux
CONFIG = lux.config.Config(botname="ROLEBOT", config_defaults=CONFIG_DEFAULT).load()

logging.basicConfig(level=logging.INFO)

def auth_func(ctx):
    return True


client = lux.client.Lux(CONFIG, auth_function=auth_func, disable_builtins=True)
# CONFIG = lux.config.Config(botname="ROLEBOT").load()

async def add_checkmark(ctx):
    await ctx.m.add_reaction("✅")

print("Registering custom commands...")
# Offering
@client.command(posts=[(add_checkmark, "async","ctx")])
async def offering(ctx: Contexter):
    await ctx.m.author.add_roles(ctx.find_role("offering"))

@client.command(posts=[(add_checkmark, "async","ctx")])
async def offeringt(ctx: Contexter):
    if ctx.find_role("offering") in ctx.m.author.roles:
        await ctx.m.author.remove_roles(ctx.find_role("offering"))
    else:
        await ctx.m.author.add_roles(ctx.find_role("offering"))

@client.command(name="-offering",posts=[(add_checkmark, "async","ctx")])
async def deoffering(ctx):
    await ctx.m.author.remove_roles(ctx.find_role("offering"))

# Seeking
@client.command(posts=[(add_checkmark, "async","ctx")])
async def looking(ctx: Contexter):
    await ctx.m.author.add_roles(ctx.find_role("looking"))

@client.command(posts=[(add_checkmark, "async","ctx")])
async def lookingt(ctx: Contexter):
    if ctx.find_role("looking") in ctx.m.author.roles:
        await ctx.m.author.remove_roles(ctx.find_role("looking"))
    else:
        await ctx.m.author.add_roles(ctx.find_role("looking"))

@client.command(name="-looking",posts=[(add_checkmark, "async","ctx")])
async def delooking(ctx):
    await ctx.m.author.remove_roles(ctx.find_role("looking"))

@client.event
async def on_member_join(member : discord.Member):
    await member.add_roles(Contexter(configs=CONFIG, guild=member.guild).find_role("member"))


client.run(CONFIG.TOKEN, bot=True)
