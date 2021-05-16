# coding: windows-1250
import json
import os
import operator

import numpy as np

import mysql_connection as db

connection = db.open_connection()
mycursor = connection.cursor()

def slova(atribut, hodnota):
    subory = []
    for file in os.listdir("dataset_lemmatized"):
        if file.endswith(".json"):
            subory.append(file)

    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = " + str(hodnota) + ""
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    rozhodnutia = []
    for x in pole:
        if str(x)[2:][: - 2] + ".json" in subory:
            rozhodnutia.append(str(x)[2:][: - 2] + ".json")
    slova = {}
    vyskyt = {}
    normovane_slova = {}
    normovane_vyskyt = {}
    for p in rozhodnutia:
        slovaVRozhodnuti = []
        a_file = open("dataset_lemmatized/" + str(p), "r", encoding='utf-8')
        json_object = json.load(a_file)
        array = json_object["dokument_fulltext"]
        for x in array:
            if len(x) > 2:
                if x in slova:
                    slova[x] += 1
                    if x not in slovaVRozhodnuti:
                        slovaVRozhodnuti.append(x)
                else:
                    slova[x] = 1
        for y in slovaVRozhodnuti:
            if y in vyskyt:
                vyskyt[y] += 1
            else:
                vyskyt[y] = 1
    sorted_slova = dict(sorted(slova.items(), key=operator.itemgetter(1), reverse=True))
    sorted_vyskyt = dict(sorted(vyskyt.items(), key=operator.itemgetter(1), reverse=True))

    for x in sorted_vyskyt:
        # podiel = sorted_vyskyt[x] / len(pole)
        # if podiel > 0.5:
        normovane_vyskyt[x] = 100 * (sorted_vyskyt[x] / len(rozhodnutia))

    for x in sorted_slova:
        if x in normovane_vyskyt:
            normovane_slova[x] = sorted_slova[x] / len(rozhodnutia)

    # print(sorted_vyskyt)
    return (normovane_slova, normovane_vyskyt)


def vratRozdiely(n,pocet, dict1, dict0, atribut):
    for x in dict1:
        if x in dict0:
            dict1[x] = dict1[x] - dict0[x]
    sorted_dict1 = dict(sorted(dict1.items(), key=operator.itemgetter(1), reverse=True))
    rozdiely_items = sorted_dict1.items()
    # print(list(rozdiely_items)[:5])
    if pocet == 1:
        najdiSlova(list(rozdiely_items)[:n], atribut, 0)
    else:
        najdiNgramy(n, list(rozdiely_items)[:n], atribut, 0)
    return list(rozdiely_items)[:n]


def najdiSlova(dict, atribut, hodnota):
    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = " + str(hodnota) + ""
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    rozhodnutia = []
    for p in pole:
        rozhodnutia.append(str(p)[2:][: - 2] + ".json")
    final = {}
    pole2 = os.listdir("dataset_lemmatized")
    for x in dict:
        final[x[0]] = {}
        for y in rozhodnutia:
            if y in pole2:
                string = ""
                a_file = open("dataset_lemmatized/" + y, "r", encoding='utf-8')
                json_object = json.load(a_file)
                slova = json_object["dokument_fulltext"]
                if x[0] in slova:
                    index = slova.index(x[0]) - 5
                    for r in range(10):
                        if index < len(slova):
                            string = string + " " + slova[index]
                            index += 1
                    final[x[0]][y] = {str(string)}

    # print(final)


