#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class znalecke_dokazovanie(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] != "znaleck�ho" or "znaleck�m" or "Znaleck�" or "znaleck�" or "znalec" or "Znalec" or "znaleck�" or "Znaleck�":
             return 0
         else: return 1
         i += 1
