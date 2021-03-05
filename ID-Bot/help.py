from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup


# Help Message
@Client.on_message(filters.private & filters.command(["help"]))
async def help(idbot, msg):
	await msg.reply(
		text=Data.HELP,
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(Data.home_button),
	)
