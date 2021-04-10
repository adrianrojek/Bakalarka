from AttributeClasses.AttributeExtractor import AttributeExtractor

class typ_konania(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     while i < len(array):
         if array[i] == "značka:":
             if "T" in array[i+1]:
                 return ("Trestné")
             if "C" in array[i + 1]:
                 return ("Občianske")
         i += 1
     return ("Iné")

    def extrahuj_json(self, Dokument):
        json_objekt = Dokument.vytvorJsonObjekt()
        if "T" in json_objekt["spisova_znacka"]:
            return ("Trestné")
        if "C" in json_objekt["spisova_znacka"]:
            return ("Občianske")
        else:
            return ("Iné")
