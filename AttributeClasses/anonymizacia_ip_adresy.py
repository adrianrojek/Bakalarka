import re

from AttributeClasses.AttributeExtractor import AttributeExtractor


class anonymizacia_ip_adresy(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array=Dokument.naSlova()
     i = 0
     while i < len(array):
            if array[i] == "IP":
                if "XX" in array[i+2]:
                  return 1
                if (char.isdigit() for char in array[i+2]):
                  return 0
            i += 1
