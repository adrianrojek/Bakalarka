#!/usr/local/bin/python
# coding: windows-1250
import AttributeClasses.typ_konania as typ_konania
from AttributeClasses.znacka import znacka
from AttributeClasses.zaciatok_konania import zaciatok_konania
from AttributeClasses.koniec_konania import koniec_konania
from AttributeClasses.nazov_sudu import nazov_sudu
from AttributeClasses.typ_sudu import typ_sudu
from AttributeClasses.anonymizacia_online_identifikatorov import anonymizacia_online_identifikatorov
from AttributeClasses.anonymizacia_osobnych_udajov import anonymizacia_osobnych_udajov
from AttributeClasses.anonymizacia_ip_adresy import anonymizacia_ip_adresy
from AttributeClasses.listinne_dokazy import listinne_dokazy
from AttributeClasses.znalecke_dokazovanie import znalecke_dokazovanie
from AttributeClasses.odborne_vyjadrenie import odborne_vyjadrenie
from AttributeClasses.rozhodnutie import rozhodnutie
from AttributeClasses.casova_peciatka import casova_peciatka
from AttributeClasses.typ_konania import typ_konania


import mysql_connection as mysqlconnector

import numpy as np
import os

import pandas as pd

from Dokument import Dokument

znacka = znacka()
nazov_sudu = nazov_sudu()
zaciatok_konania = zaciatok_konania()
koniec_konania = koniec_konania()
typ_sudu = typ_sudu()
typ_konania = typ_konania()
casova_peciatka = casova_peciatka()
anonymizacia_ip_adresy = anonymizacia_ip_adresy()
anonymizacia_osobnych_udajov = anonymizacia_osobnych_udajov()
anonymizacia_online_identifikatorov = anonymizacia_online_identifikatorov()
listinne_dokazy = listinne_dokazy()
odborne_vyjadrenie = odborne_vyjadrenie()
znalecke_dokazovanie = znalecke_dokazovanie()
rozhodnutie = rozhodnutie()



mycursor = mysqlconnector.mydb.cursor()

subory = []

for file in os.listdir("C:/Users/Adrián Rrojek/PycharmProjects/Bakalarka/dataset"):
    if file.endswith(".txt"):
        subory.append(file)

print(subory)
print("_____________________________________________________________________________________________________________________________________________________________________")

dvojrozmerne_pole = []

attribute_dictionary = {}
extraction_success = {}

extraction_success["subor"] = 0
extraction_success["znacka"] = 0
extraction_success["nazov_sudu"] = 0
extraction_success["zaciatok_konania"] = 0
extraction_success["koniec_konania"] = 0
extraction_success["typ_sudu"] = 0
extraction_success["typ_konania"] = 0
extraction_success["casova_peciatka"] = 0
extraction_success["pridelenie_ip"] = 0
extraction_success["specifikacia_zariadenia"] = 0
extraction_success["vztah_osoby_a_zariadenia"] = 0
extraction_success["anonymizacia_ip_adresy"] = 0
extraction_success["anonymizacia_osobnych_udajov"] = 0
extraction_success["anonymizacia_online_identifikatorov"] = 0
extraction_success["vysluch_strany"] = 0
extraction_success["vysluch_svedka"] = 0
extraction_success["listinne_dokazy"] = 0
extraction_success["vecne_dokazy"] = 0
extraction_success["odborne_vyjadrenie"] = 0
extraction_success["znalecke_dokazovanie"] = 0
extraction_success["rozhodnutie"] = 0


def test_extraction(subor):
    dokument = Dokument(subor)
    uspesnost = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    attribute_dictionary["subor"] = subory[pocitadlo][: - 4]
    attribute_dictionary["znacka"] = znacka.extrahuj(dokument)
    attribute_dictionary["nazov_sudu"] = nazov_sudu.extrahuj(dokument)
    attribute_dictionary["zaciatok_konania"] = zaciatok_konania.extrahuj(dokument)
    attribute_dictionary["koniec_konania"] = koniec_konania.extrahuj(dokument)
    attribute_dictionary["typ_sudu"] = typ_sudu.extrahuj(dokument)
    attribute_dictionary["typ_konania"] = typ_konania.extrahuj(dokument)
    attribute_dictionary["casova_peciatka"] = casova_peciatka.extrahuj(dokument)
    attribute_dictionary["pridelenie_ip"] = ""
    attribute_dictionary["specifikacia_zariadenia"] = ""
    attribute_dictionary["vztah_osoby_a_zariadenia"] = ""
    attribute_dictionary["anonymizacia_ip_adresy"] = anonymizacia_ip_adresy.extrahuj(dokument)
    attribute_dictionary["anonymizacia_osobnych_udajov"] = anonymizacia_osobnych_udajov.extrahuj(dokument)
    attribute_dictionary["anonymizacia_online_identifikatorov"] = anonymizacia_online_identifikatorov.extrahuj(dokument)
    attribute_dictionary["vysluch_strany"] = ""
    attribute_dictionary["vysluch_svedka"] = ""
    attribute_dictionary["listinne_dokazy"] = listinne_dokazy.extrahuj(dokument)
    attribute_dictionary["vecne_dokazy"] = ""
    attribute_dictionary["odborne_vyjadrenie"] = odborne_vyjadrenie.extrahuj(dokument)
    attribute_dictionary["znalecke_dokazovanie"] = znalecke_dokazovanie.extrahuj(dokument)
    attribute_dictionary["rozhodnutie"] = rozhodnutie.extrahuj(dokument)


    print("Vystup: ")
    print(attribute_dictionary)
    mycursor.execute("SELECT * FROM test where subor='" + attribute_dictionary["subor"] + "'")
    myresult = mycursor.fetchall()
    kontrola = np.asarray(myresult[0])
    print("Kontrola: ")
    print(kontrola)
    pocetUspesnych = 0
    pocitadloPrePole = 0
    for x in attribute_dictionary:
        if str(attribute_dictionary[x]) == kontrola[pocitadloPrePole]:
            extraction_success[x] = extraction_success[x] + 1
        pocitadloPrePole = pocitadloPrePole + 1
    print(
        "_____________________________________________________________________________________________________________________________________________________________________")
    df = pd.DataFrame(attribute_dictionary,
                      columns=["Súbor", "Spisová značka", "Názov súdu", "Rok začatia", "Rok ukončenia", "Typ súdu",
                               "Typ konania", "Časová pečiatka", "Pridelenie IP", "Špecifikácia zariadenia",
                               "Vzťah osoby a zariadenia", "Anonymizácia IP adresy", "Anonymizácia osobných údajov",
                               "Anonymizácia online identifikátorov", "Výsluch strany", "Výsluch svedka",
                               "Listinné dôkazy", "Vecné dôkazy", "Odborné vyjadrenie", "Znalecké dokazovanie",
                               "Rozhodnutie"]).T
    df.to_excel(excel_writer="C:/Users/Adrián Rrojek/Desktop/test.xlsx")
    attribute_dictionary.clear()

