# -*- coding: utf-8 -*-
"""AI Assisstant.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hm_ovUWyDZWfJTA_WgekfEFLnScsDZ4j
"""

greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening','exit']
farewells = ['bye', 'goodbye', 'see you', 'farewell', 'good night']

def main():
    print("Hello, I'm your AI assistant. Ask me a question!")
    while True:
        user_input = input("> ")

        #if any(farewell in user_input for farewell in farewells):
            # return "Goodbye! Have a great day!"
        if user_input.lower() == 'exit' :
             print("Goodbye!")
             break
        response = process_input(user_input)
        print(response)

#pip install requests #to make HTTP requests

import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"The current weather in {city} is {weather} with a temperature of {temperature}°C"
    else:
        return "Sorry, I couldn't fetch the weather for that location."

from IPython.display import HTML, display #adding funnctionality to play songs

def play_song_on_youtube(song_name):
    query = '+'.join(song_name.split())
    url = f"https://www.youtube.com/results?search_query={query}"
    link = HTML(f"<a href='{url}' target='_blank'>Click here to play {song_name} on YouTube</a>")
    display(link)
    return f"Generated link for {song_name}"

def get_news(topic="general"): #default is empty string
    api_key = '33c7654580164308a5e00e98724fbc1d'
    if topic:   #topic is specified; use everything endpoint
        url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
    else:      #fetch top headlines
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        return [f"Failed to fetch news, status code: {response.status_code}"]
    articles = response.json().get('articles', [])
    news_items = []
    for article in articles:
        title = article['title']
        news_items.append(title)
        if len(news_items) == 5:
            break
    return news_items

import random
awaiting_trivia_answer = False
correct_trivia_answer = ""

trivia_questions = [
    {"question": "What is the chemical symbol for the element oxygen?", "answer": "O"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "Who was the first President of the United States?", "answer": "George Washington"},
    {"question": "Which country hosted the 2016 Summer Olympics?", "answer": "Brazil"},
    {"question": "Who played the character of Harry Potter in the movies?", "answer": "Daniel Radcliffe"},
    {"question": "What planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "Which is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "Which famous world leader was assassinated in 1963?", "answer": "John F. Kennedy"},
    {"question": "Which sport is known as the 'king of sports'?", "answer": "Soccer"},
    {"question": "What movie franchise is famous for, 'May the Force be with you'?", "answer": "Star Wars"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "Diamond"},
    {"question": "What city is known as the City of Love?", "answer": "Paris"},
    {"question": "What was the name of the first manned mission to land on the moon?", "answer": "Apollo 11"},
    {"question": "Who holds the record for most goals in FIFA World Cup history?", "answer": "Miroslav Klose"},
    {"question": "Which actor played Jack Dawson in 'Titanic'?", "answer": "Leonardo DiCaprio"},
    {"question": "How many elements are in the Periodic Table?", "answer": "118"},
    {"question": "Which country has the most natural lakes?", "answer": "Canada"},
    {"question": "In what year did the Berlin Wall fall?", "answer": "1989"},
    {"question": "What is the national sport of Japan?", "answer": "Sumo Wrestling"},
    {"question": "What year did the television show 'Friends' first air?", "answer": "1994"}]


def get_random_trivia_question():
    return random.choice(trivia_questions)

import webbrowser
import datetime
from datetime import datetime
import pytz #region
India_time = pytz.timezone("Asia/Calcutta")
timeInIndia = datetime.now(India_time)
def process_input(user_input, is_awaiting_answer=False, answer=""):
    if 'weather' in user_input:
        city = user_input.split('weather in ')[1]
        api_key = '347871bdc282a5933a6fef14d1758c35'
        return get_weather(city, api_key)
    global awaiting_trivia_answer
    global correct_trivia_answer
    user_input = user_input.lower()

    # Check for greetings
    if any(greeting in user_input for greeting in greetings):
        return "Hello! How can I assist you today?"

    # Check for farewells
    if any(farewell in user_input for farewell in farewells):
        return "Goodbye! Have a great day!"



    if awaiting_trivia_answer:
        if user_input == correct_trivia_answer.lower():
            awaiting_trivia_answer = False
            return "Correct!"
        else:
            awaiting_trivia_answer = False
            return f"Wrong! The correct answer is: {correct_trivia_answer}"

    if 'trivia' in user_input:
        question = get_random_trivia_question()
        awaiting_trivia_answer = True
        correct_trivia_answer = question['answer']
        return f"Question: {question['question']}"

    elif 'time' in user_input:
        current_time = timeInIndia.strftime("%I:%M:%p")
        return f'The current time is {current_time}'


    elif 'play music' in user_input or 'play song' in user_input:
          song_name = user_input.split('play music ')[1] if 'play music' in user_input else user_input.split('play song ')[1]
          return play_song_on_youtube(song_name)


    elif 'date' in user_input:
        today_date = timeInIndia.strftime("%Y-%m-%d")
        return f'The today date is {today_date}'

    elif 'news' in user_input:
          topic_index = user_input.find('news') + len('news')
          topic = user_input[topic_index:].strip()
          if topic:
                return get_news(topic)
          return get_news()

    elif 'sports' in user_input:
          return get_news('sports')

    elif 'open' in user_input:
        try:
            website = user_input.split('open ')[1]
            if not website.startswith('http://') and not website.startswith('https://'):
                website = 'http://' + website
            webbrowser.open(website)
            return f"Opening {website}"
        except Exception as e:
            return f"Failed to open the website due to: {str(e)}"


    else:
        return "I didn't understand"

if __name__ == "__main__":
    main()