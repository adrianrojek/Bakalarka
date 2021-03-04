#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class anonymizacia_ip_adresy(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "znaleckého" or array[i] == "znaleckým":
             return 1
         else: return 0


         i += 1