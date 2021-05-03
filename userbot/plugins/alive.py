#FOR ASIMOV USERBOT.....
# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul and @ITZ_DARK_FURY ....and thanks to @Crackexy for the logos...
#Edited by @ITZ_DARK_FURY
# KANG WITH CREDITS ELSE GAY.....
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# 🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ASIMOV"

# Thanks to Sipak bro and Aryan.. 
# animation Idea by @ItzSipak && @Hell boy_pikachu
# Made by @hellboi_atul and @ITZ_DARK_FURY ....and thanks to @Crackexy for the logos...
#Edited by @ITZ_DARK_FURY
# Kang with credits else gay...
# alive.py for ASIMOV USERBOT
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/56689333be8d0666ad9ea.jpg"
#file2 = "" #nahi he mere pas 😢
#file3 = "" # i don't have 
#file4 = "" # anyone please make a logo for ASIMOV😅
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** 𝘼𝙎𝙄𝙈𝙊𝙑 𝙄𝙎 𝙊𝙉𝙇𝙄𝙉𝙀 **\n\n"
    pm_caption += "**yoosss Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ About My System ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/A_S_I_M_O_V)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝔸𝕊𝕀𝕄𝕆𝕍](https://github.com/DARK-FURY-xD/-ASIMOV)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [𝔸𝕊𝕀𝕄𝕆𝕍](https://github.com/DARK-FURY-xD/-ASIMOV)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

