import re
from AttributeClasses.AttributeExtractor import AttributeExtractor


class anonymizacia_online_identifikatorov(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
            if array[i] == "a@b.c":
                return 1
            elif array[i] == "Menom" or "menom" or "Nickom" or "nickom" and array[i+1]=="W.":
                return 1
            else:
                return 0
            i += 1

    def extrahuj_json(self, Dokument):
        array = Dokument.naSlova_json()
        i = 0
        while i < len(array):
            if array[i] == "a@b":
                return 1
            elif array[i] == "Menom" or "menom" or "Nickom" or "nickom" and array[i + 1] == "W.":
                return 1
            else:
                return 0
            i += 1