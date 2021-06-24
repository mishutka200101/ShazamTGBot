import telebot
import requests
import bot_token
import converter
import http.client
import json

bot = telebot.TeleBot(bot_token.TOKEN)


@bot.message_handler(commands=['start'])
def salam(message):
    bot.send_message(message.from_user.id, "Hi, this is Shazam bot.\nSend your audio, so i can find ut for you!")


@bot.message_handler(content_types=['voice'])
def voice_handler(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f'voice.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    get_audio()


def get_audio():
    url = "https://shazam.p.rapidapi.com/songs/detect"

    payload = converter.convert_audio()
    headers = {
        'content-type': "text/plain",
        'x-rapidapi-key': "901d829e6amshca40bae08527ec5p104f87jsn821ed9db023a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


bot.polling()
