import os
import asyncio
import sys
import git
import heroku3
# Changed root to DOLLSPAM
from DollXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9
from DollXSpamBot import OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, deadlyversion
from DollXSpamBot import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
# alive Pic By Default It's Will Show Our
from DollXSpamBot import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

DOLL_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/f8d63b1dc5676fc9988f1.jpg"


DOLL = "โฏ ๐ฟ๐ค๐ก๐ก โ ๐๐ฅ๐๐ข ๐๐๐๐ โฏ\n\n"
DOLL += f"**๊ง๐ฎ๐ณ ๐  ๐๐ถ๐น๐ ๐ผ๐ ๐ผ๐๐น๐พ๐ถ  ๐ ๐ฎ๐ณ๊ง**\n"
DOLL += f"โโโโโโโโโฏโขโฐโโโโโโโโ\n"
DOLL += f"โข **๐ฟ๐๐๐ท๐พ๐ฝ ๐๐ด๐๐๐ธ๐พ๐ฝ** : `3.10.1`\n"
DOLL += f"โข **๐๐ด๐ป๐ด๐๐ท๐พ๐ฝ ๐๐ด๐๐๐ธ๐พ๐ฝ** : `{version.__version__}`\n"
DOLL += f"โข **๐ณ๐พ๐ป๐ป ๐ ๐๐ฟ๐ฐ๐ผ ๐ฑ๐พ๐ ๐๐ด๐๐๐ธ๐พ๐ฝ**  : `{deadlyversion}`\n"
DOLL += f"โข **แดสแดษดษดแดส** : [Join.](https://t.me/DollxSpam_BOT)\n"
DOLL += f"โข **Source Code** : [โขRepoโข](https://github.com/DOMINATOR-XD/DollXSpamBot)\n"
DOLL += f"โโโโโโโโโฎโขโญโโโโโโโโ\n\n"   
                                  
@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sdoll(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
     await BOT0.send_file(event.chat_id,
                                  DOLL_PIC,
                                  caption=DOLL,
                                  buttons=[
        [
        Button.url("โบ๏ธแดสแดษดษดแดสโบ๏ธ", "https://t.me/Dollx_spambot"),
        Button.url("๐ฎ๐ณsแดแดแดแดสแด๐ฎ๐ณ", "https://t.me/DollxSpam_BOT")
        ],
        [
        Button.url("โข ๐สแดแดแด๐ โข", "https://github.com/DOMINATOR-XD/DollXSpamBot")
        ]
        ]
        )
