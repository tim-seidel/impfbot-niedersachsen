import telegram  #package python-telegram-bot

import timeutil
from logger import logger
import constants

#Sends a message to the telegram bot
def send_to_telegram(msg, is_important=False) -> None:
    msg_with_header = timeutil.get_time_id_stamp(constants.client_id) + " " + msg

    try:
        if constants.enable_telegram and (is_important or constants.enable_telegram_level_info):
            telegram_bot = telegram.Bot(token=constants.bot_token)
            for chat_id in constants.telegram_chat_ids:
                try:
                    telegram_bot.sendMessage(chat_id=chat_id, text=msg_with_header)
                except Exception as e:
                    logger.error(e)
    except Exception as e:
        #Something was wrong with the bot
        logger.error(e)

