#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os
nltk.download('punkt')
#Define a function to clean up text from web articles
def get_article_text(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    text = article.text
    return text
#Get the article text
article_text = get_article_text('https://www.therandomblogs.in/2022/02/top-5-best-vr-headsets-under-5000.html')
#Print the article text
print(article_text)
#Convert the article text to speech
language = 'en'
speech = gTTS(text=article_text, lang=language, slow=False)
#Save the converted audio to a file
speech.save('article.mp3')
