import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords


def scrape_function(url_pesquisa=None, palavra=None, texto=None):
    pagina = urlopen(url_pesquisa)
    soup = BeautifulSoup(pagina, "lxml")
    texto = soup.get_text()
    letras = re.sub("[^a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]", " ", texto)
    palavras = letras.lower().split()
    significados = [w for w in palavras if not w in stopwords.words("portuguese")]
    contagem = [Counter(significados)]
    return(contagem)
