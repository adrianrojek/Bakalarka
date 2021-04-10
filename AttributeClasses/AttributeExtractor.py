from abc import ABC, abstractmethod

class AttributeExtractor(ABC):

   @abstractmethod
   def extrahuj_txt(self, Dokument):
      return

   @abstractmethod
   def extrahuj_json(self, Dokument):
      return