def ngramy(n, atribut, hodnota):
    subory = []
    for file in os.listdir("dataset_lemmatized"):
        if file.endswith(".json"):
            subory.append(file)
    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = " + str(hodnota) + ""
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    rozhodnutia = []

    for x in pole:
        if str(x)[2:][: - 2] + ".json" in subory:
            rozhodnutia.append(str(x)[2:][: - 2] + ".json")
    ngramy = {}
    vyskyt = {}
    normovane_ngramy = {}
    normovane_vyskyt = {}
    for p in rozhodnutia:
        ngramyVRozhodnuti = []
        a_file = open("dataset_lemmatized/" + str(p), "r", encoding='utf-8')
        json_object = json.load(a_file)
        array = json_object["dokument_fulltext"]
        for x, _ in enumerate(array):
            if x + n < len(array):
                if len(array[x]) > 3:
                    ngram = ""
                    poc = 0
                    for y in range(n):
                        ngram = ngram + " " + array[x + poc]
                        poc += 1
                    ngram = ngram.strip()
                    if ngram in ngramy:
                        ngramy[ngram] += 1
                        if ngram not in ngramyVRozhodnuti:
                            ngramyVRozhodnuti.append(ngram)
                    else:
                        ngramy[ngram] = 1
        for y in ngramyVRozhodnuti:
            if y in vyskyt:
                vyskyt[y] += 1
            else:
                vyskyt[y] = 1

    sorted_ngramy = dict(sorted(ngramy.items(), key=operator.itemgetter(1), reverse=True))
    sorted_vyskyt = dict(sorted(vyskyt.items(), key=operator.itemgetter(1), reverse=True))

    for x in sorted_vyskyt:
        # podiel = sorted_vyskyt[x] / len(pole)
        # if podiel > 0.5:
        normovane_vyskyt[x] = 100 * (sorted_vyskyt[x] / len(rozhodnutia))

    for x in sorted_ngramy:
        if x in normovane_vyskyt:
            normovane_ngramy[x] = sorted_ngramy[x] / len(rozhodnutia)

    return (rozhodnutia,normovane_ngramy, normovane_vyskyt)


def najdiNgramy(n, dict, atribut, hodnota):
    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = " + str(hodnota) + ""
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    rozhodnutia = []
    for p in pole:
        rozhodnutia.append(str(p)[2:][: - 2] + ".json")
    final = {}
    pole2 = os.listdir("dataset_lemmatized")
    for x in dict:
        final[x[0]] = {}
        for y in rozhodnutia:
            if y in pole2:
                string = ""
                a_file = open("dataset_lemmatized/" + y, "r", encoding='utf-8')
                json_object = json.load(a_file)
                slova = json_object["dokument_fulltext"]
                poleNgramov = []
                for s, _ in enumerate(slova):
                    if s + n < len(slova):
                        ngram = ""
                        poc = 0
                        for r in range(n):
                            ngram = ngram + " " + slova[s + poc]
                            poc += 1
                        poleNgramov.append(ngram.strip())
                if x[0] in poleNgramov:
                    index = poleNgramov.index(x[0]) - 3
                    for r in range(7):
                        if index < len(poleNgramov):
                            string = string + " " + poleNgramov[index].split()[0]
                            index += 1
                    final[x[0]][y] = {str(string)}

    # print(final)

def najdiTop(atribut,n):
    top = {}
    pocitadlo = 2
    vsetky_rozhodnutia = []
    rozhodnutia1, dict1, vyskyt1 = ngramy(pocitadlo, atribut, 1)
    for r in rozhodnutia1:
        vsetky_rozhodnutia.append(r)
    rozhodnutia2, dict1, vyskyt1 = ngramy(pocitadlo, atribut, 0)
    for r in rozhodnutia2:
        vsetky_rozhodnutia.append(r)
    dict2, vyskyt2 = slova(atribut, 1)
    dict3, vyskyt3 = slova(atribut, 0)
    hladane = vratRozdiely(n, 1, vyskyt2, vyskyt3, atribut)
    print("Slova:")
    print(hladane)
    for x in hladane:
        top[x[0]] = x[1]
    for y in range(3):
        roz1, dict1, vyskyt1 = ngramy(pocitadlo, atribut, 1)
        roz2, dict0, vyskyt0 = ngramy(pocitadlo, atribut, 0)
        hladane = vratRozdiely(n, pocitadlo, vyskyt1, vyskyt0, atribut)
        print(str(pocitadlo)+"gramy")
        print(hladane)
        for x in hladane:
            top[x[0]] = x[1]
        pocitadlo += 1
    print(top)
    sorted_top = dict(sorted(top.items(), key=operator.itemgetter(1), reverse=True))
    topn = (list(sorted_top)[:n])
    print("TOP")
    print(topn)
    hladajNgramyVRozhodnutiach(vsetky_rozhodnutia, topn, atribut)

