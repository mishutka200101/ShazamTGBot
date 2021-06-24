import telebot
import requests
import bot_token
import converter
import json


bot = telebot.TeleBot(bot_token.TOKEN)
song_name = ""
artist_name = ""


@bot.message_handler(commands=['start'])
def salam(message):
    bot.send_message(message.from_user.id, "Hi, this is Shazam bot.\nSend your audio, so i can find it for you!")


@bot.message_handler(content_types=['voice'])
def voice_handler(message):
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(f'voice.ogg', 'wb') as new_file:
        new_file.write(downloaded_file)
    get_audio()
    bot.reply_to(message, "Song " + song_name + " by " + artist_name)


def get_audio():
    global song_name
    global artist_name
    url = "https://shazam.p.rapidapi.com/songs/detect"

    payload = converter.convert_audio()
    headers = {
        'content-type': "text/plain",
        'x-rapidapi-key': "901d829e6amshca40bae08527ec5p104f87jsn821ed9db023a",
        'x-rapidapi-host': "shazam.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    data = json.loads(response.text)
    song_name = data['track']['title']
    artist_name = data['track']['subtitle']


bot.polling()
