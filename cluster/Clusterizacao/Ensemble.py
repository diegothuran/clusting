# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from summa import summarizer
import spellchecker
from DBSCAN import Dbscan
from PreProcessamento import PreProcesso
from ExtracaoSujeito import ExtracaoSujeito
reload(sys)
sys.setdefaultencoding('utf-8')

class Ensemble():
    def __init__(self):
        self.preProc = PreProcesso()
        self.dbscan = Dbscan()
        self.extrator = ExtracaoSujeito()
        self.not_temas = ['d', '.', 'ok', '10', 'on', 'NO SUGGESTION', 'gr', 'procos', 'siti', 'prica', 'ito']
        self.spell = spellchecker
    '''
    def buscar(self):
        reviews =[]
        dataPath = 'cluster/Clusterizacao/teste11.csv'
        p = PreProcesso()
        with open(dataPath, 'rb') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    if row[1] != "":
                        frase = p.prePorcessar(row[0])
                        reviews.append((frase, row[1], row[0]))
        print('=========== DONE =============================')
        return reviews
    '''
    def limpezaDados(self, coments):
        p = PreProcesso()
        reviews = [(p.prePorcessar(coment[0]), coment[1], coment[0]) for coment in coments]
        return reviews

    def clusterizar(self, coments):
        #reviews = self.buscar()
        reviews = self.limpezaDados(coments)

        clusters_bruto = self.dbscan.dbScan(reviews, 0.4, 5)
        
        topicos = []
        for cluster in clusters_bruto:
            comentario = ''
            for frase in cluster:
                comentario += frase[2] + " "

            topicos.append(comentario)

        # Juntando Cluster que possuem mesmo tema

        temas = []
        clusters = []
        indice = 0
        for frase in topicos:
            try:
                tema = self.spell.correct(self.extrator.extrair(summarizer.summarize(frase,
                                                                                     words=20, language='portuguese')))
                if tema not in temas:
                    indice = indice+1
                    temas.append(tema)
                    clusters.append(frase)

                else:
                    ind = temas.index(tema)
                    novo = clusters_bruto[indice]
                    cluster = clusters[ind]
                    clusters_bruto[ind].extend(novo)
                    clusters[ind] = cluster + " " + frase
                    indice = indice+1

            except:
                indice = indice+1

        # IDENTIFICAÇÂO DE TEMA FINAL

        temas = [self.spell.correct(self.extrator.extrair(summarizer.summarize(
            frase, words=20, language='portuguese'))) for frase in clusters]

        temas = list(set(temas))
        temas_final = []
        
        for tema in temas:
            if tema not in self.not_temas:
                #print(tema)
                temas_final.append(tema)

        return temas_final, clusters_bruto