import nltk
# nltk.download('punkt_tab')
import ssl


import openai
from nltk.tokenize import word_tokenize
from nltk import pos_tag

import os
from dotenv import load_dotenv

load_dotenv()

client = openai
APIKEY = os.getenv('OPENAI_API_KEY')
openai.api_key = APIKEY
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

def dream_parser(sentence):
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)

    nouns = [word for word, pos in tagged_words if pos.startswith('NN')]  # Nouns
    verbs = [word for word, pos in tagged_words if pos.startswith('VB')]

    return nouns, verbs

def ai_interpretation(sentence):
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a hopeful dream psychologist. You will be interepting dreams from the user."},
        {
            "role": "user",
            "content": f"Given this paragraph of someones dream. Return a thoughtful analysis of this dream. {sentence}"
            }
        ]
    )
    return completion.choices[0].message
# nouns, verbs= dream_parser('The brown cat jumped over the fox')
# print(nouns, verbs)
print(ai_interpretation("i had a dream all my teeth fell out, but i was also reigned champion of teeth falling out contest"))

