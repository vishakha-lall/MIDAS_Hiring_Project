import praw
from dotenv import load_dotenv
load_dotenv()
import os
import string
import spacy
sp = spacy.load('en')
from nltk.stem import WordNetLemmatizer
import contractions
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords, wordnet
import itertools
import pickle
from keras.models import load_model
from keras.preprocessing import sequence
import numpy as np

def get_submission_data(input_url):
    reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), user_agent=os.getenv("USER_AGENT"))
    submission = reddit.submission(url=input_url)
    data = list()
    if submission.title:
        data.append(submission.title)
    if submission.selftext:
        data.append(submission.selftext)
    if submission.comments:
        comments_content = [str(comment.body) for comment in submission.comments[:50]]
        comments_content = '; '.join([str(elem) for elem in comments_content])
        data.append(comments_content)
    return data

def get_processed_data(input_data):
    punc = string.punctuation
    stop_words = set(sp.Defaults.stop_words)
    wnl = WordNetLemmatizer()
    processed_data = list()
    for data in input_data:
        data = data.replace(r'http\S+', '').replace(r'www\S+', '')
        data = [contractions.fix(word) for word in str(data).split()]
        data = " ".join(data)
        data = word_tokenize(data)
        data = [word.lower() for word in data]
        data = [word for word in data if word not in punc]
        data = [word for word in data if word not in stop_words]
        data = nltk.tag.pos_tag(data)
        data = [(word, get_wordnet_pos(pos_tag)) for (word, pos_tag) in data]
        data = [wnl.lemmatize(word,tag) for word, tag in data]
        processed_data.append(data)
    flatten = itertools.chain.from_iterable
    processed_data = list(flatten(processed_data))
    processed_data = " ".join(processed_data)
    return [processed_data]

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def get_model_prediction(input_processed_data):
    flairs = ['Non-Political','Politics','Coronavirus','AskIndia','Policy/Economy','Business/Finance','Photography','[R]eddiquette','Sports','Science/Technology','Others']
    with open('tokenizer.pkl', 'rb') as handle:
        tokenizer = pickle.load(handle)
    model = load_model('model_lstm.h5')
    tokenized_input = tokenizer.texts_to_sequences(input_processed_data)
    sequence_input = sequence.pad_sequences(tokenized_input, maxlen=80)
    prediction = model.predict(sequence_input)
    flatten = itertools.chain.from_iterable
    prediction = list(flatten(prediction))
    prediction = np.array(prediction)
    idx = np.argmax(prediction)
    return flairs[idx]
