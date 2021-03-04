from AttributeClasses.AttributeExtractor import AttributeExtractor


class koniec_konania(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "rozhodnutia:":
             if len(array[i+3]) == 4:
                 return array[i+3]
             else:
                return array[i+1][-4:]
         i += 1