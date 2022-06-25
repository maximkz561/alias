from pyrogram import Client

from app.config import get_config


class TelegramApp:
    app = Client(
        "my_account",
        api_id=get_config().telegram.api_id,
        api_hash=get_config().telegram.api_hash,
        bot_token=get_config().telegram.token
    )
