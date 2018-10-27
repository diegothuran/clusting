# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import sys
from ..models import Review
reload(sys)
sys.setdefaultencoding('utf-8')


ACENTOS = ['á', 'é', 'í', 'ó', 'ú', 'à', 'è', 'ì', 'ò', 'ù', 'ã', 'ẽ', 'ĩ', 'õ', 'ũ', 'â', 'ê', 'î', 'ô','û','ç']

S_ACENTOS = ['a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o', 'u', 'a', 'e', 'i', 'o','u','c']

MORE_STOPWORDS = ['ja', 'q', 'd', 'ai', 'desse', 'dessa', 'disso', 'nesse', 'nessa', 'nisso', 'esse', 'essa', 'isso', 'so', 'mt', 'vc', 'voce', 'ne', 'ta', 'to', 'pq',
                     'cade', 'kd', 'la', 'e', 'eh', 'dai', 'pra', 'vai', 'olha', 'pois','fica', 'muito', 'muita', 'muitos', 'muitas', 'onde', 'mim', 'oi', 'ola', 'ate','com',',','.',
                    'nao','porque','❤❤❤❤❤❤❤❤❤','.',' .','. ',' . ','procos']

MORE_STOPWORDS2 = ['ja', 'q', 'd', 'ai', 'desse', 'dessa', 'disso', 'nesse', 'nessa', 'nisso', 'esse',
                               'essa', 'isso', 'so', 'mt', 'vc', 'voce', 'ne', 'ta', 'to', 'pq',
                               'cade', 'kd', 'la', 'e', 'eh', 'dai', 'pra', 'vai', 'olha', 'pois', 'fica', 'muito',
                               'muita', 'muitos', 'muitas', 'onde', 'mim', 'oi', 'ola', 'ate', 'com', ',', '.',
                               'nao', 'porque', '❤❤❤❤❤❤❤❤❤', 'adoro', 'otimo','otima', '!', '...', 'adorei', 'nota', 'perfeito',
                               'gostei',' ok','ok ',' ok ','perfeita','perfeito','recomendo','.',' .','. ','sempre','bom','achei',
                               'eficiente','rapido','boa','super','chegou','pratica','tudo','antes','monkeybiz','bom',
                                'recomendo..','bonito','feio','problemas','nota','aprovado','ser','simples','repitirei','enrosco','indico',
                                'compra..adorei','excelente','[','parabens','procos','top','prica','vendedor','otimo','otima',
                                'rapida','rapido']



#------------------Functions----------------------------------

def create_review(frase, cluster):
    review = Review()
    review.text = frase[2]
    review.cluster = cluster
    review.data = frase[1]
    review.save()