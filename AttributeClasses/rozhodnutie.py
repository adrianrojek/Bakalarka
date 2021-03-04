#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class rozhodnutie(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "rozhodol:":
             while array[i+2] != "odôvodnenie:" or "Odôvodnenie:":
                 if array[i+1] == "vinný," or "vinnú" or "vinného":
                     return ("vinný")
                 else:
                     return ("zatiaľ neznáme")
                 i += 1
         i += 1