from pymongo import TEXT 
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

ADMIN_TEXT ="""𝗧𝗛𝗜𝗦 𝗜𝗦 𝗠𝗬 𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

/setskip - To Skip Indexing File range
/broadcast - To broadcast Message To users 
/deleteall - Delete All Files From Database 
/deletefile  - Delete a replyed File from database 
/total - Get Total Uses and Files 
/imdb - To Turn on and off Imdb 
/fsub - To Set Force Subscribe 
/autodel - To Set Autodelete Time
"""

ABOUT_TEXT = """ <blockquote>
‣ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/TGxSeriesBot'>Sᴇʀɪᴇs Bᴏᴛ</a>
‣ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a>
‣ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/CyberTGx'>ᴄʏʙᴇʀ ᠰ ᴛɢ</a>
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a>
‣ ᴘʀɪᴍᴀʀʏ ᴅʙ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
‣ sᴇᴄᴏɴᴅᴀʀʏ ᴅʙ : <a href='https://www.freesqldatabase.com/'>sᴏ̨ʟ ᴅʙ</a>
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://t.me/quickfastt'>ǫᴜɪᴄᴋ ꜰᴀsᴛ</a></b></blockquote>"""

ABOUT_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("💻 Source Code", url="https://github.com/CyberTG/SeriesFilterBot")
        ],
        [
            InlineKeyboardButton("🏡 ʜᴏᴍᴇ", callback_data="cyber|home"),
            InlineKeyboardButton("🕵‍♂ ʜᴇʟᴘ", callback_data="help|menu")
        ],
    ]
)
