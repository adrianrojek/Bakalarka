#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class rozhodnutie(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "rozhodol:":
             while array[i+2] != "od�vodnenie:" or "Od�vodnenie:":
                 if array[i+1] == "vinn�," or "vinn�" or "vinn�ho":
                     return ("vinn�")
                 else:
                     return ("zatia� nezn�me")
                 i += 1
         i += 1

    def extrahuj_json(self, Dokument):
        return