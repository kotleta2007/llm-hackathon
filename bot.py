from dotenv import load_dotenv
import os
import logging
from telegram import Update
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# get token from environment
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
assert TOKEN is not None

# configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(name)s", level=logging.INFO
)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.effective_chat is not None
    assert update.message is not None
    assert update.message.text is not None
    to_send = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=to_send)



async def cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    assert update.effective_chat is not None
    response = "Just a command"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main() -> None:
    """Run the bot."""
    application = ApplicationBuilder().token(TOKEN).build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    cmd_handler = CommandHandler("cmd", cmd)

    application.add_handler(echo_handler)
    application.add_handler(cmd_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
