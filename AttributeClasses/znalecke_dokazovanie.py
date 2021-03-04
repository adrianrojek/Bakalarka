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
         if array[i] != "znaleckého" or "znaleckým" or "Znalecký" or "znalecký" or "znalec" or "Znalec" or "znalecké" or "Znalecké":
             return 0
         else: return 1
         i += 1
