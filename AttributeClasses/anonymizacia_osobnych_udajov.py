import re
from AttributeClasses.AttributeExtractor import AttributeExtractor


class anonymizacia_osobnych_udajov(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
            if array[i] == "nar.":
                if "X" in array[i+1]:
                  return 1
                if (char.isdigit() for char in array[i+1]):
                  return 0
            i += 1
