from AttributeClasses.AttributeExtractor import AttributeExtractor


class typ_sudu(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     while i < len(array):
         if array[i] == "Súd:":
             if array[i+1] == "Okresný":
                 return("the first instance")
             if array[i+1] == "Krajský":
                 return("the second instance")

    def extrahuj_json(self, Dokument):
        json_objekt = Dokument.vytvorJsonObjekt()
        nazov=json_objekt["sud_nazov"]
        pole=nazov.split()
        if pole[0] == "Okresný":
            return ("the first instance")
        if pole[0] == "Krajský":
            return ("the second instance")
        else:
            return("Iný")
