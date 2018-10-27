# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from datetime import datetime
import math
reload(sys)
sys.setdefaultencoding('utf-8')

class Dbscan(object):
    def __init__(self):
        self.EPS = 0
        self.EPSCONT = 0
        self.MINPTS = 0
        self.MINPTSCONT = 0

    #Função Responsável por realizar clacula de similaridade
    def fadingDistance(self,fraseA, fraseB):
        FMT = "%Y-%m-%d %H:%M:%S"

        if datetime.strptime(fraseA[1], FMT) > datetime.strptime(fraseB[1], FMT):
            tdelta = datetime.strptime(fraseA[1], FMT) - datetime.strptime(fraseB[1], FMT)
        else:
            tdelta = datetime.strptime(fraseB[1], FMT) - datetime.strptime(fraseA[1], FMT)

        timeDifference = tdelta.seconds / 60.0 / 60

        words1 = set(fraseA[0].split())
        words2 = set(fraseB[0].split())

        duplicates = words1.intersection(words2)
        uniques = words1.union(words2.difference(words1))

        try:
            simi = float(len(duplicates)) / (len(uniques) * math.exp(timeDifference))
            self.EPS = self.EPS + simi
            self.EPSCONT = self.EPSCONT + 1
            return simi
        except:
            return 0.0

    #Função responsável por identificar pontos vizinhos
    def neighborhood (self,fraseA, reviews, eps):
        neighborPts = []
        for fraseB in reviews:
            distance = self.fadingDistance(fraseA,fraseB)
            if distance >= eps:
                neighborPts.append(fraseB)
        return neighborPts

    #Algoritmo DBSCAN
    def dbScan(self,reviews, eps, minPts):
        clusters = []
        visitados = []
        noise = []
        for frase in reviews:
            if frase not in visitados:

                visitados.append(frase)
                neighbours = self.neighborhood(frase, reviews, eps)

                if len(neighbours) >= minPts:
                    for fraseB in neighbours:

                        if fraseB not in visitados:
                            visitados.append(fraseB)
                            neighboursB = self.neighborhood(fraseB, reviews, eps)

                            if len(neighboursB) >= minPts:
                                neighbours.extend(neighboursB)
                    print("Cluster")
                    clusters.append(neighbours)
                else:
                    noise.append(frase)
        clusters.append(noise)
        return clusters
