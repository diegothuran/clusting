# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pickle
import nltk
import sys
from PreProcessamento import PreProcesso
reload(sys)
sys.setdefaultencoding('utf-8')

class ExtracaoSujeito(object):

    def maxFreq(self,dici):
        d = {"d": 0}
        max = d
        for palavra in dici:
            if (max.values()[0] < dici[palavra]):
                max = {palavra: dici[palavra]}
        return max

    def preparadorSeparador(self,text):
        tagger = pickle.load(open("cluster/Clusterizacao/tagger.pkl"))
        portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
        sentences = portuguese_sent_tokenizer.tokenize(text)
        tags = [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
        return tags

    def extrair(self,text):
        p = PreProcesso()
        text = p.prePorcessar2(text)
        tags = self.preparadorSeparador(text)
        dici = {}
        for tag in tags:
            for palavra in tag:
                if (palavra[0] in dici):
                    if(palavra[1]=="NOUN"):
                        dici[palavra[0]] = dici[palavra[0]] + 1
                else:
                    dici[palavra[0]] = 1

        return self.maxFreq(dici).keys()[0]