def hladajNgramyVRozhodnutiach(vsetky,hladane, atribut):
    subory = []
    for file in os.listdir("dataset_lemmatized"):
        if file.endswith(".json"):
            subory.append(file)
    vysledok = {}
    for p in vsetky:
        vysledok[p] = {}
        for h in hladane:
            vysledok[p][h] = 0
        bigramy = []
        trigramy = []
        styrigramy = []
        a_file = open("dataset_lemmatized/" + str(p), "r", encoding='utf-8')
        json_object = json.load(a_file)
        array = json_object["dokument_fulltext"]
        slova = array
        for x, _ in enumerate(array):
            if x + 4 < len(array):
                if len(array[x]) > 3:
                    bigram = ""
                    trigram = ""
                    styrigram = ""
                    poc = 0
                    for y in range(2):
                        bigram = bigram + " " + array[x + poc]
                        poc += 1
                    bigramy.append(bigram.strip())
                    poc = 0
                    for y in range(3):
                        trigram = trigram + " " + array[x + poc]
                        poc += 1
                    trigramy.append(trigram.strip())
                    poc = 0
                    for y in range(4):
                        styrigram = styrigram + " " + array[x + poc]
                        poc += 1
                    styrigramy.append(styrigram.strip())

        for h in hladane:
            dlzka = len(h.split())
            if dlzka == 1:
                if h in slova:
                    vysledok[p][h] = 1
            if dlzka == 2:
                if h in bigramy:
                    vysledok[p][h] = 1
            if dlzka == 3:
                if h in trigramy:
                    vysledok[p][h] = 1
            if dlzka == 4:
                if h in styrigramy:
                    vysledok[p][h] = 1

    print(vysledok)

    urcHodnotuAtributu(vysledok, hladane, atribut)


def urcHodnotuAtributu(vyskyty,hladane, atribut):
    vystup = []
    for v in vyskyty:
        hodnota = 0
        for key, value in vyskyty[v].items():
            hodnota = hodnota + value
        if hodnota < (len(hladane)//2)+1:
            dvojica = (str(v), str(0))
            vystup.append(dvojica)
        if hodnota > len(hladane)//2:
            dvojica = (str(v), str(1))
            vystup.append(dvojica)

    print("Hodnoty atribútu v súdnych rozhodnutiach:")
    print(vystup)
    kontrola(vystup, atribut)


def kontrola(vystup, atribut):
    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = 1"
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    perf_measure = {'TP': 0, 'TN': 0, 'FP': 0, 'FN': 0}
    rozhodnutia = []
    for p in pole:
        rozhodnutia.append(str(p)[2:][: - 2] + ".json")
    for v in vystup:
        if v[0] in rozhodnutia and str(v[1]) == str(1):
            perf_measure["TP"] += 1
        elif v[0] not in rozhodnutia and str(v[1]) == str(0):
            perf_measure["TN"] += 1
        elif v[0] in rozhodnutia and str(v[1]) == str(0):
            perf_measure["FN"] += 1
        elif v[0] not in rozhodnutia and str(v[1]) == str(1):
            perf_measure["FP"] += 1

    accuracy = (perf_measure["TP"] + perf_measure["TN"]) / (
            perf_measure["TP"] + perf_measure["TN"] + perf_measure["FP"] + perf_measure["FN"])
    precision = perf_measure["TP"] / (perf_measure["TP"] + perf_measure["FP"])
    recall = perf_measure["TP"] / (perf_measure["TP"] + perf_measure["FN"])
    f1 = (2 * (recall * precision)) / (recall + precision)

    print("")
    print(perf_measure)
    print("Accuracy: " + str(accuracy))
    print("Precision: " + str(precision))
    print("Recall: " + str(recall))
    print("F1 score: " + str(f1))
    print("")
