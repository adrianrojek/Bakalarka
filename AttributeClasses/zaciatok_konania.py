from AttributeClasses.AttributeExtractor import AttributeExtractor


class zaciatok_konania(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "značka:":
             znacka = array[i+1]
             return znacka[-4:]
         i += 1