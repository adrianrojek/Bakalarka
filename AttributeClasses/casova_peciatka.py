#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.AttributeExtractor import AttributeExtractor


class casova_peciatka(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] != "nezistenom" and array[i+1] == "�ase:" or "�ase":
             return 0
         if array[i] == "�ase:" or "�ase":
             if (char.isdigit() for char in array[i + 1]):
                 return 1
             else: return 0
         i += 1