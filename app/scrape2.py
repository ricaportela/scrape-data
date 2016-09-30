import  requests,re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords

# pagina = urllib.request.urlopen()
# pagina = urllib.request.urlopen('http://stackoverflow.com/questions/893417/item-frequency-count-in-python')

# parse tree into a nicly formatted Unicode string
# print(soup.prettify())

pagina = urlopen('file:///home/ricardo/projetos/pontotel-crawler-cobolman/app/apinfo.html')
# pagina = urlopen("http://www.bbc.com/news")
soup = BeautifulSoup(pagina, "lxml")
texto = soup.get_text()
letras = re.sub("[^a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ]"," ",texto)
palavras = letras.lower().split()

# stopwords = nltk.corpus.stopwords.words('portuguese')
significados = [w for w in palavras if not w in stopwords.words("portuguese")]
contagem = [Counter(significados)]
frequency = {}

for word in significados:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print (words, frequency[words])
