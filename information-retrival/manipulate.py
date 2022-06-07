import re
import string

import nltk
from nltk import RegexpTokenizer
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from text_preprocessing import preprocess_text, to_lower, remove_url, remove_email, remove_phone_number, \
    remove_itemized_bullet_and_numbering, expand_contraction, check_spelling, remove_special_character, \
    remove_punctuation, remove_whitespace, normalize_unicode, remove_stopword, substitute_token, lemmatize_word
from textblob import TextBlob
from num2words import num2words
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from collections import Counter
from spellchecker import SpellChecker
from dateparser.search import search_dates
from dateutil import parser

def ManipulatingText(Text,IsQuery):
    # Text = Text.lower()
    # # print("lower: " + Text)
    #
    # doc = Abbreviation(Text)
    # # print("Abbreviation: ", doc)
    #
    # doc = RemoveMarks(doc)
    # # print("RemoveMarks: " , doc)
    #
    # doc = RemoveStopWord(doc)
    # # print("RemoveStopWord: " ,doc)
    #
    # # if not IsQuery:
    # #     doc = remove_freqwords(doc)
    #     # print("remove_freqwords: ", doc)
    #
    # doc = Stemming(doc)
    # # print("Stemming: " , doc)
    #
    # doc = Lemmatize(doc)
    # # print("Lemmatize: " , doc)
    #
    # doc = ReplaceNumbersWithWords(doc)
    # # print("ReplaceNumbersWithWords: " , doc)
    #
    # # if IsQuery:
    # doc = CorrectSpelling(doc)
    #     # print("CorrectSpelling: ", doc)
    #
    # doc = Tokenization(doc)
    # # print("Tokenization: " , doc)

    if hasattr(search_dates(Text), "__len__"):
        for date in search_dates(Text):
            if(date is string):
                Text.replace(date,  parser.parse(date))

    return ReplaceNumbersWithWords(preprocess_text(Text,[to_lower,
                                    remove_url,
                                    remove_email,
                                    remove_phone_number,
                                    remove_itemized_bullet_and_numbering,
                                    expand_contraction,
                                    remove_special_character,
                                    remove_punctuation,
                                    remove_whitespace,
                                    normalize_unicode,
                                    remove_stopword,
                                    substitute_token,
                                    lemmatize_word])).split()

def Abbreviation(Text):
    for word in Text:
        word=word.replace(" U.S ","UNITED STATE")
        word=word.replace(" U.N ","UNITED NATIONS")
        word=word.replace(" DEC ","DECEMBER")
        word=word.replace(" VIET NAM ","VIETNAM")
        word=word.replace(" VIET NAM'S ","VIETNAM")
        word=word.replace(" LOS ANGELES ","LOSANGELES")
    return Text

def RemoveMarks(text):
    PUNCT_TO_REMOVE = string.punctuation
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

def remove_freqwords(text):
    cnt = Counter()
    for word in text.split():
        cnt[word] += 1

    FREQWORDS = set([w for (w, wc) in cnt.most_common(10)])
    new_text = " ".join([word for word in str(text).split() if word not in FREQWORDS])
    RAREWORDS = set([w for (w, wc) in cnt.most_common()[:-10 - 1:-1]])
    return " ".join([word for word in str(new_text).split() if word not in RAREWORDS])


def ReplaceNumbersWithWords(text):
    temp = " "
    for x in str(text).split():
        if x.isnumeric():
            x = num2words(int(x))
        temp = temp + x + " "
    return temp

def Tokenization(Text):
    tokens = sent_tokenize(Text)
    result = []
    for word in tokens:
        for word2 in word_tokenize(word):
            result.append(word2)
    return result

def RemoveStopWord(text):
    NltkStopWords = set(stopwords.words('english'))
    return " ".join([word for word in str(text).split() if word not in NltkStopWords])

def CorrectSpelling(text):
    spell = SpellChecker()
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)

def Stemming(text):
    stemmer  = PorterStemmer()
    return " ".join([stemmer.stem(word) for word in text.split()])

def Lemmatize(text):
    wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
    lemmatizer = WordNetLemmatizer()
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

