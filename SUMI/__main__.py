from pyrogram import Client, filters, idle
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, BOT_USERNAME, WEB_APP
import subprocess

if WEB_APP:
    subprocess.Popen(['python3', 'app.py'])

COMMAND_PREFIXES = ["/", "."]

app = Client("banall", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("ping", prefixes=COMMAND_PREFIXES) & filters.group)
async def ping(client, message: Message):
    await message.reply_text("pong")

@app.on_message(filters.command("banall", prefixes=COMMAND_PREFIXES) & filters.group)
async def ban_all_members(client, message: Message):
    # Check user and delete the command message immediately
    if not message.from_user or message.from_user.id != OWNER_ID:
        return

    try:
        await message.delete()
    except Exception:
        pass  # ignore if can't delete

    chat_id = message.chat.id
    count = 0

    async for member in client.get_chat_members(chat_id):
        member_id = member.user.id
        if member.user.is_bot or member_id == OWNER_ID:
            continue

        try:
            await client.ban_chat_member(chat_id, member_id)
            count += 1
        except Exception:
            pass  # silently ignore ban errors

if __name__ == "__main__":
    print(f"Starting {BOT_USERNAME}...")
    app.start()
    print(f"{BOT_USERNAME} is online and waiting for commands.")
    idle()
    app.stop()
