#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor
from Tvaroslovnik import get_lemma

class odborne_vyjadrenie(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if "odborn�" in array:
             return 1
         else:
             return 0


         i += 1

    def extrahuj_json(self, Dokument):
        array = Dokument.naSlova_json()
        prvePole = ["odborn�", "vyjadrenie"]
        druhePole = ["konzultant", "vyjadrenie","odborn�"]
        for x, _ in enumerate(array):
            if x != len(array) - 1:
                prve = array[x]
                druhe = array[x + 1]
                if get_lemma(str(prve)) in prvePole and get_lemma(str(druhe)) in druhePole:
                    return 1
        return 0
