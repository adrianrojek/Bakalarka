#!/usr/local/bin/python
# coding: windows-1250
import numpy as np
import re
import json

class Dokument:
    def __init__(self, subor):
        self.subor = subor

    def vytvorJsonObjekt(self):
        file = open("dataset_json/" + self.subor,encoding='utf-8')
        objekt = json.load(file)
        return objekt

    def naSlova_txt(self):
        subor = open("dataset_txt/" + self.subor, encoding="cp1250")
        slova = list()
        for line in subor:
            array_line = np.asarray(line.split())
            i = 0
            for x in array_line:
                if len(x.strip()) != 0:
                    slova.append(x.strip())
                i = i + 1

        array = np.asarray(slova)
        return array

    def hlavicka_txt(self):
        subor = open("dataset_txt/" + self.subor, encoding="cp1250")
        slova = list()
        for line in subor:
            array_line = np.asarray(line.split())
            i = 0
            for x in array_line:
                if len(x.strip()) != 0:
                    slova.append(x.strip())
                i = i + 1
            if "ECLI:" in line:
                break

        array = np.asarray(slova)
        return array

    def naVety(self):
        pass

    def naSlova_json(self):
        subor = open("dataset_json/"+self.subor, encoding='utf-8')
        json_objekt=json.load(subor)
        fulltext=json_objekt["dokument_fulltext"]
        slova = list()
        pole =(re.split('[, . \n " -  :]', fulltext))
        for x in pole:
            if x != '':
                slova.append(x.strip())
        array = np.asarray(slova)
        return array

