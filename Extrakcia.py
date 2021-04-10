#!/usr/local/bin/python
# coding: windows-1250
from AttributeClasses.Znacka import znacka
from AttributeClasses.ZaciatokKonania import zaciatok_konania
from AttributeClasses.KoniecKonania import koniec_konania
from AttributeClasses.NazovSudu import nazov_sudu
from AttributeClasses.TypSudu import typ_sudu
from AttributeClasses.AnonymizaciaOnlineIdentifikatorov import anonymizacia_online_identifikatorov
from AttributeClasses.AnonymizaciaOsobnychUdajov import anonymizacia_osobnych_udajov
from AttributeClasses.AnonymizaciaIpAdresy import anonymizacia_ip_adresy
from AttributeClasses.ListinneDokazy import listinne_dokazy
from AttributeClasses.ZnaleckeDokazovanie import znalecke_dokazovanie
from AttributeClasses.OdborneVyjadrenie import odborne_vyjadrenie
from AttributeClasses.Rozhodnutie import rozhodnutie
from AttributeClasses.CasovaPeciatka import casova_peciatka
from AttributeClasses.TypKonania import typ_konania
from AttributeClasses.VysluchSvedka import vysluch_svedka
from AttributeClasses.VysluchStrany import vysluch_strany

import mysql_connection as mysqlconnector

import numpy as np
import os
import json
from Dokument import Dokument

mycursor = mysqlconnector.mydb.cursor()

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
vysluch_svedka = vysluch_svedka()
vysluch_strany = vysluch_strany()

subory_json = []

for file in os.listdir("dataset_json"):
    if file.endswith(".json"):
        subory_json.append(file)

perf_measure = {"vysluch_strany": {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0},
                "vysluch_svedka": {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0},
                "listinne_dokazy": {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0},
                "vecne_dokazy": {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0},
                "odborne_vyjadrenie": {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0},
                "znalecke_dokazovanie": {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0},
                }

