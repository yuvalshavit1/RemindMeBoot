import schedule
from dotenv import load_dotenv
import threading
import os
import telebot
from bot_functions import process_user_message, schedule_job

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(func=lambda message: True)
def user_message(message):
    process_user_message(message, bot)


if __name__ == "__main__":
    threading.Thread(target=lambda: schedule.run_continuously()).start()
    bot.polling(none_stop=True)
