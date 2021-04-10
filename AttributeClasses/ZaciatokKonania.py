from AttributeClasses.AttributeExtractor import AttributeExtractor


class zaciatok_konania(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova()
     i = 0
     while i < len(array):
         if array[i] == "značka:":
             znacka = array[i+1]
             return znacka[-4:]
         i += 1

    def extrahuj_json(self, Dokument):
        json_objekt = Dokument.vytvorJsonObjekt()
        return json_objekt["spisova_znacka"][-4:]
