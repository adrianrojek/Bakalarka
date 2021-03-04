from AttributeClasses.AttributeExtractor import AttributeExtractor


class typ_sudu(AttributeExtractor):
    def __init__(self):
        pass

    def extrahuj(self, Dokument):
     array = Dokument.hlavicka()
     i = 0
     while i < len(array):
         if array[i] == "Súd:":
             if array[i+1] == "Okresný":
                 return("the first instance")
             if array[i+1] == "Krajský":
                 return("the second instance")