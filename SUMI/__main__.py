from pyrogram import Client, filters, idle
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, BOT_USERNAME

# Accept commands starting with "/" or "."
COMMAND_PREFIXES = ["/", "."]

app = Client("banall", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("ping", prefixes=COMMAND_PREFIXES) & filters.group)
async def ping(client, message: Message):
    await message.reply_text("pong")

@app.on_message(filters.command("banall", prefixes=COMMAND_PREFIXES) & filters.group)
async def ban_all_members(client, message: Message):
    if not message.from_user:
        return  # Safety check

    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id != OWNER_ID:
        print(f"Unauthorized user {user_id} tried to run banall")
        return

    print(f"banall started by owner {user_id} in chat {chat_id}")
    count = 0
    async for member in client.get_chat_members(chat_id):
        member_id = member.user.id
        if member.user.is_bot or member_id == OWNER_ID:
            continue

        try:
            await client.ban_chat_member(chat_id, member_id)
            count += 1
            print(f"Banned user {member_id} ({count})")
        except Exception as err:
            print(f"⚠️ Could not ban user {member_id}: {err}")

    print(f"banall completed: banned {count} users.")

if __name__ == "__main__":
    print(f"Starting {BOT_USERNAME}...")
    app.start()
    print(f"{BOT_USERNAME} is online and waiting for commands.")
    idle()
    app.stop()
