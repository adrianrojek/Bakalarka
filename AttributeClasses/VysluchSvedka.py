#!/usr/local/bin/python
# coding: windows-1250
from Tvaroslovnik import get_lemma
from AttributeClasses.AttributeExtractor import AttributeExtractor

class vysluch_svedka(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
        pass

    def extrahuj_json(self, Dokument):
        array = Dokument.naSlova_json()
        prvePole = ["výsluch", "výpoveď"]
        druhePole = ["svedok", "svedkyňa"]
        for x, _ in enumerate(array):
            if x != len(array) - 1:
                prve = array[x]
                druhe = array[x + 1]
                if get_lemma(str(prve)) in prvePole and get_lemma(str(druhe)) in druhePole:
                    return 1

        return 0