#!/usr/local/bin/python
# coding: windows-1250

from AttributeClasses.BooleanExtractor import  najdiTop
from Extrakcia import Extrakcia, subory_json, UspesnostAtributov


def main(atribut,n):
    #Tato metoda extrahuje volnotextove atributy(n znamena kolko slov s najvacsim rozdielom zoberieme, ak je n 5 tak najde top 5 slov alebo ngramov z ktorych vytvori klasifikator)
   najdiTop(atribut,n)

   #Tieto riadky extrahuju hlavickve atributy
   #for x in subory_json:
    #    Extrakcia(x)
   #UspesnostAtributov()


main("listinne_dokazy",5)

