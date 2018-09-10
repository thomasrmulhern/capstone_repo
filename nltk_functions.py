from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# TOKENIZER


def s_tokenize(text):
    '''nltk sentence tokenizer'''
    from nltk.tokenize import sent_tokenize
    return sent_tokenize(str(text))


def w_tokenize(text):
    '''nltk word tokenizer'''
    from nltk.tokenize import word_tokenize
    tokenizer = RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(str(text))


#STOPWORDS


stop_words = set(stopwords.words('english'))

def filter_stopwords(text):
    '''nltk filter stopwords'''
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    return [w for w in text if not w in stop_words]


#STEM/LEM


def lem(text):
    '''nltk lemmatizer'''
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(t) for t in text]
