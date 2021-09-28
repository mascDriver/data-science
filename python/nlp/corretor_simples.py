with open("artigos.txt", "r") as f:
    artigos = f.read()

print(artigos[:500])

import nltk
nltk.download('punkt')
lista_tokens = nltk.tokenize.word_tokenize(artigos)

def separa_palavras(lista_tokens):
    lista_palavras = []
    for token in lista_tokens:
        if token.isalpha():
            lista_palavras.append(token)
    return lista_palavras

lista_palavras = separa_palavras(lista_tokens)

def normalizacao(lista_palavras):
    lista_normalizada = []
    for palavra in lista_palavras:
        lista_normalizada.append(palavra.lower())
    return lista_normalizada

lista_normalizada = normalizacao(lista_palavras)
print(lista_normalizada[:5])
len(set(lista_normalizada))


palavra_exemplo = "lgica"

def insere_letras(fatias):
    novas_palavras = []
    letras = 'abcdefghijklmnopqrstuvwxyzàáâãèéêìíîòóôõùúûç'
    for E, D in fatias:
        for letra in letras:
            novas_palavras.append(E + letra + D)
    return novas_palavras

def gerador_palavras(palavra):
    fatias = []
    for i in range(len(palavra)+1):
        fatias.append((palavra[:i],palavra[i:]))
    palavras_geradas = insere_letras(fatias)
    return palavras_geradas

palavras_geradas = gerador_palavras(palavra_exemplo)
print(palavras_geradas)

def corretor(palavra)
    palavras_geradas = gerador_palavras(palavra)
    palavra_correta = max(palavras_geradas, key=probabilidade)
    return palavra_correta
  
  frequencia = nltk.FreqDist(lista_normalizada)
  
total_palavras = len(lista_normalizada)
frequencia.most_common(10)
def probabilidade(palavra_gerada):
    return frequencia[palavra_gerada]/total_palavras

probabilidade("lógica")
corretor(palavra_exemplo)
