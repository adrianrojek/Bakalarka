from AttributeClasses.AttributeExtractor import AttributeExtractor

class typ_konania(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     while i < len(array):
         if array[i] == "značka:":
             if "T" in array[i+1]:
                 return ("Trestné")
             if "C" in array[i + 1]:
                 return ("Občianske")
         i += 1