from AttributeClasses.AttributeExtractor import AttributeExtractor


class nazov_sudu(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj_txt(self, Dokument):
     array = Dokument.naSlova_txt()
     i = 0
     nazov_sudu = ""
     while i < len(array):
         if array[i] == "Súd:":
             while array[i+1] != "Spisová":
                 nazov_sudu+=" "+array[i+1]
                 i += 1
             return nazov_sudu.strip()

    def extrahuj_json(self, Dokument):
        json_objekt = Dokument.vytvorJsonObjekt()
        return json_objekt["sud_nazov"].strip()



