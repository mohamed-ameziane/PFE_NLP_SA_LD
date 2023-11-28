from bs4 import BeautifulSoup
import re
from unidecode import unidecode
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
french_stopwords = stopwords.words('french')
from nltk.stem.snowball import FrenchStemmer

#French Pre Processing Functions.
def htmlTags_remover(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

def apostrophe_remover(text):
    return re.sub("\'", " ", text).strip()

def alphaNumeric_remover(text):
     return re.sub("\S*\d\S*", "", text).strip()

def accent_remover(text):
    return unidecode(text)

def specialChar_remover(text):
    return re.sub('[^a-zA-Z]', ' ', text)

def extraSpaces_remover(text):
    return " ".join(text.split())

def textNormaliser(text):
    text = htmlTags_remover(text)
    text = apostrophe_remover(text)
    text = alphaNumeric_remover(text)
    text = accent_remover(text)
    text = specialChar_remover(text)
    text = extraSpaces_remover(text)
    text = text.lower()
    return text

def textTokenizer(text):
    return word_tokenize(text, language='french')

for word in ['n', 'ne', 'pas', 'plus', 'jamais', 'guere', 'personne', 'aucun', 'ni', 'aucune', 'rien']:
    if word in french_stopwords:
        french_stopwords.remove(word)
    else:
        continue

def stopwords_remover(tokens):
    return [word for word in tokens if word not in french_stopwords]

def textStemmer(tokens):
    stemmer = FrenchStemmer()
    return [stemmer.stem(word) for word in tokens]

def textCleaner(text):
    text = textNormaliser(text)
    tokens = textTokenizer(text)
    cleanedTokens = stopwords_remover(tokens)
    stemmedText = textStemmer(cleanedTokens)
    text = " ".join(stemmedText)
    return text


#Fonction to clean multilanguages text destined for "language identificator".
def textCleanerMulti(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', ' ', text)
    text = re.sub(r'\[.*?\]', ' ', text)
    text = text.lower()
    return text
