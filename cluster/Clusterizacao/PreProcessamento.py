# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sys
import Utils

reload(sys)
sys.setdefaultencoding('utf-8')

class PreProcesso (object):
    def __init__(self):
        self.acentos = Utils.ACENTOS
        self.s_acentos = Utils.S_ACENTOS
        self.stop_words = set(stopwords.words("portuguese"))
        self.more_stopwords = Utils.MORE_STOPWORDS
        self.more_stopwords2 = Utils.MORE_STOPWORDS2
        self.stemmer = nltk.stem.RSLPStemmer()

    def tokenizarSetenca(self,texto):
        return word_tokenize(texto)

    def removerAcentos(self,texto):
        for i in range(0,len(self.acentos)):
            texto = texto.replace(self.acentos[i],self.s_acentos[i])
        return texto

    def removerStopWords(self,texto):
        texto = ' '.join([word for word in word_tokenize(texto) if word not in self.stop_words])
        texto = ' '.join([word for word in word_tokenize(texto) if word not in self.more_stopwords])
        return texto

    def removerStopWords2(self,texto):
        texto = ' '.join([word for word in word_tokenize(texto) if word not in self.stop_words])
        texto = ' '.join([word for word in word_tokenize(texto) if word not in self.more_stopwords2])
        return texto


    def removerSufixo(self,texto):
        texto_tratado=''
        for word in texto:
            texto_tratado = texto_tratado + ' ' + self.stemmer.stem(word)
        return texto_tratado

    def prePorcessar(self,texto):
        texto = texto.lower()
        texto = self.removerAcentos(texto)
        texto = self.removerStopWords(texto)
        texto = self.tokenizarSetenca(texto)
        texto = self.removerSufixo(texto)
        return texto

    def prePorcessar2(self,texto):
        texto = texto.lower()
        texto = self.removerAcentos(texto)
        texto = self.removerStopWords2(texto)
        #texto = self.tokenizarSetenca(texto)
        #texto = self.removerSufixo(texto)
        return texto