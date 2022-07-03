"""
Handlers and main logic of the bot.
"""
import logging

from telegram import Update
from telegram.ext import (
    ContextTypes, CommandHandler, ApplicationBuilder, ConversationHandler, MessageHandler, filters,
)
from source import auth_mongo
from capybara_bot.find_pic import get_picture_from_db


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

mongo_client = auth_mongo()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Command /start
    :param update: update
    :param context: context
    :return: await
    """
    logging.info('async start')
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=r"I'm a bot, please text me /cute or /sticker",
    )


async def cute(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a picture of capybara
    :param update: Update
    :param context: Context
    :return: await
    """
    logging.info('async cute')
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="You are welcome")
    await context.bot.send_photo(
        chat_id=update.effective_chat.id, photo=get_picture_from_db(mongo_client),
    )


async def sticker(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Send a sticker with random capybara
    :param update: Update
    :param context: Context
    :return: await
    """
    logging.info('async sticker')
    await context.bot.send_sticker(
        chat_id=update.effective_chat.id, sticker=get_picture_from_db(mongo_client),
    )


async def handle_else(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle any text
    :param update: Update
    :param context: Context
    :return: Await
    """
    logging.info('async else')
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="😍🥰😘 Please use following commands:\n /cute or /sticker",
    )


def run_server(token: str) -> None:
    """
    Run bot server with token
    :param token: your uniq token
    :return: None
    """
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('cute', cute), CommandHandler('sticker', sticker), ],
        states={},
        fallbacks=[CommandHandler('sticker', sticker), ],
    )
    else_handler = MessageHandler(filters.ALL, handle_else)

    application.add_handler(start_handler)
    application.add_handler(conv_handler)
    application.add_handler(else_handler)

    application.run_polling()
