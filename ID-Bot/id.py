from pyrogram import Client, filters
from pyrogram.errors import UsernameInvalid, UsernameNotOccupied


# ID through Username
@Client.on_message(filters.command("id"))
async def id(idbot, msg):
	if not msg.chat.type == "private":
		await msg.reply(f"This {msg.chat.type}'s ID is `{msg.chat.id}`")
	else:
		if len(msg.command) == 1:
			await msg.reply(f"Your Telegram ID is: `{msg.from_user.id}`", quote=True)
		if len(msg.command) == 2:
			try:
				uname = msg.command[1]
				if uname.startswith("@"):
					check = uname[1:]
				else:
					await msg.reply("Username should start with '@'", quote=True)
					return
				try:
					user = await idbot.get_users(check)
					name = user["first_name"]
				except:
					user = await idbot.get_chat(check)
					name = user["title"]
				if len(name) <= 20:
					pass
				elif user["is_bot"]:
					name = "This Bot"
				else:
					name = "This User"
				id = user["id"]
				await msg.reply(f"{name}'s id is `{id}`", quote=True)
			except UsernameInvalid:
				await msg.reply("Invalid Username.", quote=True)
			except UsernameNotOccupied:
				await msg.reply("This username is not occupied by anyone", quote=True)
