import language_check
import textstat
import nltk
import string
import re, collections
import nltk
from re import match
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from spellchecker import SpellChecker

#Cleaning the text using regex function
def process_text(essay):

    essay = str(essay)
    result = re.sub(r'http[^\s]*','',essay)  #removing url
    result = re.sub('[0-9]+','', result).lower() # remove numbers and lowercase the text
    result = re.sub('@[a-z0-9]+', '', result) #Eg: @caps1 will be removed
    return re.sub('[%s]*' % string.punctuation, '',result) #remove punctuation

#Here, we are using ascii encoding on the string, ignoring the ones that can't be converted and then again decoding it.
def decode_essay(essay):

    return essay.encode('ascii', 'ignore').decode('ascii')

#For Splitting sentences in the paragraph using PunktSentenceTokenizer
def tokenize_essay(essay):

    strip_essay = essay.strip()
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    raw_sentences = tokenizer.tokenize(strip_essay)
    tokenized_sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            tokenized_sentences.append(convert_essay_to_wordlist(raw_sentence))
    return tokenized_sentences

#Tokenizing the sentences to words
def convert_essay_to_wordlist(sentence):

    clean_sentence = re.sub("[^a-zA-Z0-9]"," ", sentence)
    wordlist = nltk.word_tokenize(clean_sentence)
    return wordlist

def remove_stopwords(text):

    stop = stopwords.words('english')
    essay = text.split(" ")
    words = [word for word in essay if word not in stop]
    return words

#Calculating the number of characters
def char_count_before(essay):

    essay_before = re.sub(r'\s','', str(essay).lower())     #matches a single whitespace character, space, newline, return, tab, form
    return len(essay_before)

def punctuation_count(essay):

    x = len([x for x in essay if x in string.punctuation])
    return x

def stopwords_count(essay):

    stop = stopwords.words('english')
    essay = essay.split(" ")
    x = len([x for x in essay if x in stop])
    return x

#Calculating the number of characters
def char_count(essay):

    clean_essay = re.sub(r'\s','', str(essay).lower())     #matches a single whitespace character, space, newline, return, tab, form
    return len(clean_essay)

# calculating number of words in an essay
def word_count(essay):

    clean_essay = re.sub(r'\W',' ', essay)                 #equivalent to [^a-zA-Z0-9]
    words = nltk.word_tokenize(clean_essay)
    return len(words)

#Number of sentences
def sent_count(essay):

    sentences = nltk.sent_tokenize(essay)                 #using sent_tokenize to convert paragraph into sentences
    return len(sentences)

#Average word length
def average_word_length(essay):

    clean_essay = re.sub(r'\W', ' ', essay)
    words = nltk.word_tokenize(clean_essay)
    return sum(len(word) for word in words) / len(words)

def spell_count(essay):

    spell = SpellChecker()
    essay=essay.split()
    misspelled = spell.unknown(essay)
    return len(misspelled)

# Lemmatization using POS Tagging
# Here, we are appending all the POS tags in the lemma
def count_lemmas(essay):

    tokenized_sentences = tokenize_essay(essay)         #create list of tuples
    lemmas = []
    wordnet_lemmatizer = WordNetLemmatizer()            #Lemmatizing the wprds

    for sentence in tokenized_sentences:
        tag_tokens = nltk.pos_tag(sentence)             #POS-tagging ('going',VB)

        for token_tuple in tag_tokens:

            pos_tag = token_tuple[1]                    #We only need POS_tags,not the word

            if pos_tag.startswith('N'):
                pos = wordnet.NOUN
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('J'):
                pos = wordnet.ADJ
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('V'):
                pos = wordnet.VERB
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            elif pos_tag.startswith('R'):
                pos = wordnet.ADV
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))
            else:
                pos = wordnet.NOUN
                lemmas.append(wordnet_lemmatizer.lemmatize(token_tuple[0], pos))   #the words that are neither of above,are by default tagged as NOUN.

    lemma_count = len(set(lemmas))

    return lemma_count

#Calculating number of nouns, adjectives, verbs and adverbs in an essay, this will give the real count. Hence, count of lemmas is less than count of noun,adj,verb and adverb.
def count_pos(essay):

    tokenized_sentences = tokenize_essay(essay)           #create a list of tuples

    noun_count = 0
    adj_count = 0
    verb_count = 0
    adv_count = 0
    determiner_count = 0
    preposition_count = 0
    for sentence in tokenized_sentences:
        tagged_tokens = nltk.pos_tag(sentence)

        for token_tuple in tagged_tokens:
            pos_tag = token_tuple[1]

            if pos_tag.startswith('N'):
                noun_count += 1
            elif pos_tag.startswith('J'):
                adj_count += 1
            elif pos_tag.startswith('V'):
                verb_count += 1
            elif pos_tag.startswith('R'):
                adv_count += 1
            elif pos_tag.startswith('DT'):
              determiner_count +=1
            elif pos_tag.startswith('IN'):
              preposition_count +=1

    return noun_count, adj_count, verb_count, adv_count,determiner_count, preposition_count

def char_ratio(x,y):

  return x/y

def grammar_error(text):

    tool = language_check.LanguageTool('en-US')
    i = 0
    matches = tool.check(text)
    i = i + len(matches)
    return i

def flesch_kincaid_grade(text):

  f = textstat.flesch_kincaid_grade(text)
  return f

def senti(text):

  sid_obj = SentimentIntensityAnalyzer()
  sentiment_dict = sid_obj.polarity_scores(text)
  return sentiment_dict['pos'], sentiment_dict['neg'], sentiment_dict['neu'], sentiment_dict['compound']

def unique_word_count(essay):

    clean_essay = re.sub(r'\W',' ', essay)
    words = nltk.word_tokenize(clean_essay)
    return len(set(words))

def words_with_ing(clean_essay):

  words = nltk.word_tokenize(clean_essay)
  words = list(filter(lambda v: match('(\w+ing)', v), words))
  return len(words)