def test_extraction(subor):
    dokument = Dokument(subor)
    uspesnost = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    attribute_dictionary["subor"] = subory[pocitadlo][: - 4]
    attribute_dictionary["znacka"] = znacka.extrahuj(dokument)
    attribute_dictionary["nazov_sudu"] = nazov_sudu.extrahuj(dokument)
    attribute_dictionary["zaciatok_konania"] = zaciatok_konania.extrahuj(dokument)
    attribute_dictionary["koniec_konania"] = koniec_konania.extrahuj(dokument)
    attribute_dictionary["typ_sudu"] = typ_sudu.extrahuj(dokument)
    attribute_dictionary["typ_konania"] = typ_konania.extrahuj(dokument)
    attribute_dictionary["casova_peciatka"] = casova_peciatka.extrahuj(dokument)
    attribute_dictionary["pridelenie_ip"] = ""
    attribute_dictionary["specifikacia_zariadenia"] = ""
    attribute_dictionary["vztah_osoby_a_zariadenia"] = ""
    attribute_dictionary["anonymizacia_ip_adresy"] = anonymizacia_ip_adresy.extrahuj(dokument)
    attribute_dictionary["anonymizacia_osobnych_udajov"] = anonymizacia_osobnych_udajov.extrahuj(dokument)
    attribute_dictionary["anonymizacia_online_identifikatorov"] = anonymizacia_online_identifikatorov.extrahuj(dokument)
    attribute_dictionary["vysluch_strany"] = ""
    attribute_dictionary["vysluch_svedka"] = ""
    attribute_dictionary["listinne_dokazy"] = listinne_dokazy.extrahuj(dokument)
    attribute_dictionary["vecne_dokazy"] = ""
    attribute_dictionary["odborne_vyjadrenie"] = odborne_vyjadrenie.extrahuj(dokument)
    attribute_dictionary["znalecke_dokazovanie"] = znalecke_dokazovanie.extrahuj(dokument)
    attribute_dictionary["rozhodnutie"] = rozhodnutie.extrahuj(dokument)


    print("Vystup: ")
    print(attribute_dictionary)
    mycursor.execute("SELECT * FROM test where subor='" + attribute_dictionary["subor"] + "'")
    myresult = mycursor.fetchall()
    kontrola = np.asarray(myresult[0])
    print("Kontrola: ")
    print(*kontrola, sep=', ')
    pocetUspesnych = 0
    pocitadloPrePole = 0
    for x in attribute_dictionary:
        if str(attribute_dictionary[x]) == kontrola[pocitadloPrePole]:
            extraction_success[x] = extraction_success[x] + 1
        pocitadloPrePole = pocitadloPrePole + 1
    print(
        "_____________________________________________________________________________________________________________________________________________________________________")
    df = pd.DataFrame(attribute_dictionary,
                      columns=["Súbor", "Spisová značka", "Názov súdu", "Rok začatia", "Rok ukončenia", "Typ súdu",
                               "Typ konania", "Časová pečiatka", "Pridelenie IP", "Špecifikácia zariadenia",
                               "Vzťah osoby a zariadenia", "Anonymizácia IP adresy", "Anonymizácia osobných údajov",
                               "Anonymizácia online identifikátorov", "Výsluch strany", "Výsluch svedka",
                               "Listinné dôkazy", "Vecné dôkazy", "Odborné vyjadrenie", "Znalecké dokazovanie",
                               "Rozhodnutie"]).T
    df.to_excel(excel_writer="C:/Users/Adrián Rrojek/Desktop/test.xlsx")
    attribute_dictionary.clear()

pocitadlo=0

for x in subory:
    test_extraction(x)
    pocitadlo+=1
for x in extraction_success:
    extraction_success[x]= str((extraction_success[x]) / len(subory)*100 )+"%"
print(extraction_success)