znacky_mesta = [["8C/56/2016", "Okresn� s�d Liptovsk� Mikul�"], ["1T/27/2016", "Okresn� s�d Bardejov"],
                ["6C/121/2016", "Okresn� s�d �ilina"],
                ["1T/73/2016", "Okresn� s�d Rev�ca"], ["12T/193/2016", "Okresn� s�d Vranov nad Top�ou"],
                ["3To/102/2016", "Krajsk� s�d Tren��n"],
                ["3T/41/2017", "Okresn� s�d Tren��n"], ["5T/108/2016", "Okresn� s�d Zvolen"],
                ["2T/47/2016", "Okresn� s�d Bansk� Bystrica"],
                ["1T/14/2016", "Okresn� s�d Brezno"], ["6Csp/27/2016", "Okresn� s�d �ilina"],
                ["3To/131/2016", "Krajsk� s�d Bratislava"],
                ["2T/186/2017", "Okresn� s�d Bardejov"], ["1T/115/2017", "Okresn� s�d Bratislava II"],
                ["3T/130/2017", "Okresn� s�d Bratislava II"],
                ["2T/47/2016", "Okresn� s�d Bratislava IV"], ["3T/34/2017", "Okresn� s�d Bratislava III"],
                ["4T/176/2017", "Okresn� s�d Zvolen"],
                ["5T/143/2017", "Okresn� s�d Ko�ice okolie"], ["2To/7/2017", "Krajsk� s�d Pre�ov"],
                ["1T/108/2017", "Okresn� s�d Martin"],
                ["6T/119/2017", "Okresn� s�d N�mestovo"], ["3T/14/2018", "Okresn� s�d Malacky"],
                ["6To/99/2017", "Krajsk� s�d Trnava"],
                ["4To/14/2018", "Krajsk� s�d Ko�ice"], ["4C/22/2017", "Okresn� s�d Vranov nad Top�ou"],
                ["1Co/25/2018", "Krajsk� s�d Pre�ov"],
                ["2T/37/2016", "Okresn� s�d Rimavsk�"], ["1T/31/2017", "Okresn� s�d Galanta"],
                ["1T/128/2016", "Okresn� s�d Galanta"],
                ["33T/59/2018", "Okresn� s�d Nitra"], ["3T/55/2018", "Okresn� s�d Bratislava III"],
                ["3T/67/2018", "Okresn� s�d Michalovce"],
                ["6Csp/26/2016", "Okresn� s�d �ilina"], ["3T/25/2018", "Okresn� s�d Bansk� Bystrica"],
                ["41T/95/2017", "Okresn� s�d Pre�ov"],
                ["6To/34/2018", "Krajsk� s�d Pre�ov"], ["8T/32/2017", "Okresn� s�d Pie��any"],
                ["1T/66/2017", "Okresn� s�d Trnava"],
                ["7Csp/161/2017", "Okresn� s�d Rev�ca"], ["6T/75/2018", "Okresn� s�d N�mestovo"],
                ["1T/17/2017", "Okresn� s�d Ru�omberok"],
                ["13C/71/2016", "Okresn� s�d Ko�ice II"], ["5T/47/2016", "Okresn� s�d Zvolen"],
                ["6To/58/2018", "Krajsk� s�d Ko�ice"],
                ["8T/23/2018", "Okresn� s�d Ru�omberok"], ["8T/4/2018", "Okresn� s�d Star� �ubov�a"],
                ["4T/69/2018", "Okresn� s�d Ko�ice II"],
                ["2T/41/2017", "Okresn� s�d �iar nad Hronom"], ["2T/108/2017", "Okresn� s�d Lu�enec"],
                ["4To/73/2018", "Krajsk� s�d Bansk� Bystrica"],
                ["5To/122/2018", "Krajsk� s�d Bansk� Bystrica"], ["4T/77/2018", "Okresn� s�d Michalovce"],
                ["3T/50/2018", "Okresn� s�d Pre�ov"],
                ["4T/72/2016", "Okresn� s�d Pre�ov"], ["3T/96/2018", "Okresn� s�d Prievidza"],
                ["33T/83/2018", "Okresn� s�d Pre�ov"],
                ["33T/69/2018", "Okresn� s�d Nitra"], ["3T/65/2018", "Okresn� s�d Bratislava IV"],
                ["6Nt/1/2018", "Okresn� s�d Poprad"],
                ["9Tos/35/2018", "Krajsk� s�d Pre�ov"], ["3T/127/2017", "Okresn� s�d Lu�enec"],
                ["3T/153/2017", "Okresn� s�d Prievidza"],
                ["3T/81/2017", "Okresn� s�d Bratislava"], ["2T/21/2019", "Okresn� s�d Bardejov"],
                ["2T/27/2018", "Okresn� s�d Lu�enec"],
                ["2T/12/2018", "Okresn� s�d Lu�enec"], ["6T/71/2018", "Okresn� s�d Bratislava II"],
                ["1T/14/2019", "Okresn� s�d Tren��n"]]

atributy = ["subor", "znacka", "nazov_sudu", "zaciatok_konania", "koniec_konania", "typ_sudu", "typ_konania",
            "casova_peciatka", "pridelenie_ip", "specifikacia_zariadenia",
            "vztah_osoby_a_zariadenia", "anonymizacia_ip_adresy", "anonymizacia_osobnych_udajov",
            "anonymizacia_online_identifikatorov",
            "vysluch_strany", "vysluch_svedka", "listinne_dokazy", "vecne_dokazy", "odborne_vyjadrenie",
            "znalecke_dokazovanie", "rozhodnutie"]

extraction_success = {}
attribute_dictionary = {}

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


def NajdiRozhodnutie(list):
    for file in os.listdir("C:/Users/Adri�n Rrojek/Desktop/Bakalarka/jsons/"):
        a_file = open("C:/Users/Adri�n Rrojek/Desktop/Bakalarka/jsons/" + file, "r", encoding='utf-8')
        json_object = json.load(a_file)
        for x in range(len(json_object["data"])):
            json_rozhodnutie = json_object["data"][x]
            for y in znacky_mesta:
                if json_rozhodnutie["spisova_znacka"] == y[0] and json_rozhodnutie["sud_nazov"] == y[1]:
                    a_file.close()
                    novy_fulltext = ""
                    for line in json_rozhodnutie["dokument_fulltext"].splitlines():
                        novy_fulltext = novy_fulltext + line + "\n"
                    json_rozhodnutie["dokument_fulltext"] = novy_fulltext
                    mycursor.execute(
                        "select subor from data where znacka='" + json_rozhodnutie["spisova_znacka"] + "'")
                    myresult = mycursor.fetchall()
                    subor = np.asarray(myresult[0])
                    novy_json = open("dataset_json/" + subor[0] + ".json", "w", encoding='utf-8')
                    json.dump(json_rozhodnutie, novy_json, ensure_ascii=False)
                    novy_json.close()
                    znacky_mesta.remove(y)
            x = x + 1


