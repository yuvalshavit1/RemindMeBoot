import threading
import schedule
import telebot
import chatgpt_api


def job(chat_id, message, bot):
    bot.send_message(chat_id, message)


def schedule_job(chat_id, message, bot):
    threading.Timer(10, job, args=(chat_id, message, bot)).start()


def process_user_message(message, bot):  # Pass the bot as a parameter
    greet_keywords = ["hello", "hey", "hi", "what's up"]
    bye_keywords = ["bye", "see you", "goodbye", "see you"]
    help_keywords = ["help"]
    remind_keywords = ["remind", "reminder", "schedule"]

    # Convert the message text to lowercase for case-insensitive comparison
    lower_text = message.text.lower()

    if any(keyword in lower_text for keyword in remind_keywords):
        msg = message.text
        chatgpt_api.openai_message(msg, message.chat.id, bot)  # Pass the chat_id and bot instance
        msg = f"No problem. I will send you a reminder at the time you requested."
    elif any(keyword in lower_text for keyword in greet_keywords):
        msg = f"Hey {message.from_user.first_name}! How can I help you?"
    elif any(keyword in lower_text for keyword in bye_keywords):
        msg = "Bye. Can't wait to hear from you again"
    elif any(keyword in lower_text for keyword in help_keywords):
        msg = "I'm a reminder bot. You can ask me for a reminder request and I will send you notification at the" \
              "requested time. For example: 'remind me on Tuesday at 17:00 to go to the gym'"
    elif message.text == "/start":
        msg = f"Hey {message.from_user.first_name}! How can I help you?"
    else:
        msg = "I don't understand your request. For more information press 'help"

    chat_id = message.chat.id
    schedule_job(chat_id, msg, bot)
