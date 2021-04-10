#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor
from Tvaroslovnik import get_lemma

class znalecke_dokazovanie(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] != "znaleck�ho" or "znaleck�m" or "Znaleck�" or "znaleck�" or "znalec" or "Znalec" or "znaleck�" or "Znaleck�":
             return 0
         else: return 1
         i += 1

    def extrahuj_json(self, Dokument):
        array = Dokument.naSlova_json()
        prvePole = ["znaleck�", "znaleck�","sk�manie"]
        druhePole = ["sk�manie", "posudok","znalec","dokazovanie"]
        for x, _ in enumerate(array):
            if x != len(array) - 1:
                prve = array[x]
                druhe = array[x + 1]
                if get_lemma(str(prve)) in prvePole and get_lemma(str(druhe)) in druhePole:
                    return 1

        return 0

