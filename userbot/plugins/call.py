"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio
from userbot.utils import admin_cmd




@borg.on(admin_cmd(pattern=r"call"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @[ASIMOV_SUPPORT](t.me/ASIMOV_SUPPORT) ,`Please Connect me to my idiot bro,Ayush Durov`",
            "`User Authorised.`",
            "`Calling Pavel Durov`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Sar, Please Ban This nub nigga from telegram.`",    
            "`Pavel: May I Know Who Is This?`",
            "`Me: Yo Brah, itz me`  ",
            "`Pavel: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Guy Account Will Get Banned Within 24Hrs.`",
            "`Me: Thanks, See You Later Bruh.`",
            "`Pavel: Please Don't Thank Bruh, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Pavel: Yes Sir, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Pavel: Sure Sar \nTake care Bye Bye ;)`",
            "`Private Call Disconnected.`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])
