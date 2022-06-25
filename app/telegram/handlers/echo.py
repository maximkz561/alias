from app.telegram.core import TelegramApp


@TelegramApp.app.on_message()
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")

