import json

import requests
from dotenv import load_dotenv
import os
import base64
from requests import post, get
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from requests import post, get
from typing import Final



class SpotifyAPI:
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    def __init__(self):
        load_dotenv()
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.token = self.get_token()

    #Отримуємо токен
    def get_token(self):
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + auth_base64,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data=data)
        json_result = json.loads(result.content)
        return json_result["access_token"]
    #creating authorization header
    def get_auth_header(self):
        return {"Authorization": "Bearer " + self.token}
    #searching for the artist ID to use during the search
    def search_for_artist(self, artist_name):
        url = "https://api.spotify.com/v1/search"
        headers = self.get_auth_header()
        query = f"?q={artist_name}&type=artist&limit=1"

        query_url = url + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)["artists"]["items"]
        if len(json_result) == 0:
            return None
        return json_result[0]
    #searching for top 10 tracks
    def get_songs(self, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
        headers = self.get_auth_header()
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["tracks"]
        return json_result


class TelegramBot:
    TOKEN: Final = "token"
    BOT_USERNAME: Final = "username"
    def __init__(self, token):
        self.token = token
        self.app = Application.builder().token(self.token).build()

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Hello! Nice to meet you!')

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            'I am a bot that provides you with top-5 tracks of your favorite artist in Spotify! Also, I can tell you the weather in your city!')

    async def top_tracks_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        artist_name = ' '.join(context.args)

        if not artist_name:
            await update.message.reply_text(
                'Please provide the name of the artist after the command, like /toptracks ArtistName')
            return

        spotify = SpotifyAPI()
        result = spotify.search_for_artist(artist_name)

        if result is not None:
            artist_id = result["id"]
            songs = spotify.get_songs(artist_id)

            if songs:
                response = f"Top tracks for {artist_name}:\n"
                for idx, song in enumerate(songs):
                    response += f"{idx + 1}. {song['name']}\n"

                await update.message.reply_text(response)
            else:
                await update.message.reply_text(f"No top tracks found for {artist_name}")
        else:
            await update.message.reply_text(f"No information found for {artist_name}")

    async def custom_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('This is a custom command.')

    def handle_response(self, text: str) -> str:
        processed = text.lower()
        if 'hello' in processed:
            return 'Hey there!'
        if 'how are you?' in processed:
            return 'I\'m fine!'
        if 'i love python' in processed:
            return 'Me too!'
        return 'Sorry, I do not understand it... yet!'

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type = update.message.chat.type
        text = update.message.text

        print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

        if message_type == 'group':
            if BOT_USERNAME in text:
                new_text = text.replace(BOT_USERNAME, '').strip()
                response = self.handle_response(new_text)
            else:
                return
        else:
            response = self.handle_response(text)

        print('Bot: ', response)
        await update.message.reply_text(response)

    async def error(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"Update {update} caused error {context.error}")

    async def get_weather_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        city_name = ' '.join(context.args)

        if not city_name:
            await update.message.reply_text(
                'Please provide the name of the city after the command, like /getweather CityName')
            return

        weather_info = self.get_weather_info(city_name)

        if weather_info:
            if 'main' in weather_info:
                response = f"Weather information for {city_name}:\n"
                response += f"Temperature: {weather_info['main']['temp']}°C\n"
                response += f"Condition: {weather_info['weather'][0]['description']}\n"
                response += f"Humidity: {weather_info['main']['humidity']}%\n"
                response += f"Wind Speed: {weather_info['wind']['speed']} m/s"
            else:
                response = f"Error fetching weather information for {city_name}. Please try again later."
        else:
            response = f"No weather information found for {city_name}. Please try again later."

        await update.message.reply_text(response)

    def get_weather_info(self, city_name):
        api_key = "key"
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric',  # We can change this to 'imperial' for Fahrenheit
        }

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            weather_info = response.json()

            if 'main' not in weather_info:
                print(f"Error in OpenWeatherMap response: {weather_info}")
                return None

            return weather_info
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            print(f"Response content: {response.content}")
            return None
        except Exception as e:
            print(f"Error fetching weather information: {e}")
            return None
    def run(self):
        print('Starting bot...')
        self.app.add_handler(CommandHandler('start', self.start_command))
        self.app.add_handler(CommandHandler('help', self.help_command))
        self.app.add_handler(CommandHandler('toptracks', self.top_tracks_command))
        self.app.add_handler(CommandHandler('custom', self.custom_command))
        self.app.add_handler(CommandHandler('weather', self.get_weather_command))
        self.app.add_handler(MessageHandler(filters.TEXT, self.handle_message))
        self.app.add_error_handler(self.error)
        print('Polling...')
        self.app.run_polling(poll_interval=1)


if __name__ == '__main__':
    TOKEN = "token"
    BOT_USERNAME = "username"

    bot = TelegramBot(TOKEN)
    bot.run()
