import logging
import requests
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MessageNotModified

@cyber.on_callback_query(filters.regex(r"^help\|"))
async def help_menu_handler(cyber, query):
    help_text = (
        "<b>💡 Help & Instructions</b>\n\n"
        "1. <b>Search</b>: Simply send the <b>name</b> of the movie or series you are looking for.\n"
        "2. <b>Select</b>: Tap the <b>Season</b> button for a series.\n"
        "3. <b>Filter</b>: Choose the <b>Language</b> and then the <b>Quality</b>.\n"
        "4. <b>Receive</b>: The bot will automatically start sending the files to you.\n\n"
        "<i>If you see 'No series found', try a slightly different or shorter name.</i>"
    )
    HELP_KEYBOARD = InlineKeyboardMarkup([
        [InlineKeyboardButton("🏡 Home", callback_data="cyber|"),
         InlineKeyboardButton("🕹 Admins", callback_data="admin_cmd|")]
    ])
    try:
        await query.message.edit_caption(
            help_text, reply_markup=HELP_KEYBOARD, parse_mode=enums.ParseMode.HTML
        )
    except MessageNotModified:
        pass
    except Exception as e:
        logging.error(f"Error editing message caption in help_menu_handler: {e}")
        try:
            await query.message.edit_text(
                help_text, reply_markup=HELP_KEYBOARD, parse_mode=enums.ParseMode.HTML
            )
        except Exception:
            pass
    await query.answer("Showing help menu.")


@cyber.on_callback_query(filters.regex(r"^cyber\|"))
async def cyber_menu_handler(cyber, query):
    home_text = (
        "<b>👋 Hey Bro</b>\n\n"
        "<b>I Am Your Series-Filter Bot</b> - advanced, powerful and designed to make your group a Series Request Group!\n"
        "You Can Also Search Series Here\n\n"
        "<b>Let's get started! 🚀</b>"
    )
    CYBER_KEYBOARD = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚙️Help", callback_data="help|"),
         InlineKeyboardButton("🤠About", callback_data="about|")]
    ])
    try:
        await query.message.edit_caption(
            home_text, reply_markup=CYBER_KEYBOARD, parse_mode=enums.ParseMode.HTML
        )
    except MessageNotModified:
        pass
    except Exception as e:
        logging.error(f"Error editing message caption in cyber_menu_handler: {e}")
        try:
            await query.message.edit_text(
                home_text, reply_markup=CYBER_KEYBOARD, parse_mode=enums.ParseMode.HTML
            )
        except Exception:
            pass
    await query.answer("Back To Home")


@cyber.on_callback_query(filters.regex(r"^admin_cmd\|"))
async def admin_menu_handler(cyber, query):
    user_id = query.from_user.id
    is_authorized = False
    try:
        if isinstance(ADMIN_USERS, (list, tuple, set)):
            is_authorized = user_id in ADMIN_USERS
        else:
            is_authorized = (user_id == int(ADMIN_USERS))
    except Exception:
        is_authorized = False

    if not is_authorized:
        await query.answer("You are not authorized. Only the admin can open this menu.", show_alert=True)
        return

    about_text = ADMIN_TEXT
    ADMIN_KEYBOARD = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back", callback_data="cyber|"),
         InlineKeyboardButton("Close", callback_data="close")]
    ])
    try:
        await query.message.edit_caption(
            about_text, reply_markup=ADMIN_KEYBOARD, parse_mode=enums.ParseMode.HTML
        )
    except MessageNotModified:
        pass
    except Exception as e:
        logging.error(f"Error editing message caption in admin_menu_handler: {e}")
        try:
            await query.message.edit_text(
                about_text, reply_markup=ADMIN_KEYBOARD, parse_mode=enums.ParseMode.HTML
            )
        except Exception:
            pass
    await query.answer("Showing admin menu.")


@cyber.on_callback_query(filters.regex(r"^about\|"))
async def about_menu_handler(cyber, query):
    about_text = ABOUT_TEXT
    reply_markup = ABOUT_KEYBOARD
    try:
        await query.message.edit_caption(
            about_text, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML
        )
    except MessageNotModified:
        pass
    except Exception as e:
        logging.error(f"Error editing message caption in about_menu_handler: {e}")
        try:
            await query.message.edit_text(
                about_text, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML
            )
        except Exception:
            pass
    await query.answer("Showing about information.")



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
            InlineKeyboardButton("🔰 Home", callback_data="cyber|"),
            InlineKeyboardButton("❤️‍🩹 Developer", url="https://t.me/CyberTGx")
        ],
    ]
)
