from pyrogram import Client, filters, idle
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID, BOT_USERNAME

app = Client("banall", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("banall") & filters.group)
async def ban_all_members(client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    if user_id != OWNER_ID:
     
        return

    async for member in client.get_chat_members(chat_id):
        member_id = member.user.id

        if member.user.is_bot or member_id == OWNER_ID:
            continue

        try:
            await client.ban_chat_member(chat_id, member_id)
        except Exception as err:
            print(f"⚠️ Could not ban user {member_id}: {err}")


if __name__ == "__main__":
    app.start()
    print(f"{BOT_USERNAME} is online and running silently.")
    idle()
    app.stop()
