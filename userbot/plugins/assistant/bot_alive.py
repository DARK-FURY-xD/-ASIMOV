#CREDITS πΏπΌππ πΎππ½ππΌβ€
#Contributor DANISH...
from telethon import events

from userbot import ALIVE_NAME, bot

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/56689333be8d0666ad9ea.jpg"
pm_caption = "β₯ **ASSISTANT IS:** `ONLINE`\n\n"
pm_caption += "β₯ **SYSTEMS STATS**\n"
pm_caption += "β₯ **Telethon Version:** `1.15.0` \n"
pm_caption += "β₯ **Python:** `3.8.6` \n"
pm_caption += "β₯ **Database Status:**  `Functional`\n"
pm_caption += "β₯ **Current Branch** : `master`\n"
pm_caption += f"β₯ **Version** : `2.0`\n"
pm_caption += f"β₯ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "β₯ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "β₯ **License** : [GNU General Public License v3.0](https://github.com/DARK-FURY-xD/-ASIMOV/blob/master/LICENSE)\n"
pm_caption += "β₯ **Copyright** : By [ASIMOV](https://t.me/ASIMOV_SUPPORT)\n"
pm_caption += "[Assistant By ASIMOV](https://t.me/ASIMOV_SUPPORT)"

# only Owner Can Use it
@tgbot.on(events.NewMessage(pattern="^/alive", func=lambda e: e.sender_id == bot.uid))
async def _(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=pm_caption)
