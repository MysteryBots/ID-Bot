from idbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to {} \n\nUsing this bot you can check id of any group, user, bot, channel and even stickers."

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @Its_HellBot ♥"
    START += "\n\nP.S ~ Your ID is `{}`"

    # About Message
    ABOUT = "**About This Bot** \n\nThis is an ID bot by @Its_HellBot"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Help Message
    HELP = "**Help & Features** \n\n1) Send any message to get your ID. \n2) Forward any message from any user/bot/channel or anonymous admins to get ID. \n3) Send any sticker to get sticker id. \n4) Use Inline Mode to send your ID in any chat. \n5) Add in group / channel to get ID. \n6) Use /id command: \n- in private: To get ID through username \n- in group/channel: To get ID of that chat. \n\nBy @Its_HellBot ♥"

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✌ How to Use ✌", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("♥ HELLBOT CHANNEL ♥", url="https://t.me/Its_HellBot")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/HellBot_Chat")],
    ]
