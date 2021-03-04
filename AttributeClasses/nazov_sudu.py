from AttributeClasses.AttributeExtractor import AttributeExtractor


class nazov_sudu(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     nazov_sudu = ""
     while i < len(array):
         if array[i] == "Súd:":
             while array[i+1] != "Spisová":
                 nazov_sudu+=" "+array[i+1]
                 i += 1
             return nazov_sudu.strip()



