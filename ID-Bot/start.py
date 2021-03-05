from Data import Data
from Config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.private & filters.incoming & filters.command("start"))
async def start(idbot, msg):
    print("/start")
    user = await idbot.get_me()
    mention = user["mention"]
    await idbot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention, msg.from_user.id),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )
