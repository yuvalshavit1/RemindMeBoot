from datetime import datetime
import openai
import telebot

openai.api_key = "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"

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def openai_message(msg, chat_id, bot):  # Pass the chat_id and bot as parameters
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "user",
                                                 "content": f"Return only the 'date' and 'time' without writing "
                                                            f"something else."
                                                            f"return it like JSON format with the value date and "
                                                            f"value time"
                                                            f"with two different lines"
                                                            f"Assume that today is {current_datetime}.If you didn't "
                                                            f"received an exact time, you can assume it's noon and not "
                                                            f"in the night"
                                                            f"Extract the"
                                                            f"date and the time from this message: {msg}"},
                                            ]
                                            )
    choices = response['choices']

    if choices:
        generated_message = choices[0]['message']['content']
        print(generated_message)
    else:
        print("No message generated.")