def Extrakcia(subor):
    pocitadloPrePerf = 14
    dokument = Dokument(subor)
    chybne = list()
    attribute_dictionary["subor"] = subor[: - 5]
    attribute_dictionary["znacka"] = znacka.extrahuj_json(dokument)
    attribute_dictionary["nazov_sudu"] = nazov_sudu.extrahuj_json(dokument)
    attribute_dictionary["zaciatok_konania"] = zaciatok_konania.extrahuj_json(dokument)
    attribute_dictionary["koniec_konania"] = koniec_konania.extrahuj_json(dokument)
    attribute_dictionary["typ_sudu"] = typ_sudu.extrahuj_json(dokument)
    attribute_dictionary["typ_konania"] = typ_konania.extrahuj_json(dokument)
    attribute_dictionary["casova_peciatka"] = ""
    attribute_dictionary["pridelenie_ip"] = ""
    attribute_dictionary["specifikacia_zariadenia"] = ""
    attribute_dictionary["vztah_osoby_a_zariadenia"] = ""
    attribute_dictionary["anonymizacia_ip_adresy"] = ""
    attribute_dictionary["anonymizacia_osobnych_udajov"] = ""
    attribute_dictionary["anonymizacia_online_identifikatorov"] = ""
    attribute_dictionary["vysluch_strany"] = vysluch_strany.extrahuj_json(dokument)
    attribute_dictionary["vysluch_svedka"] = vysluch_svedka.extrahuj_json(dokument)
    attribute_dictionary["listinne_dokazy"] = listinne_dokazy.extrahuj_json(dokument)
    attribute_dictionary["vecne_dokazy"] = ""
    attribute_dictionary["odborne_vyjadrenie"] = odborne_vyjadrenie.extrahuj_json(dokument)
    attribute_dictionary["znalecke_dokazovanie"] = znalecke_dokazovanie.extrahuj_json(dokument)
    attribute_dictionary["rozhodnutie"] = ""
    print("Vystup: ")
    print(attribute_dictionary)
    kontrola = Kontrola(chybne)
    Vykonnost(kontrola, pocitadloPrePerf)


def Kontrola(pole):
    mycursor.execute("SELECT * FROM data where subor='" + attribute_dictionary["subor"] + "'")
    myresult = mycursor.fetchall()
    kontrola = np.asarray(myresult[0])
    print("Kontrola:")
    print(kontrola)
    pocitadloPrePole = 0
    for x in attribute_dictionary:
        if str(attribute_dictionary[x]) == kontrola[pocitadloPrePole]:
            extraction_success[x] = extraction_success[x] + 1
        else:
            pole.append(x)
        pocitadloPrePole = pocitadloPrePole + 1
    print("Nespr�vne:")
    print(pole)
    print("________________________________________")
    return kontrola


def Vykonnost(pole, pocitadlo):
    for d in perf_measure:
        if attribute_dictionary[d] == 1 and pole[pocitadlo] == "1":
            perf_measure[d]['TP'] += 1
        if attribute_dictionary[d] == 0 and pole[pocitadlo] == "0":
            perf_measure[d]['TN'] += 1
        if attribute_dictionary[d] == 1 and pole[pocitadlo] == "0":
            perf_measure[d]['FP'] += 1
        if attribute_dictionary[d] == 0 and pole[pocitadlo] == "1":
            perf_measure[d]['FN'] += 1
        pocitadlo += 1


def UspesnostAtributov():
    for x in extraction_success:
        hodnota = extraction_success[x]
        extraction_success[x] = str(hodnota / len(subory_json) * 100) + "%"
    print(extraction_success)
