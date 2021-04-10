from AttributeClasses.AttributeExtractor import AttributeExtractor

class znacka(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     while i < len(array):
         if array[i] == "značka:":
             return array[i+1]
         i += 1

    def extrahuj_json(self, Dokument):
        json_objekt=Dokument.vytvorJsonObjekt()
        return json_objekt["spisova_znacka"]
