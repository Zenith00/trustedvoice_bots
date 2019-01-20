ROLEBOT = {
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

ROLEBOT["CHANNEL_BLACKLIST_IDS"] = [
    ROLEBOT["CHANNEL_TO_ID"][name] for name in ROLEBOT["CHANNEL_BLACKLIST_NAMES"]
]
ROLEBOT["ciID_TO_ROLE"] = {}
ROLEBOT["ciROLE_TO_ID"] = {}
ROLEBOT["ID_TO_ROLE"] = {}

ROLEBOT["ROLE_BY_CONFIG"] = True
ROLEBOT["LOGGING_LEVEL"] = "INFO"
ROLEBOT["GUILD_ID"] = 534907871339741194
ROLEBOT["ACK_TYPE"] = "react"
ROLEBOT["PREFIX"] = "!"


IMGBOT = {"PRESERVE_IMAGES": True,
          "IMAGE_TARGET_CHANNEL": 361662909220388876,
          "LOGGING_LEVEL" : "INFO"}
