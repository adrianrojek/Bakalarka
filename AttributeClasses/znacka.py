from AttributeClasses.AttributeExtractor import AttributeExtractor

class znacka(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     while i < len(array):
         if array[i] == "značka:":
             return array[i+1]
         i += 1