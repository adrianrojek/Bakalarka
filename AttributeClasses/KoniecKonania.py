#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class koniec_konania(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
        array = Dokument.naSlova()
        i = 0
        while i < len(array):
            if array[i] == "rozhodnutia:":
                if len(array[i + 3]) == 4:
                    return array[i + 3]
                else:
                    return array[i + 1][-4:]
            i += 1

    def extrahuj_json(self, Dokument):
        array = Dokument.naSlova_json()
        i = 0
        while i < len(array):
            if array[i] == "Dátum" and array[i + 1] == "vydania" and array[i + 2] == "rozhodnutia":
                return array[i + 5]
            i += 1
        return
