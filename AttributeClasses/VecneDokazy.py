#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class anonymizacia_ip_adresy(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "znaleck�ho" or array[i] == "znaleck�m":
             return 1
         else: return 0


         i += 1

    def extrahuj_json(self, Dokument):
        return