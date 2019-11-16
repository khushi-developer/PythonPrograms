import json
import requests

def speak(str):
    from win32com.client import Dispatch
    speak =Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for today")
    url="http://jsonviewer.stack.hu/#http://https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=API_KEY"
    news=requests.get(url).text
    news_dict=json.loads(news)
    print(news_dict["articles"])
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..........Listen carefully")